# wontopos/glasshouse

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/wontopos/glasshouse) · 组织维护

**公开可复核的 AI 记忆基准结果发布处（规则+逐题记录）**

由 Wontopos 托管的 AI memory 基准结果发布库：制定 11 条规则（逐题记录公开、reader/judge/prompts 由版本固定、三次运行为结果五次为认证、提交须可复现等），收录公司公开声明数字的 claims register 与提交物 manifest schema。v0.1 基准为草稿未发布，submissions 目前为空，claims register 中的数字均非本库产出也未验证。全部内容以 Apache 2.0 提供，Wontopos 声明与参赛者存在利益冲突并写出限制条款。面向 memory 系统厂商与研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 11 条提交与认证规则（reader/judge/prompts 由版本固定）
- 逐题记录公开，任何人可重算聚合分数
- claims register 收录各公司已公开的声明数字并标注可验证性
- Wontopos 声明利益冲突限制：不自行合并提交、与他人同流程验证

## 适用场景

- 作为 memory 系统厂商提交可复现的基准结果
- 核对各家 AI memory 产品公开数字的 reader/judge 与运行次数
- 了解社区对可复现基准规则的设计讨论

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L16: 1. **Publish the per-question record.** Anyone can recompute the number from it. The
> L24: 5. **A submission carries its runs, its harness, and which version's reader, judge
> L72: `companies/` holds numbers that are already public. **None of them were produced

## 星数曲线

```mermaid
xychart-beta
    title "wontopos/glasshouse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bea4a75f8768` · [字段定义](../../DATASET.md)*
