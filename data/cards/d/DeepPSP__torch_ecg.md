# DeepPSP/torch_ecg

⭐ 273 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/DeepPSP/torch_ecg) · 个人维护

**基于 PyTorch 的心电图深度学习框架**

面向研究者和开发者的 ECG 深度学习 Python 库：提供 8 种数据增强器、4 种预处理器、覆盖 PhysioNet/CPSC 等 14 个 ECG 数据库的读取类与内置 Dataset、CRNN/U-Net/RR-LSTM 等模型架构，以及 VGG/ResNet 变体等 CNN backbone。模型输出分类、序列标注、波形勾画、R 波检测等结果，并配套日志、指标、BaseTrainer 训练管线抽象。文档仍在开发中，测试流程待完善，支持 pip 安装。

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

- CRNN、U-Net、RR-LSTM 等模型架构与多种 ResNet 变体 backbone
- 14 个 ECG 数据库读取类与内置 Dataset（PhysioNet/CPSC 等）
- 分类、R 波检测、波形勾画等任务的输出容器与内置指标
- BaseTrainer 抽象训练管线与 9 个基准赛题使用示例

## 适用场景

- 我在做 ECG 心律失常分类任务的模型训练与基准复现
- 我需要统一接口读取多个公开 ECG 数据库并构建 Dataset
- 我想快速实验不同的 CNN backbone 与数据增强组合

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L13: ECG Deep Learning Framework Implemented using PyTorch.
> L151: 1. CRNN, both for classification and sequence tagging (segmentation)

## 星数曲线

```mermaid
xychart-beta
    title "DeepPSP/torch_ecg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 272 --> 274
    line [273, 273]
```

2026-10-18 273 → 2026-10-22 273（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `bc001b5e9c03` · [字段定义](../../DATASET.md)*
