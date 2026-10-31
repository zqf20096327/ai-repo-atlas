# phd-benel/PowerLine-MTYOLO

⭐ 17 · 推送 2026-10-09 · [GitHub](https://github.com/phd-benel/PowerLine-MTYOLO) · [官网](https://www.mdpi.com/2504-446X/9/7/505) · 组织维护

**多任务 YOLO 模型：无人机影像中同时分割电缆与检测断股**

论文配套代码仓库，发表于 MDPI Drones。基于 A-YOLOM 架构与 YOLOv8，提出单阶段轻量多任务模型 PowerLine-MTYOLO，从无人机影像中同时完成电力电缆分割与断股检测，引入 SDPM、HAD、EFR 与 Shape-Aware WiseIoU 损失四个模块。同时发布合并公开电力电缆数据集 MPCD（聚合 5 个 Roboflow 公开数据集，1,871 张图像、2,501 个电缆分割掩码、1,906 个断股标注），提供预训练权重、Google Colab 推理/训练流程与演示视频。代码与数据集通过 Google Drive 链接分发，采用 AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单阶段多任务：同时输出电缆分割掩码与断股检测框
- 引入 SDPM、HAD、EFR、Shape-Aware WiseIoU 四个专用模块
- 发布 MPCD 数据集：1,871 张图、2,501 个分割掩码、1,906 个断股标注
- 提供预训练权重与 Google Colab 推理/训练复现流程

## 适用场景

- 无人机电力线路巡检中自动定位断股缺陷
- 在公开电缆数据集上复现或开展多任务分割/检测研究
- 作为电力基础设施细粒度结构监测的模型基础

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L12: To address these limitations, we propose PowerLine-MTYOLO, a lightweight, one-stage multitask model designed for si
> L53: Benelmostafa, B.-E.; Medromi, H. PowerLine-MTYOLO: A Multitask YOLO Model for Simultaneous Cable Segmentation and B

## 星数曲线

```mermaid
xychart-beta
    title "phd-benel/PowerLine-MTYOLO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `46ea0440e4c9` · [字段定义](../../DATASET.md)*
