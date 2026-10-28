# opencrust-org/opencrust

⭐ 147 · Rust · MIT · 推送 2026-10-19 · [GitHub](https://github.com/opencrust-org/opencrust) · 组织维护

**Rust 编写的个人多 agent AI 助手平台，覆盖多聊天渠道**

单个 16 MB 二进制的 AI agent 运行平台，用 Rust 编写，将 agent 接入 Telegram、Discord、Slack、WhatsApp、LINE、微信、iMessage、MQTT 等 9 个渠道，内置 Web 聊天界面与终端聊天。支持 15 个 LLM 提供商（Anthropic、OpenAI、Ollama 原生接入及 12 个 OpenAI 兼容端点）、MCP 工具接入、SKILL.md 技能体系（兼容 agentskills.io）与自学习技能生成。安全机制含 AES-256-GCM 凭据加密库、默认认证、提示注入检测、速率与 token 预算限制。提供文档 RAG（SQLite + 向量检索）、定时任务、多 agent 路由与 WASM 沙箱插件。提供各平台预编译二进制，也可 cargo 源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 16 MB 二进制接入 9 个聊天渠道，空闲内存 13 MB
- 15 个 LLM 提供商：Anthropic/OpenAI/Ollama 原生 + 12 个 OpenAI 兼容端点
- MCP 支持（Stdio + HTTP）与 agentskills.io 兼容的 SKILL.md 技能体系
- 跨会话模式追踪的自学习技能生成（含置信门控与提示注入扫描）

## 适用场景

- 在 Telegram/Discord/微信等渠道运行 7x24 个人 AI 助手
- 通过文档 RAG 让 agent 自动检索并引用我的资料回答
- 用 SKILL.md 定义技能并从社区 hub 安装
- 配置多个命名 agent 并用 handoff 路由任务

## 场景标签

`AI 助手` `多智能体` `聊天机器人` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L27: A single 16 MB binary that runs your AI agents across Telegram, Discord, Slack, WhatsApp, WhatsApp Web, LINE, WeCha
> L119: ### LLM Providers

## 星数曲线

```mermaid
xychart-beta
    title "opencrust-org/opencrust 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 145 --> 148
    line [146, 147, 147]
```

2026-10-18 146 → 2026-10-28 147（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e5bb8f3d0596` · [字段定义](../../DATASET.md)*
