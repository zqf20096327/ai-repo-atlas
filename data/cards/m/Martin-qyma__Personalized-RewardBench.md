# Martin-qyma/Personalized-RewardBench

⭐ 14 · Python · 推送 2026-04-09 · [GitHub](https://github.com/Martin-qyma/Personalized-RewardBench) · [官网](https://arxiv.org/abs/2604.07343) · 个人维护

**评测奖励模型个性化偏好能力的基准（COLM 2026 论文）**

COLM 2026 论文配套的基准代码库：基于用户专属评分准则构建 chosen/rejected 回应对，评测奖励模型刻画个体偏好的能力；数据含用户历史 profile，可用于推断偏好。提供 pointwise（判别式 RM 打分）与 pairwise（生成式 LLM 裁判、随机 A/B 换位）两种评测模式，数据从 HuggingFace 目录 QiyaoMa/Personalized-RewardBench 加载；另含 Best-of-N 推理扩展实验（k 最大 128）与基于 verl 的 PPO 训练流程。实验显示现有 RM 准确率上限 75.94%。面向奖励模型与对齐方向研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于用户专属 rubric 构建 chosen/rejected 对，rubric 与 narrative 严格排除在 RM 输入外防泄漏
- pointwise 判别式打分与 pairwise LLM 裁判（A/B 随机换位）两种评测模式
- BoN 推理扩展实验（k∈{1…128}）与 verl PPO 个性化训练全流程
- 基准表现与 BoN/PPO 下游性能的相关性实验

## 适用场景

- 评测我的奖励模型在个性化偏好上的准确率
- 研究 BoN/PPO 下游任务中奖励模型的个性化能力
- 基于用户历史 profile 训练生成个性化回复的策略模型

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L5: Pluralistic alignment has emerged as a critical frontier in the development of Large Language Models (LLMs), with re
> L31: Evaluate any reward model on the benchmark using **pointwise** or **pairwise** comparison. Both modes load directly

## 星数曲线

```mermaid
xychart-beta
    title "Martin-qyma/Personalized-RewardBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `96b150ffa4dc` · [字段定义](../../DATASET.md)*
