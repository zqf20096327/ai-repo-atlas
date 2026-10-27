# joexk1/JoeBro

⭐ 90 · Swift · GPL-3.0 · 推送 2026-10-14 · [GitHub](https://github.com/joexk1/JoeBro) · [官网](https://joexk1.github.io/joebro/) · 个人维护

**给个人用户的本地优先 macOS AI 工作区应用**

原生 SwiftUI macOS 桌面应用，内置纯 Python 标准库后端（随应用启动、本地 127.0.0.1:8765 通信）。用户自带模型：可接 Ollama 等本地模型或 OpenAI/DeepSeek/Anthropic 等任意 OpenAI 兼容 API key。功能包括聊天与 Agent 模式（读文件、编辑 Word 文档、跑终端、搜索网页）、Deep Research 生成带引用报告、IMAP 邮件、日历、持久化长期记忆（Brain）、技能学习、API 工具/MCP 服务器/插件三层工具体系，以及 Telegram 机器人远程编排。数据存本地 SQLite，默认开启 Cloak Mode 脱敏。要求 macOS 26+ Apple Silicon，提供未公证 dmg 下载，需 Xcode 26 构建源码。限制：手机配对需自建姐妹仓库 JoeBro Mobile，且仅在 Mac 运行时可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Agent 模式可读文件、编辑 .docx、跑终端、调用自建 API 工具/MCP 服务器/插件
- 长期记忆 Brain 以单条事实存储并生成可交互记忆图谱
- 零外部依赖后端（纯 Python 标准库），无需 pip 安装
- 默认 Cloak Mode：密钥与敏感信息在请求发出前替换为占位符

## 适用场景

- 在一个窗口里用自有模型聊天、处理邮件、管理日历和文档
- 让 Agent 代为执行文件编辑、终端命令与网页研究
- 通过 Telegram 机器人远程驱动 Mac 上的工作区

## 场景标签

`AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: JoeBro is another way. It hands a busy person the full power of modern AI without asking them to become a software 
> L33: - **Chat** with any model, with live streaming, extended thinking, and a real agent mode. Sort chats into folders t
> L107: - **Bring your own models.** Run local models with Ollama (or anything OpenAI-compatible) over your network, or pa

## 星数曲线

```mermaid
xychart-beta
    title "joexk1/JoeBro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-27 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `f0e3a1ace2fc` · [字段定义](../../DATASET.md)*
