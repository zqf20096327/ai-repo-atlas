# shyammarjit/EEG-Emotion-Recognition

⭐ 70 · Jupyter Notebook · MIT · 推送 2026-05-29 · [GitHub](https://github.com/shyammarjit/EEG-Emotion-Recognition) · [官网](https://ieeexplore.ieee.org/document/9588702) · 组织维护

**基于 GA 优化 MLP 的 EEG 情绪识别研究代码（IRIA 2021 论文）**

论文配套代码：用功率谱密度特征量化 DEAP 数据集 EEG 信号，在 valence-arousal 维度上以多层感知机（MLP）分类情绪，并用遗传算法优化 MLP 架构。论文报告二分类（Low/High Valence 与 Low/High Arousal）平均准确率约 91%，四分类情绪约 83.5%；代码新版本因预处理改进报告了更高指标（10 折交叉验证下 valence 96.64%）。面向科研复现者，需自行获取 DEAP 数据集并配置 dataset_path、遗传代数、种群规模等参数。README 未给出依赖安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 功率谱密度特征 + MLP 分类 valence-arousal 情绪
- 遗传算法优化 MLP 架构（代数/种群/交叉与变异概率可配）
- 支持二分类（Valence/Arousal）与四分类（HVLA/HVHA/LVLA/LVHA）情绪识别
- 提供论文与结果表格引用

## 适用场景

- 复现 IRIA 2021 论文的 EEG 情绪识别实验
- 在 DEAP 数据集上做基于 GA-MLP 的情绪分类研究
- 对比情绪识别方法的基线结果

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L1: # EEG-Based Emotion Recognition Using Genetic Algorithm Optimized Multi-Layer Perceptron (IRIA 2021)
> L12: > ***Abstract:*** Emotion Recognition is an important problemwithin Affective Computing and Human Computer Interact
> L18: dataset_path  <- Path for the DEAP dataset

## 星数曲线

```mermaid
xychart-beta
    title "shyammarjit/EEG-Emotion-Recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-28 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9ae507160226` · [字段定义](../../DATASET.md)*
