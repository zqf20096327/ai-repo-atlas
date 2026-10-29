# extropic-ai/sparse-transformers

⭐ 34 · Python · Apache-2.0 · 推送 2026-09-17 · [GitHub](https://github.com/extropic-ai/sparse-transformers) · 组织维护

**JAX 稀疏注意力 Transformer 研究代码集合**

包含多个 JAX 研究子项目的仓库，主题为稀疏与注意力变体的 Transformer 模型：research/st 提供稀疏因果 Transformer 语言模型，research/z1t 提供 Z1 可编译 Transformer。每个子项目有独立的 pyproject.toml，需进入各自目录按其 README 给出的命令安装。仓库本身未提供统一安装入口、模型权重或使用示例，面向研究者复现或扩展这些模型结构。

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

- 稀疏因果 Transformer 语言模型（research/st）
- Z1 可编译 Transformer（research/z1t）
- 每个子项目独立 pyproject.toml 与安装说明

## 适用场景

- 研究稀疏注意力 Transformer 结构
- 复现或扩展仓库内的模型实现
- 基于 JAX 开展注意力变体实验

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains JAX research projects for sparse and attention variant transformer models.
> L5: - `research/st`: sparse causal transformer language models.

## 星数曲线

```mermaid
xychart-beta
    title "extropic-ai/sparse-transformers 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-29 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a20d463e3332` · [字段定义](../../DATASET.md)*
