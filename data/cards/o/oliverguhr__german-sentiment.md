# oliverguhr/german-sentiment

⭐ 69 · Python · MIT · 推送 2026-07-17 · [GitHub](https://github.com/oliverguhr/german-sentiment) · 个人维护

**德语情感分类模型与数据集（LREC 2020 论文）**

LREC 2020 论文《Training a Broad-Coverage German Sentiment Classification Model for Dialog Systems》的代码与数据仓库。组合 8 个数据集（约 535 万样本，含 holidaycheck 酒店评论、filmstarts 电影评论、SCARE 等，SCARE 因法律原因不直接提供）训练 FastText 与 BERT 情感分类模型，模型可下载（6 GB），并给出各数据集上的 micro F1 结果。模型本身推荐通过另一仓库的 Python 包使用；本仓库侧重数据与训练复现，安装需 Python 3.6+ 并运行脚本下载模型与数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个德语数据集合计约 535 万样本（SCARE 需自行向作者获取）
- 提供 FastText 与 BERT 训练模型下载（6 GB）
- BERT 组合数据集 micro F1 0.9744（非平衡）
- 提供脚本一键下载模型与数据以复现结果

## 适用场景

- 复现论文中的德语情感分类训练与评测
- 获取德语酒店/电影评论等情感数据集做自己的实验
- 下载预训练 FastText/BERT 模型用于德语情感分析

## 场景标签

 · 领域:NLP/情感分析

## 证据(README 行号)

> L1: # Broad-Coverage German Sentiment Classification Model for Dialog Systems
> L3: This repository contains the code and data for the Paper "Training a Broad-Coverage German Sentiment Classification 

## 星数曲线

```mermaid
xychart-beta
    title "oliverguhr/german-sentiment 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-29 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `629112d2bfbc` · [字段定义](../../DATASET.md)*
