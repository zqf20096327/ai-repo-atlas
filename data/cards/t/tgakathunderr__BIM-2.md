# tgakathunderr/BIM-2

⭐ 23 · Python · 推送 2026-05-21 · [GitHub](https://github.com/tgakathunderr/BIM-2) · [官网](https://unikai.vercel.app/docs/bim) · 个人维护

**仿生序列学习模型：以 Jaccard 惊讶度为唯一训练信号的 CPU 语言模型**

BIM 2 是受生物学启发的序列学习架构，不使用反向传播、GPU 与预训练。它将 token 映射为 16,384 列的稀疏分布式表示，在两层皮层（L1 感觉层/L2 抽象层）中通过自顶向下顶端反馈进行预测；预测与实际 SDR 的 Jaccard 距离作为唯一训练信号，按惊讶度缩放 Hebbian 学习率，支持会话中 WRONG/RIGHT 在线纠错。附带 ConceptGraph 概念结晶与 BFS 两跳推理、虚构语料 NovaCorp 基准（直接召回≥60%、推理≥30%）。限制：词级分词器（词表上限 5000）、无开放域知识、交互模式仅单 token 回复。面向计算神经科学与轻量机器学习方向的研究者与开发者。

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

- Jaccard 惊讶度作为唯一训练信号，无损失函数/优化器/梯度
- 两层皮层架构含 L2→L1 顶端偏置反馈与突触稳态
- 131,072 细胞全 CPU 运行，内存低于 200MB
- ConceptGraph 概念结晶与深度 2 的 BFS 多跳推理

## 适用场景

- 研究无反向传播的在线 Hebbian 序列学习
- 在 CPU 上小内存环境做小规模序列记忆与纠错学习实验
- 复现 NovaCorp 域知识直接召回与两跳推理基准

## 场景标签

 · 领域:机器学习/计算神经科学

## 证据(README 行号)

> L3: A biologically inspired sequence learning architecture. No backpropagation. No GPU. No pretraining.
> L9: Before each token arrives, BIM predicts which sparse columns should activate next, based purely on what it has learn
> L63: python main.py interact

## 星数曲线

```mermaid
xychart-beta
    title "tgakathunderr/BIM-2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `a0111af2b375` · [字段定义](../../DATASET.md)*
