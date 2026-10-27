# future-agi/agent-command-center-sdk

⭐ 30 · Python · Apache-2.0 · 推送 2026-05-12 · [GitHub](https://github.com/future-agi/agent-command-center-sdk) · 组织维护

**Agent Command Center 网关的 Python/TypeScript 客户端 SDK**

为 Future AGI 开源的 OpenAI 兼容 AI 网关（Agent Command Center，Go 服务，负责路由/缓存/护栏/成本追踪）提供类型化的 Python 与 TypeScript 客户端，并附带 LangChain、LlamaIndex、React、Vercel AI SDK 四个框架集成包。调用面与 OpenAI SDK 同构，替换类名与 base_url 即可迁移；网关侧的 100+ 供应商接入、15 种路由策略、语义缓存、护栏与按 key 预算通过同一调用透出。需 Python 3.9+/Node 18+ 并连接云端或自托管网关端点方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容调用面（chat/embeddings/images/audio/batches/rerank 等）
- 透出网关能力：15 种路由策略、语义缓存、内联护栏、按 key 预算
- LangChain/LlamaIndex/React/Vercel AI SDK 集成包，按原框架方式使用
- 支持 100+ 供应商经统一端点接入（含 Ollama、vLLM）

## 适用场景

- 在代码中将多个 LLM 供应商统一到一个 OpenAI 兼容端点后调用
- 为 LangChain.js / LlamaIndex.TS / React 聊天界面接入网关
- 按请求配置回退链、成本优化路由与护栏策略

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Python and TypeScript SDKs — plus LangChain, LlamaIndex, React, and Vercel AI SDK integrations — for Agent Command
> L28: This repo ships the **client SDKs** for the Agent Command Center. The gateway itself — the Go service that handles 

## 星数曲线

```mermaid
xychart-beta
    title "future-agi/agent-command-center-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `86926b8d0629` · [字段定义](../../DATASET.md)*
