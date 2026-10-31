# nusnlp/greco

⭐ 16 · Macaulay2 · GPL-3.0 · 推送 2026-01-24 · [GitHub](https://github.com/nusnlp/greco) · [官网](https://aclanthology.org/2023.emnlp-main.785) · 组织维护

**EMNLP 2023 论文官方代码：用质量估计对 GEC 纠错结果打分、重排与系统融合**

GRECO 是语法纠错（GEC）系统的组合框架：基于 DeBERTa-v3-large 训练的质量估计模型，对候选纠错句子打分，用于重排 top-k 模型输出，或通过投票系数将多个 GEC 系统的纠错结果融合为单一输出。提供 Python 类调用（.score()）、批量脚本与复现 BEA-2019/CoNLL-2014 结果的命令，支持用自定义数据重训模型。可选接入 neuqe、VERNet、SOME 等其他质量估计模型做相关性对比。代码与模型采用 GPLv3，并另行提供商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 质量估计模型对候选纠错句子打分
- 对 top-k GEC 模型输出进行重排
- 多系统纠错结果融合（投票系数可调）
- 支持用自定义数据重新训练模型

## 适用场景

- 我有多条 GEC 系统输出，想融合成一条更好的纠错结果
- 我想对自己的 top-k 纠错候选做重排
- 我想复现论文在 BEA-2019/CoNLL-2014 上的 F0.5 分数

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L2: This repository provides the code to easily score, re-rank, and combine corrections from Grammatical Error Correctio
> L30: You can import the GRECO class from `models.py`, instantiate the class, and pass the source(s) and hypotheses (in t
> L74: python run_combination.py --model greco --lm_model microsoft/deberta-v3-large --output_path outputs/bea-test.out --

## 星数曲线

```mermaid
xychart-beta
    title "nusnlp/greco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d15851f14f02` · [字段定义](../../DATASET.md)*
