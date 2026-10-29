# Jaykef/ai-algorithms

⭐ 183 · Jupyter Notebook · MIT · 推送 2026-07-30 · [GitHub](https://github.com/Jaykef/ai-algorithms) · 个人维护

**面向低算力研究者的 AI 算法第一性原理实现集合**

收录 20 余个 AI 算法（KDA、Rectified Flow、GRPO 训练器、Byte Latent Transformer、Forward-Forward、I-JEPA、知识蒸馏等）的最小化从零实现，每个实现附论文链接与 demo。目标是提供理解基础算法的教育资源，面向算力受限（gpu poor）的研究者，声明所有代码可在 CPU 与 8GB 内存下运行，部分实现支持 GPU（vllm + flash attention）。以 Jupyter notebook 为主，建议在 Colab 或 VSCode 中打开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 20 余个 AI 算法的第一性原理最小实现，各附论文与 demo
- 声明全部代码可在 CPU、8GB 内存环境运行
- 多个实现的论文来源（Meta/Microsoft/Apple/学术机构）均在条目中标注
- 包含自研 GRPO 训练器，支持 SmolLM2/SmolVLM 等小模型

## 适用场景

- 想从零理解某篇算法论文的研究者对照实现学习
- 低配 CPU 机器上复现小型训练实验
- 快速浏览多个注意力/归一化/训练算法变体的对比实验

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: This repo is a work in progress containing first-principle nano implementations of groundbreaking AI algorithms usin
> L5: ## Implementations

## 星数曲线

```mermaid
xychart-beta
    title "Jaykef/ai-algorithms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 182 --> 184
    line [183, 183]
```

2026-10-18 183 → 2026-10-29 183（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b6c6dd690a37` · [字段定义](../../DATASET.md)*
