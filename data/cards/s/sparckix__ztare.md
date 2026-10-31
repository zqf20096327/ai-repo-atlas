# sparckix/ztare

⭐ 20 · Python · MIT · 推送 2026-08-29 · [GitHub](https://github.com/sparckix/ztare) · 个人维护

**本地优先的主张审计引擎：核验文档声明是否有证据支撑**

面向需要对高风险论断负责的项目方与研究者的本地优先引擎：输入项目文件夹、报告、PRD、模型输出或数据集，将其中声明与项目证据比对，标记为 backed/contradicted/untested，并产出决策简报。关键机制包括：提议者不给自己评分（生成、对抗审查、评分、确定性门分离）、证据绑定与来源链接、通过来源防火墙生成受治理工件（决策备忘录/ADR 等）、Lean 4 受治理证明搜索。以 Python 包安装，可选 extras 分能力安装；Lean 4/Mathlib 为需经 elan 自装的外部工具；Project Workbench 为本地 Web 应用，支持 Docker Compose 单容器路径，尚无多用户认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 声明级证据比对：backed/contradicted/untested 标记与决策简报
- 提议者不给自己评分：生成/审查/评分/确定性门分离
- 来源防火墙：受治理工件中每个元素须逐字溯源到硬化声明
- Scenario + 能力插件以 YAML/.py 即插即用地绑定用例

## 适用场景

- 审计 PRD/报告/模型输出中的声明是否有本地证据支撑
- 把 AI 润色后的交付物经再摄取门核验，防止夹带无支撑声明
- 以决策简报明确某个决策依赖哪些未决声明与反事实敏感性
- 对 Lean 4 形式化与证明搜索做受治理管理

## 场景标签

 · 领域:AI 治理/主张验证

## 证据(README 行号)

> L20: Bring a project folder, report, PRD, model output, proof note, dataset, or repo. Paste a document and ZTARE
> L21: compares its claims with the project's evidence. It marks claims as backed, contradicted, or untested and
> L68: AI can produce a plausible answer without leaving a usable audit trail. The risk grows when one model both
> L69: produces the work and grades it. ZTARE separates drafting, evidence binding, checking, report readiness, and

## 星数曲线

```mermaid
xychart-beta
    title "sparckix/ztare 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f401a107a98d` · [字段定义](../../DATASET.md)*
