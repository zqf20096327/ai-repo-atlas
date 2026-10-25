# citoverse/cito

⭐ 55 · HTML · GPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/citoverse/cito) · [官网](https://citoverse.github.io/cito/) · 组织维护

**R 语言的深度神经网络训练与解释框架**

面向 R 用户的开源 R 包，提供公式语法的深度神经网络（DNN）训练接口，基于 R 原生 torch 包实现，无需 Python 安装或 API。支持 CPU、GPU 与 macOS GPU 训练、交叉验证下的超参数自动调优（tune() 标记待调参数、未超基线损失的组提前中止）、收敛诊断，并提供变量重要性、部分依赖图、累积局部效应图等可解释 AI 指标；可选 bootstrap 生成置信区间与 p 值，支持自定义损失函数。通过 CRAN 或 GitHub 安装，GPL-3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 公式语法拟合 DNN，基于 R 原生 torch，无需 Python
- 交叉验证下的超参数自动调优与提前中止机制
- 多种可解释 AI 指标（变量重要性/部分依赖图/ALE/效应估计）
- bootstrap 置信区间与 p 值，支持自定义损失函数

## 适用场景

- 用熟悉的 R 公式语法训练深度神经网络
- 对训练好的 DNN 做可解释性分析与统计推断
- 在 CPU/GPU/macOS GPU 上训练并自动调参

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L12: The ‘cito’ package provides a user-friendly interface for training and
> L16: problems. DNNs can be trained on CPU, GPU and MacOS GPUs. In addition,
> L22: is computationally efficient because it is based on the deep learning

## 星数曲线

```mermaid
xychart-beta
    title "citoverse/cito 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-25 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5595cf8a116c` · [字段定义](../../DATASET.md)*
