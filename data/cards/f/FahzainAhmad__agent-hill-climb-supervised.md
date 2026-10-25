# FahzainAhmad/agent-hill-climb-supervised

⭐ 69 · Python · 推送 2025-11-09 · [GitHub](https://github.com/FahzainAhmad/agent-hill-climb-supervised) · 个人维护

**视觉行为克隆 AI：CNN 观察游戏画面自动玩 Hill Climb Racing**

监督学习项目：从带动作标注的游戏帧（加速/刹车/无动作三类）训练 7 层 CNN（TensorFlow/Keras），实现行为克隆，模仿人类驾驶行为。数据采集脚本录制画面并记录键盘输入，预处理将帧缩放为 64×64 RGB 并遮蔽 UI 元素（油量条、金币、分数等）。推理时通过屏幕捕获实时读帧、预测动作并模拟按键，附显示预测动作/FPS/置信度的叠加层。提供 29,278 帧数据集与预训练模型（Kaggle），可用脚本直接运行预训练模型或从零训练。

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

- CNN 从原始画面帧预测三类驾驶动作（行为克隆）
- 29,278 帧带标注数据集与预训练模型托管于 Kaggle
- 预处理自动遮蔽油量条/金币/分数等非游戏元素
- 实时推理循环：截屏→预测→模拟按键→叠加显示

## 适用场景

- 让 AI 自动玩 Hill Climb Racing 的 Countryside 关卡
- 学习行为克隆/监督学习在游戏中的完整流程
- 复用数据集与模型做自己的驾驶预测实验

## 场景标签

`模型训练` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: This project implements a **supervised deep learning system** that learns to autonomously control a vehicle in the *
> L6: Using computer vision and a convolutional neural network (CNN), the model observes raw gameplay frames and predicts 

## 星数曲线

```mermaid
xychart-beta
    title "FahzainAhmad/agent-hill-climb-supervised 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-25 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `973ab2718694` · [字段定义](../../DATASET.md)*
