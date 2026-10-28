# marceloeatworld/clopinette-ai

⭐ 28 · TypeScript · 推送 2026-10-08 · [GitHub](https://github.com/marceloeatworld/clopinette-ai) · [官网](https://clopinette.app) · 个人维护

**部署在 Cloudflare Workers 上的自托管多平台 AI agent，带持久记忆与 13 工具**

面向自托管用户的多平台 AI agent：以 Cloudflare Workers + Durable Objects 为运行时，每用户一个隔离 DO 与 SQLite，Web UI 经 WebSocket 流式对话，并通过 webhook 接入 Telegram / WhatsApp / Discord / MCP。提供 13 个工具（网页、文档 RAG、记忆、日历、待办、图像生成、TTS、浏览器、异步委派等）、5 层记忆、技能中心（含安装前提示注入扫描）、BYOK 13 家模型商经 AI Gateway 接入。部署需 Bun、Wrangler 与 Workers 付费计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个工具：网页搜索、文档 RAG（AutoRAG）、图像生成、TTS、浏览器（Playwright MCP）、并行研究子 agent 等
- 5 层记忆：MEMORY.md/USER.md、FTS5+Vectorize 混合检索、记忆 flush、技能索引、可选 Honcho
- BYOK 支持 13 家模型商，经 Cloudflare AI Gateway 接入，可跨厂商配置辅助模型
- 技能 Hub 含内置 10 技能与外部仓库导入，安装前扫描提示注入/密钥外泄结构

## 适用场景

- 自建跨 Telegram/WhatsApp/Discord/Web 的个人 AI 助手并保留持久记忆
- 对自己上传的文档做 RAG 问答与深度研究（并行子 agent）
- 用自带 API key 在 Cloudflare 上运行多模型 agent 以控制成本

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: Cloudflare-native AI agent with persistent memory, a built-in skills hub, multimodal I/O, and Telegram / WhatsApp / 
> L29: - **Tool-driven runtime** — web, docs, memory, history, skills, notes, calendar, todo, image, tts, clarify, with op

## 星数曲线

```mermaid
xychart-beta
    title "marceloeatworld/clopinette-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9d534dfaccab` · [字段定义](../../DATASET.md)*
