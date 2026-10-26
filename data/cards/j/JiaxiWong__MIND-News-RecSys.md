# JiaxiWong/MIND-News-RecSys

⭐ 38 · Jupyter Notebook · 推送 2025-12-02 · [GitHub](https://github.com/JiaxiWong/MIND-News-RecSys) · 个人维护

**DIN 新闻推荐模型：BERT 语义热启动解决冷启动**

在 Microsoft MIND 新闻数据集上实现 Deep Interest Network（DIN）的 PyTorch 项目：用 all-MiniLM-L6-v2（BERT）编码新闻标题并经 PCA 压缩到 32 维作为语义初始化，缓解物品冷启动；注意力机制在 ID 与类别序列上建模用户兴趣；采用两阶段训练（先冻结 BERT 只训 MLP，再全局微调）。README 报告 MIND-Large 验证集上 Global AUC 0.7133、MRR 0.3818。安装需 pip 依赖并自行下载数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DIN 注意力机制对候选新闻与历史行为计算相关性
- BERT(all-MiniLM-L6-v2) 语义向量 + PCA 32 维的冷启动处理
- 两阶段训练：冻结热启动后全局微调做领域适配
- 融合新闻 ID、类别、子类别的分层多粒度特征

## 适用场景

- 在 MIND 数据集上复现/研究新闻推荐与冷启动策略
- 学习 DIN 注意力建模与 BERT 语义初始化的训练流程
- 以轻量单模型方式做 CTR 预测实验

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L7: This project implements a Deep Interest Network (DIN) for news recommendation on the Microsoft News Dataset(MIND, A 
> L8: It features a Semantic Warm-up strategy using BERT embeddings to solve the item cold-start problem.

## 星数曲线

```mermaid
xychart-beta
    title "JiaxiWong/MIND-News-RecSys 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0e6d2a0533bf` · [字段定义](../../DATASET.md)*
