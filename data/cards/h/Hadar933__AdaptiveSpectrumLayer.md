# Hadar933/AdaptiveSpectrumLayer

⭐ 24 · Python · 推送 2025-12-16 · [GitHub](https://github.com/Hadar933/AdaptiveSpectrumLayer) · 个人维护

**扑翼机器人翼的深度逆向映射模型（ICLR 2025）PyTorch 官方实现**

ICLR 2025 论文 A Deep Inverse-Mapping Model for a Flapping Robotic Wing 的官方 PyTorch 实现：提出 Adaptive Spectrum Layer（ASL）架构，从翅膀运动学（pitch/yaw/roll 角度时间序列）逆向映射到力传感器测量。支持自建扑翼系统数据（153 组实验，5000Hz）与开源数据集（548 组实验，25Hz），数据已内置于仓库 ML/Data 目录。附带数据处理、相机标定/轨迹追踪、基准模型（NLinear、FEDformer 等）与可视化脚本；通过 git clone 加 requirements.txt 安装，运行 main.py 训练并以 TensorBoard 记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Adaptive Spectrum Layer（ASL）逆向映射架构（力→运动学方向的模型）
- 内置 153 组自建扑翼数据与兼容的开源时序数据集
- 含相机标定、力传感器数据处理与基准模型（NLinear/FEDformer 等）目录
- TensorBoard 训练日志与模型保存支持

## 适用场景

- 复现 ICLR 2025 扑翼逆向映射论文实验
- 在自有时序运动学-力数据上训练 ASL 模型
- 与 NLinear/FEDformer 等基准模型做对比实验

## 场景标签

 · 领域:机器人学/深度学习科研

## 证据(README 行号)

> L1: # A Deep Inverse-Mapping Model For A Flapping Robotic Wing (ICLR 2025)
> L21:  Figure 2: Overview of the proposed ASL architecture for Inverse-Mapping
> L54:  Implements core machine learning functionality using PyTorch. This includes:

## 星数曲线

```mermaid
xychart-beta
    title "Hadar933/AdaptiveSpectrumLayer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `a7542a8587e0` · [字段定义](../../DATASET.md)*
