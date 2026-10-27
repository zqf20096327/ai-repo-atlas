# ZENGJingqi/GraphAI-for-TCM

⭐ 43 · Jupyter Notebook · MIT · 推送 2026-04-27 · [GitHub](https://github.com/ZENGJingqi/GraphAI-for-TCM) · [官网](https://doi.org/10.5281/zenodo.13763953) · 个人维护 · 中文 README

**用可解释图神经网络量化中药配伍机制的科研代码库**

由 Zeng Jingqi 维护的研究代码库，兼具双重角色：一是开放研究代码，提供中药饮片-药性语义图构建、预训练图注意力网络（GAT）推理与注意力解释的 Jupyter notebook 流水线；二是在线平台 TCMXAI 的后端模型，用户可在浏览器中浏览 TCM-MKG 知识库、检索数据并运行预训练模型，输出五维机制预测分与配伍关系表/注意力热图。训练集含 6,080 个标注图样本（每节点 91 维特征），另支持超图与 Graph Transformer 等实验设置。输出仅用于研究解释与假设生成，不构成临床诊断或用药建议。

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

- 预训练 GAT 模型对复方输出五维机制预测分
- 注意力权重输出配伍关系表、热力图与配伍图
- 本地 notebook 流水线：图构建→预测→定量解释
- 附带 6,080 个标注图样本与超图训练资产

## 适用场景

- 对中药复方做配伍机制的定量预测与解释
- 复现或扩展论文中的图/超图学习实验
- 在线浏览与检索 TCM-MKG 知识库数据

## 场景标签

`知识图谱` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L36: - **Predict formula-level mechanisms directly in the browser**
> L56: The deployed GraphAI-for-TCM model represents a formula as a **Chinese-herbal-piece plus medicinal-property semanti
> L64: Zeng, J., & Jia, X. (2025). *Quantifying compatibility mechanisms in traditional Chinese medicine with interpretabl

## 星数曲线

```mermaid
xychart-beta
    title "ZENGJingqi/GraphAI-for-TCM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5b1dcf34dade` · [字段定义](../../DATASET.md)*
