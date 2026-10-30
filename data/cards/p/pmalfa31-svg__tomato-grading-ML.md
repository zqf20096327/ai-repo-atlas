# pmalfa31-svg/tomato-grading-ML

⭐ 18 · C · MIT · 推送 2026-08-06 · [GitHub](https://github.com/pmalfa31-svg/tomato-grading-ML) · 个人维护

**光学分选线的番茄成熟度/尺寸分级 ML 流水线**

面向工业多光谱光学分选（RGB/NIR/HSI 线扫）的数据处理、模型训练与固件导出流水线：处理传送带上的水果光谱切片，按批次类型（standard/cherry，由上游显式配置）用两个专用 RandomForestClassifier 分别做 5 类/3 类成熟度分级，并触发气动剔除命令；含基于 transit_len 的批次一致性检查（阈值 12）。模型经 m2cgen 导出为零依赖原生 C 头文件，用于 ESP32/FreeRTOS 等资源受限微控制器，附 ESP32 硬件示例与 Wokwi 浏览器仿真。限制：多数类别未在不同采集条件下验证，CHERRY 批仅 23 个样本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双模型批次架构：批次类型为显式配置参数而非逐果推断
- RandomForest 经 m2cgen 导出为零外部依赖的原生 C 头文件
- transit_len 批次一致性检查（异常樱桃番茄混入检测）
- ESP32 实机验证示例与 Wokwi 浏览器仿真（延迟数据以实机为准）

## 适用场景

- 把分级模型集成到传送带光学分选线的嵌入式固件
- 从传感器线扫原始数据生成逐果特征向量并训练模型
- 无硬件时用 Wokwi 仿真浏览项目行为

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: This repository implements a data engineering, Machine Learning training, and firmware export pipeline for an indust
> L10: The software processes in real time the spectral profiles of fruit (standard and cherry tomatoes) as they transit a

## 星数曲线

```mermaid
xychart-beta
    title "pmalfa31-svg/tomato-grading-ML 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `f4da89101dcb` · [字段定义](../../DATASET.md)*
