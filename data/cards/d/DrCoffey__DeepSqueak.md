# DrCoffey/DeepSqueak

⭐ 435 · MATLAB · BSD-3-Clause · 推送 2026-04-08 · [GitHub](https://github.com/DrCoffey/DeepSqueak) · 组织维护

**检测啮齿动物超声发声（USV）的 MATLAB 深度学习工具**

面向生物声学研究的 MATLAB GUI 软件：将音频转为声谱图后，用基于 YOLO V2 的目标检测网络在谱图上定位小鼠/大鼠的超声发声，并做轮廓不变聚类（变分自编码器）。支持浏览整段音频以修正或新增检测框，可用自有录音重训网络，或手工标注训练新物种检测器。由研究者团队（Coffey 等，2021 版权）维护，可在 MATLAB File Exchange 获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YOLO V2 架构的声谱图发声检测
- 可用自有录音重训网络或从零训练新物种检测器
- 变分自编码器实现轮廓不变聚类，附聚类 GUI
- 整段音频导航以精修检测框

## 适用场景

- 自动化检测小鼠/大鼠超声发声实验数据
- 用自有录音微调检测网络
- 对检测到的发声做聚类分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: ﻿# DeepSqueak v3: Using Machine Vision to Accelerate Bioacoustics Research
> L18: - Brand New YOLO V2 based Detection Architechture

## 星数曲线

```mermaid
xychart-beta
    title "DrCoffey/DeepSqueak 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 433 --> 435
    line [434, 434]
```

2026-10-18 434 → 2026-10-22 434（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `00dec5d1d523` · [字段定义](../../DATASET.md)*
