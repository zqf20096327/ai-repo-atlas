# Suro-One/Hyena-Hierarchy

⭐ 48 · Python · 推送 2026-03-30 · [GitHub](https://github.com/Suro-One/Hyena-Hierarchy) · [官网](https://www.youtube.com/watch?v=jwT__og3epg) · 个人维护

**训练字符级语言模型的 Hyena 卷积架构实现**

基于 PyTorch 实现 Hyena Hierarchy 与 Zera Hierarchy 的字符级语言模型训练代码：Hyena 是一种卷积神经网络变体架构，用于替代循环/注意力结构建模序列。用户需自备 Python 3 与 torch 环境，通过 python hyena-split-memory.py 直接运行训练。代码致谢部分引用 Kalchbrenner 等人的句子建模 CNN 论文及 Poli 等人的 Hyena Hierarchy 论文（斯坦福大学与 Mila 等机构）。README 未提供打包发布、预训练权重或基准结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 Hyena 卷积架构的字符级语言模型训练
- 单脚本运行：python hyena-split-memory.py
- 依赖仅 Python 3 与 torch

## 适用场景

- 研究 Hyena 类卷积序列架构的语言建模
- 复现并修改字符级语言模型训练代码
- 学习长序列卷积架构的实现方式

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L3: This code trains a character-level language model using a variant of a convolutional neural network architecture cal
> L20: ## Hyena Hierarchy: Towards Larger Convolutional Language Models

## 星数曲线

```mermaid
xychart-beta
    title "Suro-One/Hyena-Hierarchy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-26 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4cf2339a4025` · [字段定义](../../DATASET.md)*
