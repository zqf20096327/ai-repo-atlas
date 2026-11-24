# vectara/hallucination-leaderboard

⭐ 3,329 · Python · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/vectara/hallucination-leaderboard) · [官网](https://vectara.com) · 组织维护

**用 HHEM 模型评测各 LLM 摘要幻觉率的排行榜**

Vectara 维护的公开 LLM 排行榜，使用其 HHEM-2.3 幻觉评测模型计算各家 LLM 在短文档摘要任务中的幻觉率、事实一致率与回答率。评测方法：将约 7700 篇不公开的文章（50 词至 24K 词）喂给各 LLM 要求仅依据原文生成摘要，温度设为 0，再计算事实一致性。README 同时给出所用提示词、API 调用细节、往期版本链接及Hugging Face 交互式版本入口。限制：评测仅覆盖摘要任务，数据集不公开以防过拟合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 用 HHEM-2.3 计算幻觉率、事实一致率、回答率三项指标
- 评测集含 7700+ 篇多领域文章，不公开以防过拟合
- 提供 Hugging Face 交互式排行榜与往期版本链接

## 适用场景

- 选型时查看各 LLM 在摘要任务上的幻觉率数据
- 了解 RAG/Agent 场景下模型作为摘要器的事实一致性表现
- 追踪各版本排行榜随模型更新的变化

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Public LLM leaderboard computed using Vectara's Hallucination Evaluation Model, also known as HHEM. This evaluates h
> L132: This leaderboard uses HHEM-2.3, Vectara's commercial hallucination evaluation model, to compute the LLM rankings. 
> L135: The dataset used for this leaderboard is carefully curated as follows:

## 星数曲线

```mermaid
xychart-beta
    title "vectara/hallucination-leaderboard 星数(近 11 点)"
    x-axis ["2026-10-21", "2026-10-26", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-15", "2026-11-20", "2026-11-21", "2026-11-24"]
    y-axis "stars" 3321 --> 3331
    line [3322, 3323, 3322, 3323, 3322, 3326, 3327, 3329, 3330, 3329, 3329]
```

2026-10-21 3,322 → 2026-11-24 3,329（+7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `76f015346e69` · [字段定义](../../DATASET.md)*
