# lbl-camera/fvGP

⭐ 16 · Python · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/lbl-camera/fvGP) · [官网](https://fvgp.readthedocs.io/) · 组织维护

**面向 HPC 的函数值高斯过程（GP）Python 库**

Python 包 fvGP，提供高度灵活的函数值高斯过程实现，专长包括超大规模 GP、面向 HPC 训练的 GP、高级核函数设计与域感知随机函数逼近；作者称其保持精确大规模 GP 的世界纪录（README 自述）。README 建议通过 gpCAM 使用本包。由 LBNL 等机构相关人员开发，获 DOE 多项目支持，依赖同团队的 HGDL 优化包做训练。计划中功能：随机流形学习。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 函数值高斯过程（fvGP）的灵活实现
- 面向 HPC 训练与超大规模场景设计
- 高级核函数设计与域感知随机函数逼近
- 使用 HGDL 优化包（基于 HGDN 算法）

## 适用场景

- 科学计算与实验设计中的大规模函数值 GP 建模
- 需要域感知随机函数逼近的代理模型任务
- 作为 gpCAM 的底层 GP 引擎使用

## 场景标签

 · 领域:科学计算/机器学习库

## 证据(README 行号)

> L11: Python package for highly flexible function-valued Gaussian processes (fvGP)
> L15: Specialties: Extreme-Scale GPs, GPs Tailored for HPC training, Advanced Kernel Designs, Domain-Aware Stochastic Fun

## 星数曲线

```mermaid
xychart-beta
    title "lbl-camera/fvGP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2b37d9777ba3` · [字段定义](../../DATASET.md)*
