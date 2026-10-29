# google-deepmind/unlearning_evaluation

⭐ 20 · Python · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/google-deepmind/unlearning_evaluation) · 组织维护

**NeurIPS 2023 机器遗忘竞赛的评分代码：评估遗忘算法质量**

DeepMind 发布的竞赛评测代码，用于为 NeurIPS 2023 Machine Unlearning 竞赛提交打分。机制：运行指定遗忘算法与从头重训的 oracle 算法各 512 次（默认），基于遗忘样本上两类模型置信度计算遗忘质量分，再结合保留集/测试集准确率调整得出最终分数。需自备 CASIA-SURF 数据集（邮件申请授权获取），通过 xmanager 运行 launch.py。用户可将 do_unlearning 替换为自己的遗忘算法。竞赛已结束，代码用于复现评测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 遗忘算法与 oracle 重训各跑 _NUM_MODELS 次（默认 512）计算遗忘质量分
- 最终分数结合保留集与测试集准确率（utility）调整
- do_unlearning 函数可替换为用户自定义遗忘算法
- 重训 checkpoint 可保存复用以节省计算

## 适用场景

- 我在做机器遗忘研究，想复现竞赛的评测指标
- 我想用标准指标给自己的遗忘算法打分
- 我在参加或复盘 NeurIPS 2023 机器遗忘竞赛

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Evaluation code for the NeurIPS 2023 Machine Unlearning competition
> L42: The forgetting quality score is then computed from the confidences of each

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/unlearning_evaluation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d1bf2823a65a` · [字段定义](../../DATASET.md)*
