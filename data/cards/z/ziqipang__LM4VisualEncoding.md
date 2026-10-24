# ziqipang/LM4VisualEncoding

⭐ 245 · Python · MIT · 推送 2026-06-29 · [GitHub](https://github.com/ziqipang/LM4VisualEncoding) · [官网](https://arxiv.org/abs/2310.12973) · 组织维护

**ICLR 2024 论文官方代码：冻结 LLM Transformer 层作视觉编码器**

论文 "Frozen Transformers in Language Models are Effective Visual Encoder Layers" 的官方实现（ICLR 2024 Spotlight）。方法是从预训练 LLM 中提取一个冻结的 Transformer 块，接在原视觉编码器顶部，前后插入可训练线性层对齐特征维度，训练时冻结该 LLM 块仅优化其他模块，用于纯视觉任务。作者提出信息过滤假说解释其效果，并在多类任务上发布实验代码（分目录组织）。README 仅到 Getting Started 入口，具体安装运行需查看各子目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提取冻结 LLM Transformer 块作为视觉编码器层
- 前后线性层对齐特征维度，仅训练非 LLM 模块
- 多任务实验代码按子目录组织发布
- 提出信息过滤假说解释冻结 LLM 块的作用

## 适用场景

- 复现论文的视觉编码实验
- 研究 LLM 预训练权重在视觉任务中的迁移
- 基于该方法开展自己的视觉模型研究

## 场景标签

 · 领域:计算机视觉/表征学习

## 证据(README 行号)

> L25: This paper reveals an intriguing discovery: **pretrained transformers from LLMs, despite being trained solely on te
> L27: Our approach is straightforward yet overlooked: incorporating a **frozen** transformer block from a **pre-trained**

## 星数曲线

```mermaid
xychart-beta
    title "ziqipang/LM4VisualEncoding 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 244 --> 246
    line [245, 245]
```

2026-10-18 245 → 2026-10-24 245（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3f3a94460c20` · [字段定义](../../DATASET.md)*
