# Unfold-Security/pydantic-collab

⭐ 33 · Python · MIT · 推送 2026-08-11 · [GitHub](https://github.com/Unfold-Security/pydantic-collab) · 组织维护

**基于 Pydantic AI 的多智能体编排框架**

供开发者用声明式代码构建多智能体协作的 Python 框架：提供 Pipeline、Star、Mesh 及自定义拓扑结构，支持 agent 间工具调用与控制权移交两种交互模式，内置拓扑校验、运行间共享记忆、执行追踪与拓扑图可视化，可配置上下文传递与移交上限。基于 Pydantic AI 构建，支持 Logfire 可观测性。通过 pip 安装，附示例工程。

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

- 预置 Pipeline/Star/Mesh 拓扑与自定义图结构
- 工具调用（保持控制）与移交（转移控制）两种交互模式
- 跨 agent 共享记忆与可配置上下文传递
- 拓扑可视化与移交/递归深度限制

## 适用场景

- 编排分阶段工作流（分诊→调查→响应）
- 组建协调者加领域专家的多 agent 团队
- 实现起草者与评审者的迭代精炼循环

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Build AI agent teams that collaborate intelligently — with handoffs, consultations, and shared memory.**
> L17: - 🐍 **Pydantic-AI Native** — Use Pydantic-AI and Logfire observability

## 星数曲线

```mermaid
xychart-beta
    title "Unfold-Security/pydantic-collab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ef687ee494fa` · [字段定义](../../DATASET.md)*
