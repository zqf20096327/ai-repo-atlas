# XMU-Kuangnan-Fang-Team/GENetLib

⭐ 197 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/XMU-Kuangnan-Fang-Team/GENetLib) · [官网](https://genetlib.readthedocs.io/en/latest/) · 组织维护

**用深度学习做基因-环境交互分析的 Python 库**

面向复杂疾病研究者的 Python 库，通过神经网络框架进行基因-环境（G-E）交互分析。支持标量与函数型（稠密测量）输入，输出覆盖连续、二分类与生存数据；在神经网络估计中集成 MCP 稀疏惩罚与 L2 正则以处理高维遗传数据。提供 scalar_ge 与 func_ge 两个核心函数，含模拟数据生成；基于 PyTorch，兼容 Python 3.8+，从 PyPI 安装。方法源自 Genetic Epidemiology 等论文。

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

- 神经网络框架下的 G-E 交互分析，支持标量与函数型输入
- 连续、二分类、生存三类输出支持
- MCP 稀疏惩罚与 L2 正则处理高维遗传数据
- 提供模拟数据生成与核心函数 scalar_ge / func_ge

## 适用场景

- 对高维基因数据做基因-环境交互分析
- 处理稠密测量的函数型 SNP 数据的交互分析
- 复现或扩展基于深度学习的 G-E 交互方法

## 场景标签

 · 领域:生物信息学/统计遗传学

## 证据(README 行号)

> L12: ``GENetLib`` is a Python library designed for gene-environment interaction analysis via neural network, addressing 
> L22: By integrating minimax concave penalty (MCP) and $L_2$-norm regularization within a neural network estimation frame

## 星数曲线

```mermaid
xychart-beta
    title "XMU-Kuangnan-Fang-Team/GENetLib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-18 197 → 2026-10-24 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3f1d74e98e66` · [字段定义](../../DATASET.md)*
