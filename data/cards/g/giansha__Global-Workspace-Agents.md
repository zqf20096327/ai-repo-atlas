# giansha/Global-Workspace-Agents

⭐ 19 · Python · MIT · 推送 2026-04-23 · [GitHub](https://github.com/giansha/Global-Workspace-Agents) · [官网](https://giansha.github.io/Global-Workspace-Agents/) · 个人维护

**基于全局工作空间理论的多智能体 LLM 主动思考架构**

受认知科学全局工作空间理论（GWT）启发的多智能体 LLM 架构，将协调方式从被动共享记忆改为事件驱动的离散动力学系统。核心机制包括：4 阶段认知循环（感知→思考→仲裁→更新）、基于语义簇香农熵的内在驱动动态调节生成温度、每 tick 注入不变身份防止语义漂移、STM 缓存 + LTM 向量库（RAG）的双层记忆与 token 阈值自动分层。面向研究自主推理与主动发起对话的开发者与研究者；README 主要展示一个无用户输入、纯 idle tick 运行的 WALL·E 自主思考会话日志，技术栈为 Python 与 Next.js。

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

- 4 阶段认知循环（Perceive→Think→Arbitrate→Update）的离散动力学协调
- Shannon 熵驱动内在动机，动态调节生成温度以打破推理停滞
- 双层记忆：STM 活动缓存 + LTM 向量库（RAG），按 token 阈值 θ 自动分层
- Core Self 身份注入机制防止长程语义漂移

## 适用场景

- 研究 LLM 在无用户输入下的自主持续推理
- 构建能主动发起对话的多智能体系统
- 实验认知科学理论（全局工作空间）在 LLM 上的实现

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: > **GWA** transitions multi-agent LLM coordination from passive shared memory to an **active, event-driven discrete
> L23: - **The Cognitive Tick** — a 4-phase discrete loop: *Perceive → Think → Arbitrate → Update*

## 星数曲线

```mermaid
xychart-beta
    title "giansha/Global-Workspace-Agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 low · 依据 README sha `fc60acdef11a` · [字段定义](../../DATASET.md)*
