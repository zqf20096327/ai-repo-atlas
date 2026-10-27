# bsc-quantic/tn4ml

⭐ 23 · Python · MIT · 推送 2026-06-23 · [GitHub](https://github.com/bsc-quantic/tn4ml) · [官网](https://tn4ml.readthedocs.io) · 组织维护

**基于张量网络做机器学习的 Python 库**

tn4ml 是用于机器学习应用的张量网络 Python 库，构建在 Quimb（张量网络对象）与 JAX（优化流程）之上。支持一维张量网络结构（MPS/MPO/Spaced MPO），并提供多种嵌入函数、初始化技术、目标函数与优化策略。示例覆盖分类、异常检测（含 DMRG 类方法）、乳腺癌分类、MNIST 无监督学习与 LHC 质子碰撞事件潜在空间异常检测。通过 pip 安装，支持 GPU 运行，附论文与文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 MPS/MPO/Spaced MPO 三种一维张量网络结构
- 构建于 Quimb 与 JAX 之上，可配置嵌入、初始化、目标函数与优化策略
- 提供分类与异常检测示例（含 DMRG 类方法、LHC 粒子碰撞事件数据）
- 支持 GPU 运行与 64 位精度配置

## 适用场景

- 用张量网络做分类或异常检测任务
- 研究高能物理事件数据（如 LHC）的潜在空间异常检测
- 在 JAX 流水线中训练矩阵乘积态模型

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: **tn4ml** is a Python library that handles tensor networks for machine learning applications.
> L11: It is built on top of **Quimb**, for Tensor Network objects, and **JAX**, for optimization pipeline.

## 星数曲线

```mermaid
xychart-beta
    title "bsc-quantic/tn4ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d3376509bd91` · [字段定义](../../DATASET.md)*
