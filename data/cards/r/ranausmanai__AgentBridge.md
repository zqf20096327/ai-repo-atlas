# ranausmanai/AgentBridge

⭐ 21 · TypeScript · MIT · 推送 2026-03-04 · [GitHub](https://github.com/ranausmanai/AgentBridge) · [官网](https://agentbridge.cc) · 个人维护

**把任意 OpenAPI API 快速变为 AI agent 可调用的桥接工具**

面向 API 所有者与 agent 开发者的桥接框架：粘贴 OpenAPI 规范生成 .agentbridge.json manifest，发布到 agentbridge.cc 目录后任何 AI agent 可发现并调用该 API；支持 well-known URL 自动发现。agent 侧提供 CLI 对话、MCP server（接入 Claude Desktop/Cursor/Windsurf）、TypeScript SDK 与网页聊天，LLM 采用自带 key 模式（Claude/GPT/Groq/Ollama 及任意 OpenAI 兼容端点）。支持 Docker 与 Vercel 自托管，认证为可选项（不设 Supabase 变量则免登录运行）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAPI spec 一条命令生成 .agentbridge.json manifest
- CLI/MCP server/SDK/Web 四种使用形态
- LLM provider 覆盖 Claude、GPT、Groq、Ollama 及 OpenAI 兼容端点（BYOK）
- 支持 Docker 自托管与 .well-known URL 自动发现

## 适用场景

- API 所有者让自己的服务被 AI agent 发现和调用
- 为 Claude Desktop/Cursor/Windsurf 配置任意 API 的 MCP 接入
- agent 开发者通过 CLI 或 SDK 直接对话式调用公开 API

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L25: Most APIs are built for humans writing code. But AI agents need to **discover, understand, and call APIs autonomous
> L168: |`@agentbridgeai/llm`|LLM providers — Claude, GPT, Groq, Ollama, any OpenAI-compatible|npm|

## 星数曲线

```mermaid
xychart-beta
    title "ranausmanai/AgentBridge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `875b59484d80` · [字段定义](../../DATASET.md)*
