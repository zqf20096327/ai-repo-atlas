# kkirchheim/pytorch-ood

⭐ 352 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/kkirchheim/pytorch-ood) · [官网](https://pytorch-ood.readthedocs.io/) · 个人维护

**基于 PyTorch 的分布外（OOD）检测库，供研究者评测检测方法**

Python 库 pytorch-ood，面向使用深度神经网络做分布外检测（OOD Detection）的研究者与开发者：提供 20 余种检测器实现（OpenMax、ODIN、Mahalanobis、Energy-Based、ViM 等）、损失函数、数据集、预训练网络权重与数据增强，并兼容 pytorch-lightning 等框架；覆盖开集识别、新颖性检测、置信度估计、异常检测等相邻领域的方法。内置基准评测（如 OpenOOD v1.5），缓存 logits 复用计算；约定 OOD 检测器输出离群值分数且 OOD 数据标签须小于 0。经 PyPI 安装，依赖 torch/torchvision/scipy。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 余种 OOD 检测器实现（2016-2022 年论文方法）
- 提供预训练模型权重（如 WideResNet-40 CIFAR-10）与统一加载接口
- 内置 OpenOOD v1.5 等基准评测，支持 logits/特征缓存复用
- 覆盖开集识别、新颖性检测、置信度估计、异常分割等相邻方法

## 适用场景

- 评测与对比多种 OOD 检测方法在标准基准上的表现
- 给已有 PyTorch 分类模型添加分布外/离群检测能力
- 复现 OOD 检测论文方法或开展新方法研究

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L38: A Python library for Out-of-Distribution (OOD) Detection with Deep Neural Networks based on PyTorch.
> L42: - Out-of-Distribution Detection Methods
> L109: Evaluate detectors against common benchmarks, for example the OpenOOD v1.5 CIFAR benchmark.

## 星数曲线

```mermaid
xychart-beta
    title "kkirchheim/pytorch-ood 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 349 --> 353
    line [350, 351, 352]
```

2026-10-18 350 → 2026-10-29 352（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d89bf539d7bb` · [字段定义](../../DATASET.md)*
