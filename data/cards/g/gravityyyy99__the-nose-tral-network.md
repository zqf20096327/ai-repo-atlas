# gravityyyy99/the-nose-tral-network

⭐ 3 · Python · MIT · 推送 2026-11-10 · [GitHub](https://github.com/gravityyyy99/the-nose-tral-network) · 个人维护

**气味预测与模拟电子鼻的教学演示应用**

以 Streamlit 构建的单页应用：用户选择或输入 138 个气味词之一，应用展示对应分子结构、8 路模拟气体传感器的反应条形图，以及两个随机森林模型的气味词预测（一个基于 RDKit Morgan 分子指纹，一个仅读取传感器数值）。作者声明电子鼻完全由代码模拟，无硬件；模型基于 OpenPOM 数据集约 5,000 个已标注分子训练，准确率由 evaluate.py 在留出集上测得并写入 evaluation.json。计划接入 BME688+ESP32 真实传感器并重新训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 气味模型：RDKit Morgan 指纹 + 100 棵树的随机森林，预测 138 个气味词
- 鼻子模型：从 8 路模拟传感器数值回归气味词分布
- 模拟传感器加入噪声、湿度与漂移，模拟真实硬件
- evaluate.py 在留出数据上实测准确率并逐项标注真实/模拟成分

## 适用场景

- 输入一个气味词，查看其分子构成与传感器反应模式
- 学习从分子指纹到传感器阵列的气味机器学习完整链路
- 作为后续接入真实气体传感器的基础代码框架

## 场景标签

 · 领域:化学信息学/气味机器学习

## 证据(README 行号)

> L13: You pick or type a smell (Vanilla, Smoky, Woody, Citrus, or any of 138 smell words), and the app shows you what
> L161: - **Smell model.** Each molecule becomes a "fingerprint": a count of its chemical fragments (a Morgan fingerprint 
> L205: |Smell model (random forest trained on the OpenPOM dataset)|**Real model**, really trained and tested on held-out 

## 星数曲线

```mermaid
xychart-beta
    title "gravityyyy99/the-nose-tral-network 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-10 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `5604f603563d` · [字段定义](../../DATASET.md)*
