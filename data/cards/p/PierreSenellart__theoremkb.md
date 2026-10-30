# PierreSenellart/theoremkb

⭐ 26 · Jupyter Notebook · MIT · 推送 2026-07-21 · [GitHub](https://github.com/PierreSenellart/theoremkb) · 组织维护

**从数学研究论文中抽取定理等语义信息的工具集**

由 ENS Valda 研究组（PSL/CNRS/Inria）维护的科研项目，目标是从数学类研究论文中抽取定理、证明等语义信息，构建数学结果知识库。提供三条技术路径的实验代码：基于样式信息、基于计算机视觉的 YOLO 目标检测、基于 Transformers/LSTM 的序列预测，主要以 Jupyter Notebook 形式交付。配套 4400 篇 arXiv 论文数据集的引用列表（因许可不重新分发原文）。项目声明为进行中，代码为初步版本。

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

- 三条抽取路径：样式信息、YOLO 目标检测、Transformers/LSTM 序列预测
- 以 Jupyter Notebook 形式提供预处理与训练流程
- 4400 篇 arXiv 论文数据集（提供链接列表，不重新分发）
- 配套多篇论文与学位论文组成的文献列表

## 适用场景

- 对数学论文做定理与证明的自动抽取实验
- 复现或比较不同抽取方法（样式/视觉/NLP）
- 构建数学结果知识库的研究基础

## 场景标签

`科研工具` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3: TheoremKB is a research project and a corresponding collection of tools
> L44: We are currently experimenting with the extraction of mathematical results
> L65: `/transformers_tkb.ipynb` contains application of several AutoEncoding Transformers all base models (SciBert, Bert,

## 星数曲线

```mermaid
xychart-beta
    title "PierreSenellart/theoremkb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9d4514faeda5` · [字段定义](../../DATASET.md)*
