# lekhashree21/CrimeTrace-AI-SIH

⭐ 10 · C++ · 推送 2026-09-10 · [GitHub](https://github.com/lekhashree21/CrimeTrace-AI-SIH) · 个人维护

**面向警方预测网络犯罪取现地点的 ML 系统**

机器学习驱动的网络犯罪取现地点预测系统，为执法部门提供实时预测。后端用 Python/Scikit-learn 训练 Random Forest 模型，以 Flask REST API 提供预测服务，通过 Flutter 移动应用向警方发送即时告警。包含数据预处理管道与模型训练脚本，自述预测准确率 90% 以上，为 SIH 2024 项目，由个人开发者维护。

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

- Random Forest 模型预测网络犯罪取现地点
- Flask REST API 后端与 Flutter 移动端告警
- 包含数据预处理管道与模型训练脚本
- 自述准确率 90%+，附性能指标表

## 适用场景

- 警方实时预测网络犯罪现金提取地点
- 通过移动端接收预测告警
- 复用其预处理与训练流程处理类似交易数据

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: CrimeTrace AI is a machine learning-powered system designed to assist law enforcement in predicting cybercrime cash 
> L22: |ML Model|Python, Random Forest, Scikit-learn|
> L23: |Backend API|Flask, REST API|

## 星数曲线

```mermaid
xychart-beta
    title "lekhashree21/CrimeTrace-AI-SIH 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `6c2bb7b3559c` · [字段定义](../../DATASET.md)*
