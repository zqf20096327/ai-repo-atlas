# Accenture/AmpliGraph

⭐ 2,242 · Python · Apache-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/Accenture/AmpliGraph) · 组织维护

**面向开发者的知识图谱表示学习与链接预测 Python 库**

Accenture 维护的开源 Python 库，基于 TensorFlow 2，用于知识图谱上的关系学习：生成图中概念的向量嵌入（TransE、DistMult、ComplEx、HolE、RotatE 等模型），结合打分函数预测未见链接，支持补全缺失三元组、发现新事实、实体聚类与近重复预测，并提供评测协议与指标。面向需要开发、评估关系学习模型或完成知识图谱的研究者与开发者。提供 Keras 风格 API，可在 CPU 与 GPU 上训练；需 Python 3.9–3.11，经 pip 安装。2.0 版本更换了数据输入输出管线并停止支持部分旧模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 TransE/DistMult/ComplEx/HolE/RotatE 等知识图谱嵌入模型
- Discovery 高层 API：发现新事实、聚类实体、预测近重复
- 提供 MRR Filtered 等评测协议与指标，附多个基准数据集结果
- 基于 TensorFlow 2，可在 CPU 与 GPU 上运行训练

## 适用场景

- 补全大型知识图谱中缺失的三元组
- 生成独立的知识图谱嵌入向量用于下游任务
- 开发并评测新的关系学习模型
- 从已有知识图谱中发现新知识

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L11: **Open source library based on TensorFlow that predicts links between concepts in a knowledge graph.**
> L13: **AmpliGraph** is a suite of neural machine learning models for relational Learning, a branch of machine learning
> L25: It then combines embeddings with model-specific scoring functions to predict unseen and novel links:

## 星数曲线

```mermaid
xychart-beta
    title "Accenture/AmpliGraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 2241 --> 2243
    line [2242, 2242]
```

2026-10-18 2,242 → 2026-10-21 2,242（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2d0d12b611be` · [字段定义](../../DATASET.md)*
