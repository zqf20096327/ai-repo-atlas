# GraflowAI/graflow

⭐ 41 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/GraflowAI/graflow) · [官网](https://graflow.ai) · 组织维护

**面向开发者的 Pythonic LLM agent 工作流编排框架**

Graflow 是一个 Python 编写的 agent 工作流编排框架，采用 define-by-run 模式：用普通 Python 函数定义任务，以 `>>`（串行）和 `|`（并行）两个运算符组合，运行时通过 `next_task`/`next_iteration` 动态改变图结构。支持检查点续跑、human-in-the-loop 审批、Redis 分布式 worker 池、Docker 容器内执行任务，可注入 LiteLLM/Pydantic AI/Google ADK 的 LLM agent，并提供 Langfuse 追踪集成。README 中与 LangGraph 做了代码与范式对比。Apache 2.0 许可。

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

- `>>` 与 `|` 运算符组合任务，无图构建 API
- define-by-run：运行时动态增删任务与循环
- Redis 后端分布式执行与检查点续跑
- 任务可在 Docker 容器内执行，支持自定义 TaskHandler（Kubernetes/Lambda/Ray 等）

## 适用场景

- 用纯 Python 编写 ETL 与多 agent LLM 流水线
- 需要中途人工审批的工作流
- 将同一工作流从本地扩展到分布式 worker 池

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Graflow is a Python-based agent orchestration framework with a **workflow-first, defined-by-run** approach focused o
> L69: |**LLM agents**|Plug in LiteLLM, Pydantic AI, or Google ADK agents and inject them into tasks|

## 星数曲线

```mermaid
xychart-beta
    title "GraflowAI/graflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2ec22455d05a` · [字段定义](../../DATASET.md)*
