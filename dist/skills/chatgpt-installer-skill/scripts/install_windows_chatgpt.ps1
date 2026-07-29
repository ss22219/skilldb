<#
.SYNOPSIS
    Automated Windows ChatGPT Desktop Installation Script (Region Bypass & Store ID 9NT1R1C2HH7J)
#>

param (
    [string]$MsixPath = ""
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "   Windows ChatGPT 官方桌面版自动化安装   " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Check System Region
$currentGeo = (Get-ItemProperty -Path "HKCU:\Control Panel\International\Geo" -Name "Nation" -ErrorAction SilentlyContinue).Nation
Write-Host "[1/3] 检查系统区域设置..." -ForegroundColor Yellow

if ($currentGeo -ne "244") { # 244 is GeoID for US
    Write-Host "⚠️  提示: 当前系统区域未设为“美国” (United States)。" -ForegroundColor Yellow
    Write-Host "👉 建议先按 Win + I 打开设置 -> 时间及语言 -> 区域 -> 国家或地区修改为“美国”。" -ForegroundColor Yellow
} else {
    Write-Host "✅ 系统区域已被设为美国 (United States)。" -ForegroundColor Green
}

# 2. Local MSIX bundle install if provided
if ($MsixPath -ne "" -and (Test-Path $MsixPath)) {
    Write-Host "`n[2/3] 使用离线包安装: $MsixPath ..." -ForegroundColor Yellow
    try {
        Add-AppxPackage -Path $MsixPath -ErrorAction Stop
        Write-Host "🎉 成功部署离线包！可以在“开始”菜单中打开 ChatGPT 了。" -ForegroundColor Green
        exit 0
    } catch {
        Write-Host "❌ 离线包安装失败: $_" -ForegroundColor Red
    }
}

# 3. Try Winget Install
Write-Host "`n[2/3] 尝试使用 Windows 包管理器 Winget 抓取官方包安装..." -ForegroundColor Yellow
$wingetExists = Get-Command winget -ErrorAction SilentlyContinue

if ($wingetExists) {
    Write-Host "执行命令: winget install --id=9NT1R1C2HH7J -e" -ForegroundColor Gray
    winget install --id=9NT1R1C2HH7J -e
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n🎉 官方 ChatGPT 桌面版安装完成！请在“开始”菜单查找使用。" -ForegroundColor Green
        exit 0
    } else {
        Write-Host "⚠️ Winget 安装返回非零状态。如未安装成功，请使用离线包方式。" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠️ 系统中未找到 winget 命令。" -ForegroundColor Yellow
}

# 4. Manual Fallback Instructions
Write-Host "`n==========================================" -ForegroundColor Cyan
Write-Host "   离线包手动安装备用方案说明" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "1. 打开浏览器访问在线抓包网站: https://store.rg-adguard.net/"
Write-Host "2. 左侧选 ProductId ，中间输入 ChatGPT 产品 ID: 9NT1R1C2HH7J ，右侧选 Retail 点击搜索"
Write-Host "3. 在结果中找到以 .msixbundle 结尾的文件（约 200MB+）并下载"
Write-Host "4. 下载后在 PowerShell (管理员) 执行:"
Write-Host "   Add-AppxPackage -Path `"C:\路径\文件名.msixbundle`""
