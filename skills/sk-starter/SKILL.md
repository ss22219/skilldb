---
name: sk-starter
description: ChatGPT 从零到一通关全流程新手教程 Skill (/sk-starter)。第一步：配置 VPN 网络；第二步：安装桌面版客户端；第三步：购买账号与 Plus 订阅接码。
---

# ChatGPT 通关全流程新手教程 Skill (/sk-starter)

本 Skill 用于引导新手用户从零开始，按三大核心步骤完成 ChatGPT 的网络配置、软件安装与账号订阅。

---

## 🧭 三步通关流程图

```mermaid
flowchart TD
    subgraph 第一步：配置 VPN 网络
        A1[访问 https://古拉.com/] --> A2[注册并按月订阅机场套餐]
        A2 --> A3[下载配置 Clash 客户端并开启系统代理]
    end

    subgraph 第二步：安装 ChatGPT 客户端
        B1{系统类型判断}
        B1 -->|macOS| B2[下载 DMG 离线包安装]
        B1 -->|Windows| B3[设置区域为“美国”] --> B4[Winget/MSIX 部署]
    end

    subgraph 第三步：购买账号与 Plus 订阅
        C1[访问 https://aiprobe.top/] --> C2[对比购买低价 Plus 成品号/代充]
        C2 --> C3[接入 SMS-Activate 租号接收 OTP 验证码]
    end

    A3 --> B1
    B2 --> C1
    B4 --> C1
```

---

## 第一步：配置 VPN 网络 (解锁基础设施)

1. **访问服务商**：在浏览器打开 `https://古拉.com/` (转码域名: `https://xn--w4r430a.com/`)。如遇到 DNS 拦截，建议调整系统的 DNS 为 `223.5.5.5` 或 `1.1.1.1`。
2. **注册与订阅**：点击注册账号，在控制面板选择按月订阅套餐（建议月付降低风险）。
3. **安装配置 Clash 客户端**：
   - **Windows**: 下载安装 [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev/releases)。
   - **macOS**: 下载安装 [Clash Verge Rev for macOS](https://github.com/clash-verge-rev/clash-verge-rev/releases) 或 ClashX Meta。
   - **Android**: 安装 [Clash Meta for Android](https://github.com/MetaCubeX/ClashMetaForAndroid/releases)。
   - **iOS**: 使用美区 Apple ID 在 App Store 下载 Shadowrocket (小火箭)。
4. **导入并开启代理**：在古拉后台点击“一键导入 Clash”，在客户端中选中节点，切换模式为 **规则模式 (Rule)** 并开启 **系统代理 (System Proxy)**。

---

## 第二步：安装 ChatGPT 官方桌面版客户端

根据操作系统执行不同的安装方案：

### macOS 用户：
- 直接下载官方离线 DMG 安装包：[https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg](https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg)
- 下载后双击打开，将 `ChatGPT.app` 拖入 `Applications` 应用程序文件夹即可。

### Windows 用户（突破“地区不可用”限制）：
1. **修改系统区域**：按 **Win + I** 打开设置 -> **时间及语言** -> **区域** -> 将“国家或地区”修改为 **美国 (United States)**（即时生效，无需重启）。
2. **方法 A（官方推荐 Winget 一键安装）**：以管理员身份打开终端运行：
   ```powershell
   winget install --id=9NT1R1C2HH7J -e
   ```
3. **方法 B（离线包安装）**：打开抓包网站 [store.rg-adguard.net](https://store.rg-adguard.net/)，选 ProductId 输入 `9NT1R1C2HH7J` 搜索，下载 `.msixbundle` 后通过 `Add-AppxPackage -Path "C:\下载路径\ChatGPT.msixbundle"` 进行安装。

---

## 第三步：购买账号与 Plus 订阅接码

1. **低价资源对比与采购**：
   - 访问 `https://aiprobe.top/`，利用 `aiprobe-plus-buyer` 检索并对比全网低价且带质保的 ChatGPT Plus 成品号、代充与兑换码。
2. **接码渠道验证**：
   - 注册或升级新账号遇到手机号验证时，接入 SMS 接码渠道（SMS-Activate / 5SIM）。
   - 租用 OpenAI 专属号码，自动轮询获取 6 位数 SMS OTP 验证码完成绑定与 Plus 升级。

---

## 💻 命令行快速调用

在终端或 Agent 中输入：

```text
/sk-starter
```

即可开启分步全流程互动引导。
