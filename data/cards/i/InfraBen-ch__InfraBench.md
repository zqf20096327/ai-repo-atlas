# InfraBen-ch/InfraBench

⭐ 31 · Shell · Apache-2.0 · 推送 2026-09-14 · [GitHub](https://github.com/InfraBen-ch/InfraBench) · [官网](https://infraben.ch/) · 组织维护

**基础设施智能体的评测基准：跨全栈层级的故障任务包**

面向基础设施运维 AI agent 的评测基准：以任务包（指令、环境、验证器）形式提供覆盖 L1 硬件到 L4 应用的真实故障场景，评估持久性、不变量、清理与风险等运维生命周期维度，而非仅二元通过/失败。仓库公开策展任务包（hello-world、IPMI 断电恢复、Cassandra 脑裂、Ceph 引导等），端到端评测运行时 Syscraft 暂未开源，当前任务包可作为布局与验证器参考。附 HotInfra '26 论文，Apache 2.0 许可，由威斯康星大学麦迪逊分校与爱荷华州立大学团队维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 任务包覆盖 L1 硬件→L4 应用全栈层级与运维生命周期
- 每个任务包含 task.toml、instruction、environment 与 verifier 测试
- 评估维度含持久性、不变量、清理与风险，非仅 pass/fail
- 配套 HotInfra '26 论文（arXiv:2608.11234）

## 适用场景

- 评测基础设施运维 agent 在真实故障场景下的表现
- 参考任务包布局与验证器编写自己的评测任务
- 了解 agent 在生产运维风险维度的能力边界

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L23: **InfraBench** evaluates AI agents on realistic infrastructure incidents across the full stack (L1 hardware → L4 ap
> L35: This is the **public** InfraBench surface: curated task packages (instruction, environment, verifier). The evaluati
> L63: End-to-end runs use **Syscraft** (provisioning, fault scenarios, agent adapters).

## 星数曲线

```mermaid
xychart-beta
    title "InfraBen-ch/InfraBench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-31 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `6e6c53c180a2` · [字段定义](../../DATASET.md)*
