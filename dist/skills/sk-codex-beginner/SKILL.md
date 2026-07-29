---
name: sk-codex-beginner
description: 中国大陆小白用户从 0 到 1 成功使用 OpenAI Codex / ChatGPT 桌面版的极简全流程通关 Skill (/sk-codex-beginner)。包含网络解锁、客户端安装、账号获取及 Codex 手机接码全步骤。
---

# 小白国内使用 OpenAI Codex 从零到一极简通关指南 (/sk-codex-beginner)

针对中国大陆零基础用户（小白），提供一条**无缝通关路径**。只需要按顺序完成以下 4 个阶段，即可顺畅使用 OpenAI Codex / ChatGPT 桌面版。

---

## 🧭 0 到 1 全流程通关路线图

```mermaid
flowchart TD
    subgraph 阶段一：网络准备 (解锁访问)
        A1[访问 https://古拉.com/] --> A2[注册并按月订阅机场套餐]
        A2 --> A3[安装 Clash Verge Rev 客户端]
        A3 --> A4[导入订阅，开启系统代理 + 规则模式]
    end

    subgraph 阶段二：安装客户端 (突破限制)
        B1{系统类型判断}
        B1 -->|macOS| B2[下载 ChatGPT.dmg 官方离线包]
        B1 -->|Windows| B3[设置区域为美国 -> Winget 一键安装]
    end

    subgraph 阶段三：账号与 Codex 手机接码
        C1[从 aiprobe.top 获取稳定成品号/代充] --> C2[接码渠道租用号码接收 Codex 短信验证码]
    end

    subgraph 阶段四：启动体验 Codex
        D1[打开桌面应用登录账号] --> D2[解锁 Codex 代码大模型助手]
    end

    A4 --> B1
    B2 --> C1
    B3 --> C1
    C2 --> D1
```

---

## 阶段一：网络准备 (解决打不开与 403 阻断)

> **小白痛点**：在大陆直接访问 OpenAI 官网或 Codex 会提示“403 Forbidden”或“无法访问”。

1. **访问机场服务商**：在浏览器打开 `https://古拉.com/` (Punycode 映射域名: `https://xn--w4r430a.com/`)。若遇到拦截打不开，请将系统 DNS 改为 `223.5.5.5` 或 `1.1.1.1`。
2. **注册与购买订阅**：注册账号登录后台，在“商店”购买按月订阅套餐（建议月付降低风险）。
3. **下载安装 Clash 客户端**：
   - **Windows 用户**: 下载安装 [Clash Verge Rev x64 安装包](https://github.com/clash-verge-rev/clash-verge-rev/releases)。
   - **macOS 用户**: 下载安装 [Clash Verge Rev for Mac](https://github.com/clash-verge-rev/clash-verge-rev/releases)。
4. **导入并连接代理**：
   - 在古拉后台点击 **“一键导入 Clash”**。
   - 在软件界面中选中节点配置，模式选择 **规则模式 (Rule)**，并勾选开启 **系统代理 (System Proxy)**。

---

## 阶段二：安装 ChatGPT / Codex 桌面版

> **小白痛点**：在 Windows 微软商店搜不到应用，提示“在你所在的地区不可用”。

### macOS 用户指南：
直接下载官方 DMG 离线包文件：[ChatGPT.dmg](https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg)，双击拖入 `Applications` 应用程序文件夹即可完成安装。

### Windows 用户指南（突破区域限制）：
1. **修改系统地区为美国**：按键盘 **Win + I** 打开设置 -> **时间及语言** -> **区域** -> 将“国家或地区”下拉框修改为 **美国 (United States)**。（*修改即时生效，无需重启*）。
2. **使用 Winget 一键安装**：以管理员身份打开终端 / PowerShell，运行：
   ```powershell
   winget install --id=9NT1R1C2HH7J -e
   ```
   提示协议输入 `Y` 回车即可自动安装完成。

---

## 阶段三：获取账号与 Codex 手机短信接码

> **小白痛点**：没有国外手机号，提示“Need Phone Number Verification for Codex”。

1. **获取账号/Plus 订阅**：
   - 访问 `https://aiprobe.top/`，系统会自动利用 `/aiprobe-plus-buyer` 过滤掉扫码、提链、免费等杂项，返回纯净且带首登质保的成品号或 Plus 订阅。
2. **Codex 手机接码验证**：
   - 使用 SMS 接码客户端（支持 SMS-Activate / 5SIM）。
   - 选择服务代码 `openai` 或 `dr` (Codex)，租用可接收短信的临时号码（成本约 1-3 元）。
   - 将租用到的号码填入 OpenAI 验证框，系统会自动轮询获取 6 位数 SMS 验证码完成绑定。

---

## 阶段四：启动体验 Codex

1. 打开安装好的 ChatGPT / Codex 桌面应用。
2. 登录刚刚验证通过的账号。
3. 即可开始在应用中体验 OpenAI Codex 代码自动生成、智能 Debug 与 Pair Programming 助手！

---

## 💻 命令行快速体验

在终端输入：

```bash
cd c:\Users\gool\Desktop\skilldb\skills\sk-codex-beginner\scripts
python cli.py
```
