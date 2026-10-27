# JamesPiggott/Ancient-Language-Decipherer

⭐ 27 · Python · 推送 2025-11-30 · [GitHub](https://github.com/JamesPiggott/Ancient-Language-Decipherer) · 个人维护

**深度学习识别古埃及圣书体等古文字的研究项目**

研究型仓库，用 Python 3 与 TensorFlow/Keras 构建卷积神经网络，对古埃及圣书体做字符特征提取、分割与分类，远期目标扩展到苏美尔楔形文字、玛雅文字及转写与翻译。当前已实现特征提取脚本与基础 CNN 分类训练，数据集整理、模型改进与重构仍在进行。README 引述 Franken(2013) 等学术基线，列出多个公开数据集来源，声明为实验性、非商业项目，2025 年 11 月宣布恢复开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- image_processing.py 特征提取与 train_model.py CNN 训练脚本
- 以 TensorFlow/Keras CNN 为核心，规划分割、转写与翻译流水线
- 汇总 Fayrose、Gimbert、JSesh 等公开圣书体数据集来源
- 规划离线优先设计与公开数据集构建/标注工具

## 适用场景

- 训练识别古埃及圣书体字符的 CNN 分类模型
- 调研古文字识别的公开数据集与前期研究
- 作为古文字分割与识别研究的基础代码库参与贡献

## 场景标签

`OCR` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: This repository explores the application of **Deep Learning (Computer Vision + NLP)** to detect, recognize and ulti
> L24: - TensorFlow / Keras
> L90: - ✅ Basic CNN classification

## 星数曲线

```mermaid
xychart-beta
    title "JamesPiggott/Ancient-Language-Decipherer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c09828c1b1e4` · [字段定义](../../DATASET.md)*
