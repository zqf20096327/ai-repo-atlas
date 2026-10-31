# Djtony707/TITAN

⭐ 19 · TypeScript · MIT · 推送 2026-10-30 · [GitHub](https://github.com/Djtony707/TITAN) · [官网](https://lakelogicai.net/) · 个人维护

**本地优先的 AI agent 框架：多智能体组成团队并自学习技能**

TypeScript 编写、MIT 许可的本地优先 AI agent 框架，npm 全局安装。v8 将 agent 组织为“公司”：每个成员有独立 ed25519 身份、专属模型与 harness，共享基于 SQLite FTS5 的本地索引记忆；所有事件经哈希链签名，离线可验证。支持 36 个 LLM 提供方，含 Ollama、vLLM、llama.cpp/LM Studio 等本地后端与 OpenAI 兼容端点。提供技能自学习（replay 考试验证）、Mixture of Agents、验证墙与 Reliability Mode 等机制，8700+ 测试。README 声明项目正演进为下一代 Odyssey（开发中）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 agent “公司”结构：独立密钥身份、专属模型与 harness、共享记忆
- 哈希链签名事件日志，离线可验证，无管理员后门
- 重复任务自动编译为可复放技能，需通过确定性回放考试
- 支持 36 个 LLM 提供方，含 Ollama/vLLM/llama.cpp 等本地后端

## 适用场景

- 在本地硬件上组建多智能体团队处理写作、研究、构建等分工任务
- 让 agent 从我的重复工作流中沉淀可复用技能
- 使用本地模型获得带验证与自我批评的可靠回答
- 通过 MCP 将 TITAN 作为工具接入其他 agent 系统

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L1: > **TITAN** — A local-first AI agent framework that runs on your hardware, with your models, under your control. v8 
> L12:  The local-first AI agent framework where your agents are a company — shared memory, real hiring, earned autonomy —
> L131: ### 🌐 Works alongside Hermes Agent & OpenClaw — the MCP triangle

## 星数曲线

```mermaid
xychart-beta
    title "Djtony707/TITAN 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `8d3e20b25d11` · [字段定义](../../DATASET.md)*
