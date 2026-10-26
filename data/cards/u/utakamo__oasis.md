# utakamo/oasis

⭐ 40 · Lua · MIT · 推送 2026-10-25 · [GitHub](https://github.com/utakamo/oasis) · [官网](https://utakamo.com/article/openwrt/myapp/oasis/intro.html) · 个人维护 · 中文 README

**OpenWrt 路由器上的 AI 聊天助手，用 AI 生成并校验路由器配置**

面向 OpenWrt 24.x 的三件套应用：oasis 提供 CUI 聊天核心，luci-app-oasis 在 LuCI WebUI 中提供聊天界面，oasis-mod-tool 让 AI 调用本机工具（如查询 LAN IP）。用户对话后由 AI 给出 OpenWrt 最优设置建议，设备端分析回应中的 UCI 命令序列并验证可执行性后弹窗通知。支持 OpenAI/Ollama/Gemini/Anthropic/OpenRouter/LM Studio 作为后端，可自定义系统消息、加载/恢复聊天记录，通过 JSON-RPC 供手机端应用集成。README 自述为实验性软件，现阶段不面向最终用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 6 种 AI 服务后端（OpenAI/Ollama/Gemini/Anthropic/OpenRouter/LM Studio）
- 设备端分析并验证 AI 回应中的 UCI 命令序列可执行性
- oasis-mod-tool 扩展使 AI 可调用本机工具，工具可作为插件添加
- JSON-RPC 接口供智能手机聊天应用等外部设备集成

## 适用场景

- 在路由器 WebUI 里与 AI 对话获取 OpenWrt 设置建议
- 通过系统消息预置知识让 AI 专注于特定配置任务
- 手机端聊天应用经 RPC 接入路由器上的 AI 服务

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L18: This software provides the ability to link OpenWrt and AI. Based on user input, the AI provides the optimal setting
> L22: |oasis|AI chat core software (provides stand-alone CUI-based chat functionality)|
> L23: |luci-app-oasis|This is a plugin to use AI chat from within LuCI's WebUI. (base software is oasis)|

## 星数曲线

```mermaid
xychart-beta
    title "utakamo/oasis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3ab429c27800` · [字段定义](../../DATASET.md)*
