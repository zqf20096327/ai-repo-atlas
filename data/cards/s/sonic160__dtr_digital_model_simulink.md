# sonic160/dtr_digital_model_simulink

⭐ 24 · MATLAB · MIT · 推送 2025-12-02 · [GitHub](https://github.com/sonic160/dtr_digital_model_simulink) · 组织维护

**Simulink 机器人数字模型：仿真生成故障数据训练 AI 故障诊断模型**

为 Hiwonder Armpi_FPV 六自由度机械臂构建 Simulink 数字模型，模拟末端执行器在四电机控制指令下的三维运动轨迹。提供脚本与教程：在数字模型上注入故障生成仿真数据，训练故障诊断 AI 模型，并可在连接数字孪生的真实机器人上采集数据测试模型性能。仓库属于机器人预测性维护数字孪生开源计划的一部分。运行需 MATLAB/Simulink R2023b 或更高版本，含运动学建模教程与多份 MATLAB 实时脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Armpi_FPV 机械臂的 Simulink 数字模型（含控制结构与运动学版本）
- 故障注入生成仿真训练数据的脚本与教程
- 支持仿真数据训练、真实机器人数据测试的迁移流程
- 附 URDF 多体树建模与正/逆运动学教程

## 适用场景

- 在虚拟空间生成故障数据训练机器人故障诊断模型
- 构建机械臂数字孪生并做预测性维护研究
- 复现数字孪生支持故障诊断的论文方法

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L18:  This repository presents a digital model of a robot, and use it to train an AI model for fault diagnosis. The perf
> L55: As a use case of this digital model, you will find a script and tutorial on how to use this digital model to genera
> L72: - `scripts`: This folder contains scripts for running simulation on the digital model, and training and test the AI

## 星数曲线

```mermaid
xychart-beta
    title "sonic160/dtr_digital_model_simulink 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f0899ed45af1` · [字段定义](../../DATASET.md)*
