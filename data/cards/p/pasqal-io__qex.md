# pasqal-io/qex

⭐ 23 · Jupyter Notebook · NOASSERTION · 推送 2026-06-09 · [GitHub](https://github.com/pasqal-io/qex) · [官网](https://arxiv.org/abs/2404.14258) · 组织维护

**JAX 可微 Kohn-Sham DFT 实现：训练量子(增强)神经网络交换关联泛函**

Pasqal 维护的量子增强 Kohn-Sham 密度泛函理论（KS-DFT）JAX 实现，基于 JAX-DFT（1D）与 PySCFAD（3D），用于训练量子/量子增强神经网络逼近 KS-DFT 的普适交换关联泛函。提供量子-经典混合模型、多种量子网络结构（基础/卷积/全局/局部泛函），通过 Qadence 与 Horqrux 在 GPU 上做量子模拟器加速，支持 JIT 编译与自动微分，附 1D/3D 训练脚本与复现论文的 notebooks。限制：3D 部分仅网络可 jit，且目前仅实现原论文内容。需 Python 3.10.16，从源码克隆安装，GPU 加速需另装 jax[cuda12]。

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

- 量子-经典混合 KS-DFT 实现，多种量子神经网络结构
- JAX 的 JIT 编译、自动微分与 GPU 加速
- 提供 1D 与 3D（H2 分子）训练示例脚本与复现论文的 notebooks
- 用户可继承 KohnShamNetwork 自定义网络

## 适用场景

- 训练量子(增强)神经网络逼近交换关联泛函
- 复现 Phys. Rev. A 论文中的 1D/3D 电子结构实验
- 在 JAX 生态中做可微 DFT 电子结构研究

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: QEX is a quantum-enhanced implementation of Kohn-Sham Density Functional Theory (KS-DFT) in JAX, building upon the 
> L17: The primary goal is to enable to train quantum(-enhanced) neural networks to approximate the universal exchange-cor
> L21: QEX leverages JAX primitives for JIT compilation, automatic differentiation, and GPU acceleration for quantum emula

## 星数曲线

```mermaid
xychart-beta
    title "pasqal-io/qex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `5e30b3e3957a` · [字段定义](../../DATASET.md)*
