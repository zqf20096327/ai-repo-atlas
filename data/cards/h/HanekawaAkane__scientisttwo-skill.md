# HanekawaAkane/scientisttwo-skill

⭐ 3 · Python · MIT · 推送 2026-11-05 · [GitHub](https://github.com/HanekawaAkane/scientisttwo-skill) · 个人维护 · 中文 README

**把论文方法做成 agent 可执行的科研流水线 skill**

将 ScientistTwo 论文中的自主科研流程抽象为一套 WorkBuddy 可执行的 agent 协议，包含十道以产物判定的闸门（G0–G7）与六种模式（ideate/screen/improve/ablate/review/audit），覆盖局限提取、种子想法、子集筛选、消融归因、模拟评审与完整性审计。README 声明非论文官方实现，要求有 GPU 执行环境才跑全量，无算力时降级为可执行队列，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六种模式：ideate/screen/improve/ablate/review/audit
- 十道闸门靠产物判定，含子集预筛与消融归因门槛
- 双评审器 held-out 校验与 3 seed 显著性门槛
- A/B/C/D 四档算力降级与 80% 预算熔断机制

## 适用场景

- 给 AI agent 装上带闸门的自主科研流水线
- 先低成本筛掉不可靠的研究想法再投入全量算力
- 对已有稿件做消融归因与完整性审计

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: 把「在某个 SOTA 上做出可归因的改进，并写成能过评审的稿子」这件事，拆成一条带闸门的流水线，做成可被 AI agent 直接执行的 skill。
> L40: SKILL.md                       # 路由 + 硬规则 + 预期管理

## 星数曲线

```mermaid
xychart-beta
    title "HanekawaAkane/scientisttwo-skill 星数(近 2 点)"
    x-axis ["2026-11-22", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-22 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `011a7daaadcb` · [字段定义](../../DATASET.md)*
