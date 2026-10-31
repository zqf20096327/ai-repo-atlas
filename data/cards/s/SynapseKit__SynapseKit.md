# SynapseKit/SynapseKit

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/SynapseKit/SynapseKit) · [官网](https://synapse-kit.com) · 组织维护

**面向生产环境的异步优先 Python LLM 应用框架**

最小化、async-first 的 Python LLM 应用框架，仅 2 个硬依赖（numpy 与 rank-bm25）。提供统一接口接入 46 个 LLM 提供商、32 个向量存储、83 个数据加载器与 56 个 agent 工具，覆盖 RAG 管道、ReAct/function calling agent、DAG 图工作流、结构化输出、成本跟踪与内置实时可观测面板（SynapseKit Live）。各集成为可选 extras，按 pip extras 安装。面向不依赖 SaaS、在生产环境交付 LLM 功能的 Python 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2 个硬依赖（numpy + rank-bm25），其余为可选 extras
- 46 个 LLM 提供商、32 个向量存储、83 个数据加载器统一接口
- 内置零依赖实时可观测面板 SynapseKit Live（env var 启用）
- 内置 DAG 图工作流、agent 联邦与成本-质量路由

## 适用场景

- 构建异步 RAG 管道与带工具调用的 agent 服务
- 在不重写代码的情况下切换 LLM 提供商或向量存储
- 在生产环境本地观测 LLM 调用成本与调用链，不依赖 SaaS

## 场景标签

`Agent 框架` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L15: **Build production LLM apps with 2 dependencies.**
> L20: SynapseKit is a minimal, async-first Python framework for LLM applications: 46 LLM providers, 32 vector stores, 83 
> L131: |**🧠 LLM Providers**|46 providers behind one `BaseLLM` interface, auto-detected from the model name. Swap without 

## 星数曲线

```mermaid
xychart-beta
    title "SynapseKit/SynapseKit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `1cec4eeb6156` · [字段定义](../../DATASET.md)*
