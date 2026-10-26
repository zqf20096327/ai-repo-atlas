# SarodYatawatta/federated-pytorch-test

⭐ 42 · Python · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/SarodYatawatta/federated-pytorch-test) · 个人维护

**面向研究者的 PyTorch 联邦学习实验代码集（CIFAR10）**

提供一组基于 PyTorch 的联邦学习训练脚本：在 CIFAR10 上训练 K 个 CNN 模型，每个模型仅使用 1/K 训练数据且不共享数据，实现联邦平均、FedProx、共识优化（自适应 ADMM）等算法；与常规做法不同，仅在模型间传递参数子集以降低带宽。附带随机 LBFGS 优化器，支持 ResNet18、变分自编码器联邦训练、联邦聚类 VAE 及基于 LOFAR 数据的对比预测编码示例。GPU 加速可选（use_cuda=True）。以源码脚本形式提供，无打包安装流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 联邦平均/FedProx/共识优化（ADMM）多种算法实现
- 仅传递参数子集以降低带宽占用
- 附带随机 LBFGS 优化器
- 含联邦 VAE、联邦聚类 VAE、CPC 等扩展脚本

## 适用场景

- 在 CIFAR10 上对比联邦平均与共识优化的训练效果
- 研究低带宽下仅传参数子集的联邦学习
- 复现联邦 VAE 聚类与对比预测编码等论文实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L2: We train CNN models __without__ having access to the full dataset. The CIFAR10 dataset is used in all examples. The 
> L19: ``` consensus_multi.py ```: Train K models using 1/K of the data, with consensus optimization (adaptive) ADMM, K ca

## 星数曲线

```mermaid
xychart-beta
    title "SarodYatawatta/federated-pytorch-test 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `00b66b57d3cb` · [字段定义](../../DATASET.md)*
