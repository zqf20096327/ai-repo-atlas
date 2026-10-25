# georg-wolflein/pathology-foundation-models

⭐ 208 · Makefile · 推送 2026-02-15 · [GitHub](https://github.com/georg-wolflein/pathology-foundation-models) · 个人维护

**病理学基础模型与特征提取器清单（含 patch 级与切片级）**

由个人维护的病理学自监督特征提取器/基础模型策展清单，分两张表格收录约 40 个模型：patch 级模型（如 UNI、Virchow、H-optimus、GigaPath 等）与 slide/patient 级模型（如 PRISM、CHIEF、TITAN 等）。每个条目列出研发团队、权重可得性、发布时间、SSL 方法、训练 WSI/切片/患者规模、架构、参数量、嵌入维度、输入尺寸、有效放大倍数与数据集。作者随新模型发布持续更新，接受 PR/issue 补充。清单本身不提供代码或权重，仅作信息索引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两张表格分别收录 patch 级与 slide/patient 级模型
- 每条目含 SSL 方法、训练规模、架构、参数量、嵌入维度等字段
- 以 >100K 切片训练的模型加粗标注为 foundation model
- 区分语言-视觉预训练（VL）与纯视觉模型

## 适用场景

- 为病理图像分析任务选型合适的特征提取器
- 比较各模型的数据来源（TCGA/专有）与权重可得性
- 跟踪病理基础模型领域的发展时间线

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L3: We are witnessing the emergence of many new feature extractors trained using self-supervised learning on large patho
> L4: This repository aims to provide a comprehensive list of these models, alongside key information about them.

## 星数曲线

```mermaid
xychart-beta
    title "georg-wolflein/pathology-foundation-models 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 206 --> 209
    line [207, 208, 208]
```

2026-10-18 207 → 2026-10-25 208（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fda908a12f2f` · [字段定义](../../DATASET.md)*
