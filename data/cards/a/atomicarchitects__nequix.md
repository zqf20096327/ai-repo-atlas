# atomicarchitects/nequix

⭐ 80 · Python · MIT · 推送 2026-04-05 · [GitHub](https://github.com/atomicarchitects/nequix) · [官网](https://arxiv.org/abs/2601.07742) · 组织维护

**材料科学机器学习原子间势基础模型（含声子微调）**

Nequix 提供材料领域基础模型的源码与预训练权重，覆盖 MPtrj、OMat24 等数据集训练的多个模型变体，以及声子微调（PFT）方法。支持 JAX 与 PyTorch 双后端、OpenEquivariance GPU 内核、ASE 计算器接口、解析 Hessian 与声子计算，通过 nequix_train 命令用单个 YAML 配置训练。限制：PFT 训练仅支持 JAX 后端；复现训练需单节点 4×A100，耗时约 60-140 小时。

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

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- 提供 5 个预训练模型权重（MP/OMat/OAM 系列及 PFT 变体）
- JAX/Torch 双后端，GPU 支持 OpenEquivariance 内核
- ASE 计算器接口，支持解析 Hessian 与声子计算
- 声子微调（PFT）训练流程与预处理数据下载脚本

## 适用场景

- 用预训练模型在 ASE 中做材料能量/力/Hessian 计算
- 在自有数据上训练或微调机器学习原子间势
- 做声子与振动性质计算（有限位移或解析 Hessian）
- 复现论文中的 Nequix-MP-1 / OMat / OAM 训练

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: Source code and model weights for the Nequix foundation model, and Phonon fine-tuning (PFT).
> L37: Using `nequix.calculator.NequixCalculator`, you can perform calculations in

## 星数曲线

```mermaid
xychart-beta
    title "atomicarchitects/nequix 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-20"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-20 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `b3a7d7eb6f96` · [字段定义](../../DATASET.md)*
