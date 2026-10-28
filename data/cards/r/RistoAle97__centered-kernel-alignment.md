# RistoAle97/centered-kernel-alignment

⭐ 83 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/RistoAle97/centered-kernel-alignment) · 个人维护

**给研究者的 PyTorch CKA 表示相似度计算库**

以 PyTorch 实现 Centered Kernel Alignment（CKA）相似性指标：基于 HSIC 计算神经网络两层（或两模型）输出表示之间的相似度，支持无偏 HSIC 估计的 minibatch 版本，避免全数据集激活驻留内存。要求 Python ≥ 3.10，可从 PyPI、本仓库或源码安装，附 examples 目录示例。作者声明本仓库主要面向个人与学术用途，不保证对所有模型可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 线性 CKA 相似度计算（基于 HSIC 归一化）
- 提供 minibatch 无偏 HSIC 估计版本，降低内存需求
- 支持 PyPI 安装与源码安装，附基础示例场景

## 适用场景

- 比较同一模型不同层之间的表示相似度
- 比较不同宽度/深度网络学到的表示差异
- 分析模型表示随训练或结构变化的演化

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: > Centered Kernel Alignment (CKA) [1] is a similarity index between representations of features in neural networks,
> L32: Therefore, we need to define the unbiased estimator of HSIC so that the value of CKA is independent of the batch si

## 星数曲线

```mermaid
xychart-beta
    title "RistoAle97/centered-kernel-alignment 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 81 --> 84
    line [82, 83, 83]
```

2026-10-18 82 → 2026-10-28 83（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2f35075ada44` · [字段定义](../../DATASET.md)*
