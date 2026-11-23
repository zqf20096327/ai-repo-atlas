# GiacomoSaccaggi/Recycling-bin

⭐ 10 · HTML · 推送 2026-05-21 · [GitHub](https://github.com/GiacomoSaccaggi/Recycling-bin) · 个人维护

**用 ML/DL 自动垃圾分类的研究项目，含机器人与实体分类桶**

将垃圾分类作为统计分类问题的研究项目：通过网络抓取（129 类共 41,042 张图片）、Telegram 机器人收集照片（1,348 张）和带传感器的 Arduino 分类桶（重量、透明度、电导率等结构化数据）三种途径采集训练数据；训练 GBM、MLP、ResNet 及 Stacking 集成模型；落地为两个应用——接收照片返回预测类别的 Telegram 机器人和用训练模型自动分拣垃圾的实体桶。附项目网页、演示视频与意大利语论文 PDF。README 未给出安装与运行说明。

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

- 三种数据采集途径：Web 抓取 41,042 张图、Telegram 收图、Arduino 传感器记录结构化数据
- GBM、MLP、ResNet 与 Stacking 集成模型（README 报告 84%–96% 准确率）
- 应用一：Telegram 机器人接收照片返回预测的垃圾类别
- 应用二：基于训练模型自动分拣垃圾的实体桶

## 适用场景

- 拍照识别垃圾所属类别（通过 Telegram 机器人）
- 搭建带传感器、可自动分拣的智能垃圾桶
- 参考垃圾分类的多源数据采集与建模流程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: A research project that tackles waste sorting as a statistical classification problem, using Machine Learning and De
> L37: 1. **Telegram Bot** — Receives a photo and returns the predicted waste category
> L38: 2. **Automatic Recycling Bin** — A physical bin that sorts waste automatically using the trained models

## 星数曲线

```mermaid
xychart-beta
    title "GiacomoSaccaggi/Recycling-bin 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `7f257f6eb1e0` · [字段定义](../../DATASET.md)*
