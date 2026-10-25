# Davidlequnchen/VLM-CADFeatureRecognition

⭐ 83 · Jupyter Notebook · MIT · 推送 2026-01-31 · [GitHub](https://github.com/Davidlequnchen/VLM-CADFeatureRecognition) · 组织维护

**用视觉语言模型自动识别 CAD 制造特征的代码与数据集**

伴随 JCISE 2025 论文的官方代码库：用视觉语言模型（VLM）结合提示工程（多视图查询图像、少样本学习、顺序推理、思维链）在 CAD 设计中自动识别制造特征，不依赖大规模训练集或预定义几何规则。提供 MFCAD-VLM 数据集（STEP 文件、专家标注 JSON、每模型三张等轴测视图图像，按难度分级）。以源码加数据集形式提供，需 Python、PyTorch 与 pythonocc 环境运行论文所述实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VLM 提示工程（多视图、少样本、思维链）做制造特征识别
- MFCAD-VLM 数据集：STEP 文件、专家标注 JSON、三视角等轴测图像
- 按 easy/medium/hard 难度分级组织 CAD 模型

## 适用场景

- 复现论文中的 CAD 制造特征识别实验
- 获取 MFCAD-VLM 数据集用于 AFR 研究与评测
- 探索 VLM 在制造设计理解中的应用

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L4: This repository contains the code and resources accompanying the paper "Leveraging Vision-Language Models for Manufa
> L12: Automatic Feature Recognition (AFR) is crucial for converting design knowledge into actionable manufacturing inform

## 星数曲线

```mermaid
xychart-beta
    title "Davidlequnchen/VLM-CADFeatureRecognition 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 81 --> 84
    line [82, 83, 83]
```

2026-10-18 82 → 2026-10-25 83（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `8483084141e9` · [字段定义](../../DATASET.md)*
