# maxsitt/insect-detect-docs

⭐ 31 · CC-BY-SA-4.0 · 推送 2026-04-16 · [GitHub](https://github.com/maxsitt/insect-detect-docs) · [官网](https://maxsitt.github.io/insect-detect-docs/) · 组织维护

**DIY 昆虫监测相机陷阱的文档网站源码：搭建、训练与部署指南**

Insect Detect 项目的文档仓库：存放基于 Material for MkDocs 的文档网站 Markdown 源文件与图片资源，配套论文（PLOS ONE 2024）与 Zenodo DOI。文档覆盖低成本硬件组件（Raspberry Pi Zero 2 W、Luxonis OAK-1、Witty Pi）的组装步骤、软件配置、用自有图像训练 YOLOv5/6/7/8 检测模型与 YOLOv5-cls 分类模型、以及在设备端检测追踪、本地 PC 分类与元数据后处理的部署流程。注意：检测模型训练部分正在重构，v2.0.0 后不再支持旧方式训练的 YOLO 模型。本仓库本身为文档，可运行脚本位于 insect-detect 等其他仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖硬件组装、软件配置、模型训练到部署的全流程文档
- 面向 Raspberry Pi Zero 2 W + Luxonis OAK-1 的低成本 DIY 硬件方案
- 模型训练可在 Google Colab 免费云端 GPU 完成，分类训练无需本地 GPU
- 提供 PLOS ONE 论文引用与 CC BY-SA 4.0 许可

## 适用场景

- 科研或保护工作者按文档自行组装自动昆虫监测相机陷阱
- 用自有昆虫图像训练并部署 YOLO 检测/分类模型
- 了解设备端检测到本地分类的完整处理流程

## 场景标签

`目标检测` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: This repository contains the Markdown source files and assets (images, screenshots) of
> L8: the **Insect Detect Docs** 📑 website,
> L71: The **Deployment** section will give you details on each step of the processing pipeline,

## 星数曲线

```mermaid
xychart-beta
    title "maxsitt/insect-detect-docs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `40f41d7670b3` · [字段定义](../../DATASET.md)*
