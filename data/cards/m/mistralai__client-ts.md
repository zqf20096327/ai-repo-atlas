# mistralai/client-ts

⭐ 157 · TypeScript · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/mistralai/client-ts) · 组织维护

**Mistral AI 平台的 TypeScript 客户端 SDK（v2）**

Mistral AI 官方 TypeScript SDK v2，供开发者在 JS 应用中调用 Mistral 平台的 Chat Completion、Embeddings、Agents、语音转写/合成、Batch、RAG 托管索引与可观测性（数据集/评测/日志/追踪）等 API。仅发布 ESM 包，支持 npm/pnpm/bun/yarn 安装；通过 MISTRAL_API_KEY 或服务账号 token 文件认证，token 每次请求重读以支持轮换。另为 GCP 与 Azure 提供专用 SDK；部分 API 方法标记为已弃用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Chat/Embeddings/Agents/Audio/Batch/RAG 托管索引与可观测性 API
- 支持 MISTRAL_API_KEY 与服务账号 token 文件双认证路径，token 自动轮换生效
- v2 为 ESM-only，类型更短、枚举/联合类型向前兼容（Zod v4）

## 适用场景

- 在 Node/浏览器应用中集成 Mistral 模型的对话与向量能力
- 管理 Mistral 平台的 RAG 托管索引与文档摄取
- 接入平台可观测性：评测流水线、日志与追踪查询

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L12: Mistral AI API: Our Chat Completion and Embeddings APIs specification. Create your account on La Plateforme to get 
> L131: ## Available Resources and Operations

## 星数曲线

```mermaid
xychart-beta
    title "mistralai/client-ts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 156 --> 158
    line [157, 157]
```

2026-10-18 157 → 2026-10-24 157（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ba23eeb1c7b1` · [字段定义](../../DATASET.md)*
