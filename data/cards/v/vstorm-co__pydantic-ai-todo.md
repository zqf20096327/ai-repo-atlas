# vstorm-co/pydantic-ai-todo

⭐ 76 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/vstorm-co/pydantic-ai-todo) · [官网](https://vstorm-co.github.io/pydantic-deepagents/) · 组织维护

**为 Pydantic AI agent 提供任务规划与跟踪的工具集**

面向 Pydantic AI 开发者的任务管理扩展库：通过 Capabilities API 一行代码接入 agent，注册 add/read/write/update/remove 等 todo 工具，可选启用子任务、依赖与循环检测；存储后端含内存、异步内存与 PostgreSQL（多租户），并提供 webhooks/回调事件系统。已与 Pydantic 团队合作并入官方 pydantic-ai-harness（PR #404），本包保留在 PyPI 但被取代，新项目建议使用 harness。由 Vstorm 公司维护并提供咨询服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Capabilities API 一行接入，自动注册 todo 工具与系统提示
- 子任务、依赖与循环检测支持
- 内存/异步内存/PostgreSQL 多租户存储后端
- TodoEventEmitter 事件系统支持回调

## 适用场景

- 给 Pydantic AI agent 添加任务规划与进度跟踪能力
- 多租户场景下持久化 agent 任务数据
- 通过事件回调响应任务状态变化

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L62: **Todo Toolset for Pydantic AI** adds task planning capabilities to any Pydantic AI agent. Your agent can create, t
> L243: |pydantic-ai|The foundation — agent framework by Pydantic|

## 星数曲线

```mermaid
xychart-beta
    title "vstorm-co/pydantic-ai-todo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-29 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fc0965bf3d1e` · [字段定义](../../DATASET.md)*
