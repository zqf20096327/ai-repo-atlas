# amrraedamr/opinionated-genai-starter

⭐ 6 · Python · MIT · 推送 2026-11-15 · [GitHub](https://github.com/amrraedamr/opinionated-genai-starter) · 个人维护

**FastAPI LLM 产品脚手架：单服务或拆分微服务皆可运行**

以 uv workspace 组织的 FastAPI 项目模板：共享 base 包提供 auth、LLM 抽象、工具调用、RAG、用量计费、存储等能力，四个参考服务展示拆分形态，脚本可生成新服务或将多个切片合并为单服务部署。服务边界由 CI 中运行的 lint 强制（禁止跨服务外键、禁止互相导入）。基础设施经 docker compose 提供本地编排，事件经 Redis Streams 传递，Compose 编排仅面向本地环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套代码可组合为单服务或拆分多个微服务
- boundary_lint 在 CI 中强制服务边界（禁跨服务外键）
- LLM 层直连 OpenAI/Anthropic/Gemini SDK，统一调用形态与错误层次
- RAG、用量按 Decimal 计价、PII 脱敏等可选能力按需开启

## 适用场景

- 从零搭建 LLM 聊天后端而不必预先决定服务拆分
- 需要多租户、限流、追踪等能力的企业 LLM 服务起步
- 学习单体到微服务的边界治理与事件驱动设计

## 场景标签

 · 领域:LLM 应用开发基础设施

## 证据(README 行号)

> L7: **A FastAPI foundation for LLM products that runs as one service or several,
> L168: - **LLM** — provider SDKs directly, not LangChain. `AbstractLLMService` gives
> L31:   base/          shared library: LLM, auth, stores, cache, vectors, RAG, broker

## 星数曲线

```mermaid
xychart-beta
    title "amrraedamr/opinionated-genai-starter 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-24"]
    y-axis "stars" 5 --> 7
    line [6, 6]
```

2026-11-19 6 → 2026-11-24 6（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `b0dca562886b` · [字段定义](../../DATASET.md)*
