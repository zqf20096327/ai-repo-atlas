# tensorly/torch

⭐ 84 · Python · BSD-3-Clause · 推送 2026-08-12 · [GitHub](https://github.com/tensorly/torch) · [官网](http://tensorly.org/torch/) · 组织维护

**基于 PyTorch 的张量深度学习库：提供张量分解与分解化网络层**

TensorLy-Torch 是构建于 TensorLy 与 PyTorch 之上的 Python 库，面向在深度学习中使用张量方法的开发者。它提供张量分解的统一 API（分解、操作与初始化）、可直接嵌入 PyTorch 模型的张量层（张量回归层、分解化卷积、张量化线性层、张量收缩层），以及 Tensor Dropout、L1 正则自动选秩等张量钩子。支持 CP、Tucker、tensor-train 分解实现的任意阶卷积。为 PyTorch 专用库，可经 pip 或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CP/Tucker/tensor-train 分解化卷积（任意阶）
- 张量回归层、张量化线性层、收缩层等内置张量层
- Tensor Dropout 与 L1 正则端到端自动选择秩
- 张量分解的统一分解/操作/初始化 API

## 适用场景

- 用张量分解压缩 CNN 卷积层参数
- 在 PyTorch 模型中加入张量回归或张量化线性层
- 通过 Tensor Dropout 与自动选秩对网络正则化

## 场景标签

 · 领域:深度学习/张量方法

## 证据(README 行号)

> L6: TensorLy-Torch is a Python library for deep tensor networks that
> L34: **TensorLy-Torch** is a PyTorch only library that builds on top of TensorLy and provides out-of-the-box tensor laye

## 星数曲线

```mermaid
xychart-beta
    title "tensorly/torch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 83 --> 85
    line [84, 84]
```

2026-10-18 84 → 2026-10-28 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e310a521ea66` · [字段定义](../../DATASET.md)*
