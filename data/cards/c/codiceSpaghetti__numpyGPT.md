# codiceSpaghetti/numpyGPT

⭐ 20 · Python · 推送 2025-11-23 · [GitHub](https://github.com/codiceSpaghetti/numpyGPT) · 个人维护

**仅用 NumPy 从零实现 GPT 的教育性项目：手写前向/反向传播**

用 NumPy 与 Python 标准库从零实现 GPT：Linear、Embedding、LayerNorm、MultiHeadAttention 等模块均手写前向与反向传播，无自动求导、无框架依赖，并提供 char/word/BPE 三种分词器、Adam 优化器与配套教学文档（BACKPROP.md、OPTIMIZERS.md、TOKENIZERS.md）。README 记录了在 Shakespeare 数据集上三种分词方式的同架构对比实验，含损失、参数量、输出样例与训练曲线。面向希望理解 Transformer 与反向传播内部机制的开发者和学习者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手写每层的前向/反向传播，梯度计算显式可见
- 提供 char/word/BPE 三种分词器与 Adam 优化器
- 含反向传播、优化器、分词器的配套教学文档
- 三种分词方式的同架构训练对比实验与结果分析

## 适用场景

- 学习 Transformer 与反向传播的底层实现
- 比较字符级/词级/BPE 分词对训练与生成的影响
- 作为从零实现语言模型的参考代码

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: GPT from scratch. Just NumPy and Python.
> L9: Understanding comes from building. This repo implements the core pieces of neural networks - modules, tokenizers, op
> L63: - **Explicit gradients** - see exactly how backprop works

## 星数曲线

```mermaid
xychart-beta
    title "codiceSpaghetti/numpyGPT 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1402439d1999` · [字段定义](../../DATASET.md)*
