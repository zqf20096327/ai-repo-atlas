# Cyapstaye/Adame_ver.open

⭐ 15 · Python · 推送 2026-07-01 · [GitHub](https://github.com/Cyapstaye/Adame_ver.open) · [官网](https://adame.ai) · 个人维护

**macOS 桌面 Agent 应用：自带工具/技能/终端运行多步 AI 代理**

面向 macOS 的 Electron + React 桌面应用，搭配本地 Python agent 后端（JSON-RPC over stdio），让用户在本地运行带工具、技能库、内嵌 pty 终端的多步 AI agent。支持接入 OpenAI/Anthropic/DeepSeek 或本地模型，API key 经 OS keychain 加密存储，也可用 ChatGPT OAuth 登录；支持 MCP 客户端、会话检查点、上下文压缩与设备端记忆。开发需 Node.js 20.19+ 与 Python 3.11+，打包版后端经 PyInstaller 编译为独立二进制。许可尚待确定（License to be determined）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Electron UI + Python agent 后端双进程架构（JSON-RPC over stdio）
- 自带模型接入 OpenAI/Anthropic/DeepSeek/本地模型，key 经 OS keychain 加密存储
- 内置工具与 MCP 客户端，连接外部工具服务器
- 检查点、上下文压缩与设备端记忆支持长 agent 会话

## 适用场景

- 在 macOS 本地运行多步 AI agent 完成研究、创作与开发任务
- 通过 MCP 接入外部工具服务器扩展 agent 能力
- 用自有 API key 在应用内直接调用多家模型

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L5: **Adame is an agentic desktop app for macOS.** It pairs a native Electron + React
> L6: interface with a local Python agent backend, so you can run multi-step AI agents —
> L7: with tools, skills, an embedded terminal, and your own API keys — directly on your

## 星数曲线

```mermaid
xychart-beta
    title "Cyapstaye/Adame_ver.open 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `41bb8cd9aa28` · [字段定义](../../DATASET.md)*
