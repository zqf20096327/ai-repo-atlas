# nagarjuna-tella/Aksara

⭐ 18 · Python · MIT · 推送 2026-09-13 · [GitHub](https://github.com/nagarjuna-tella/Aksara) · 个人维护

**PostgreSQL 后端框架：同一模型生成 REST API 与 MCP 工具**

Python 异步应用框架，基于 FastAPI，从同一模型与策略边界生成 REST API 与经授权的 MCP 工具；提供异步 ORM/迁移、权限/租户/字段级管控、审批边界与审计事件，以及可选的持久化 Operations（重试、幂等、执行前重新授权）。面向构建多租户应用的后端工程师。自述 pre-1.0：规划器、自主工作流、Studio 等仍属实验性；需自行运维 Python 服务与 PostgreSQL，应用方负责凭证验证与业务策略。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 同一模型与策略边界生成 REST API 与 MCP Streamable HTTP 工具
- Principal/PolicyEngine 权限、租户与字段级管控同时覆盖 REST 与 MCP
- 可选持久化 Operations：等待/重试的任务执行前重新校验授权
- aksara doctor 提供 launch-check/security-check/production-check 诊断

## 适用场景

- 构建多租户的工单/内部运营/SaaS 后端 API
- 让 agent 通过 MCP 以受权限管控的方式访问后端操作
- 实现需等待或重试且执行时重新授权的业务动作

## 场景标签

 · 领域:后端框架/LLM 基础设施

## 证据(README 行号)

> L5:  An async PostgreSQL backend framework that generates REST APIs and authorized MCP tools from the same model and pol
> L14: Aksara is a PostgreSQL-backed Python application framework with generated APIs,
> L18: It is for backend engineers building tenant-aware applications such as support

## 星数曲线

```mermaid
xychart-beta
    title "nagarjuna-tella/Aksara 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b4fadfcbbc39` · [字段定义](../../DATASET.md)*
