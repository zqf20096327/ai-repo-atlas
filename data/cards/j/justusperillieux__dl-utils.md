# justusperillieux/dl-utils

⭐ 14 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/justusperillieux/dl-utils) · 个人维护

**为深度学习开发者提供 PyTorch 损失、模型与指标工具库**

一个 PyTorch 深度学习工具库，以函数式与模块化两种形式提供损失函数、模型定义和指标，尽可能使用纯 PyTorch 实现。包含数据工具（随机假数据集）、GAN 基础实现、附加优化器和张量操作等子包。可通过 pip 从 PyPI 或源码安装，可搭配任意训练框架使用。作者声明代码测试覆盖不完整，尚无完整 CI/CD 与单元测试。

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

- 损失函数、模型定义与指标同时提供函数式和模块化两种接口
- 尽可能采用纯 PyTorch 实现，可搭配 Ignite、PyTorch-Lightning 或自定义训练循环使用
- 子包覆盖数据、损失、指标、模型（含 GAN）、优化器与工具函数

## 适用场景

- 训练 PyTorch 模型时补充框架未内置的损失函数与指标
- 以任意维度使用流行模型的 Nd 实现
- 在自定义训练循环中复用优化器与张量工具

## 场景标签

 · 领域:机器学习/深度学习

## 证据(README 行号)

> L4: This package contains mainly loss functions, model definitions and metrics in both functional and modular and (whene
> L17: * `dlutils.losses`: extends the losses given in PyTorch itself by a few more loss functions


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `4cfa0a36d8db` · [字段定义](../../DATASET.md)*
