# CodeAndCanvasLabs/Daemora

⭐ 16 · TypeScript · AGPL-3.0 · 推送 2026-06-18 · [GitHub](https://github.com/CodeAndCanvasLabs/Daemora) · [官网](https://daemora.com) · 组织维护

**自托管自主 AI agent 平台：多模型、20 通道、MCP 工具集成**

自托管的自主 AI agent 平台：部署后连接 Telegram、Discord、Slack 等 20 个消息通道，通过对话让 agent 写代码、做研究、发邮件、跑定时任务。支持 7 家模型提供商（OpenAI/Anthropic/Google/xAI/DeepSeek/Mistral/Ollama，59+ 模型），提供按任务类型的模型路由、52 个内置工具、任意 MCP server 接入、多 agent 团队与并行子 agent、三层记忆、OAuth 一键集成 13 项服务。提供 macOS/Windows 原生安装包或 npm 全局安装，以守护进程方式常驻运行；需至少一个模型 API key（Ollama 本地除外）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 家模型提供商 59+ 模型，支持任务类型路由与提供商故障转移
- 20 个消息通道与 13 项 OAuth 集成（X/Gmail/GitHub/Notion 等）
- 任意 MCP server 接入 + 52 个内置工具 + 多 agent 团队
- 三层记忆（语义/情景/程序性）与循环检测、生产级调度

## 适用场景

- 在自己服务器上部署一个 7x24 小时自主干活的 AI agent
- 通过 Telegram/Discord 等消息渠道指挥 agent 写代码、做研究、发邮件
- 用 Ollama 本地模型搭建不依赖外部 API 的 agent
- 设置 GitHub issue 触发、定时任务等自动化流程

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Daemora - Autonomous AI Agent
> L12: Deploy once on your machine. Connect your channels. Message the bot - it writes code, does research, sends emails, 
> L163: |**Ollama**|`llama3`, `llama3.1`, `qwen2.5-coder` - local, no API key needed|

## 星数曲线

```mermaid
xychart-beta
    title "CodeAndCanvasLabs/Daemora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c1c6a21a2611` · [字段定义](../../DATASET.md)*
