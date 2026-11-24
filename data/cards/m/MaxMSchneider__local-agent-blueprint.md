# MaxMSchneider/local-agent-blueprint

⭐ 3 · MIT · 推送 2026-11-02 · [GitHub](https://github.com/MaxMSchneider/local-agent-blueprint) · 个人维护

**本地小模型个人助理的设计蓝图：系统而非模型审批动作**

非框架、非库的规格文档集：由设计决策、接口规范、伪代码与验收检查组成，指导个人或编码 Agent 在任意 harness 上重建本地个人助理。核心机制是把可靠性从模型移入系统：动作经审批协议与门控批准，重复任务按聊天→技能→脚本两级硬化阶梯逐步确定化；以控制论与反馈回路组织各子系统（记忆、调度、安全、预算、急停）。目标硬件为本地服务的小参数量 MoE 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两级硬化阶梯：重复任务从聊天固化为技能、再固化为脚本
- 动作协议：台账、分级、门控与审批令牌，由系统而非提示词强制执行
- 以控制论概念组织的 19 篇核心文档，含验收检查套件
- 提供针对已有助理的只读差距分析文档

## 适用场景

- 在本地小模型上构建数据不出机器的个人助理
- 为已有的本地助理做差距分析与改造规划
- 让编码 Agent 按规格和验收门逐步搭建助理系统

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L6: **A blueprint for personal agents in which the system, not the model, approves actions, and in which recurring work 
> L8: This repository is not a framework and not a library. It is a set of design decisions, interface specifications, pse
> L29: The blueprint aims at **agentic, local operation of small models**:

## 星数曲线

```mermaid
xychart-beta
    title "MaxMSchneider/local-agent-blueprint 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-02 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c520b971479b` · [字段定义](../../DATASET.md)*
