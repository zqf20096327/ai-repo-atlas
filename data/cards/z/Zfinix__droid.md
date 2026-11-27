# Zfinix/droid

⭐ 11 · Kotlin · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/Zfinix/droid) · [官网](https://droid.withaster.dev) · 组织维护

**让 AI agent 像用户一样操作 Android 手机的应用，支持任意模型与 MCP/ACP 接入**

Droid 是一个 Android 应用（dev.aster.probe），通过无障碍服务让 AI agent 读取屏幕、点击、滑动并输入文字，从而在用户的应用中以用户的账号完成任务。模型可自由选择：免账号免费模型、本地 Ollama/LM Studio 或 40 家带密钥的 provider。电脑端 Claude Code、Codex、Cursor 等 MCP 客户端可将手机屏幕作为工具，Zed 与 JetBrains 经 ACP 与手机上的 agent 通信，连接方式支持 USB、Wi-Fi 与 Tailscale。README 自述项目为实验性，仅支持 Android 8+ 的 arm64-v8a 设备，无 iPhone 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过无障碍服务读屏、点击、滑动、输入，在用户的应用中执行操作
- 支持 40 家 provider 与本地模型服务器，聊天中可切换模型与推理力度
- MCP/ACP 双通道：任意 MCP 客户端驱动手机，Zed/JetBrains 经 ACP 对话
- /remember、/learn、/skills 技能保存，agent 自行调度唤醒并复盘最短路径

## 适用场景

- 让 AI 代我在手机上完成下单、开关设置等操作
- 把手机屏幕作为 MCP 工具接入电脑端的 Claude Code/Codex/Cursor
- 在 Telegram/WhatsApp/iMessage 里远程指挥手机做事

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: An agent that uses your Android phone the way you do. Run it on any model,
> L19: Droid (`dev.aster.probe`) gives an AI agent your phone's screen. An accessibility service lets it read, tap, swipe 
> L21: - **Any model.** Free models with no account and no key, Ollama or LM Studio on your own computer, or a key for one


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `9dafd3c5393c` · [字段定义](../../DATASET.md)*
