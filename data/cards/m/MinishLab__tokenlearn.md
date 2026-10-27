# MinishLab/tokenlearn

⭐ 111 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/MinishLab/tokenlearn) · [官网](https://minish.ai/packages/tokenlearn/usage) · 组织维护

**预训练 Model2Vec 静态词嵌入模型的训练方法库**

MinishLab 维护的 Python 包，用于预训练 Model2Vec 静态嵌入模型（如 Potion 系列）。流程分两步：featurize 从任意 sentence transformer 与 HuggingFace 数据集生成 mean token 嵌入数据集，train 以这些嵌入为目标训练静态模型，并可推送至 Hub。训练产出基础模型与加权模型两个版本。限制：代码假设 tokenizer 的 padding token ID 为 0，否则需修改代码。提供 CLI 命令与可选评测依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- featurize CLI 从 sentence transformer 生成 mean token 嵌入数据集
- train CLI 训练 Model2Vec 静态模型，产出基础与加权两个版本
- 数据集与模型支持 HuggingFace Hub 推送与 repo ID 读取
- 用于训练 Potion 系列模型（potion-base-32M 等）

## 适用场景

- 训练自己的 Model2Vec 静态嵌入模型
- 基于任意 HuggingFace 数据集蒸馏 sentence transformer 为静态嵌入
- 复现 Potion 系列模型的训练流程

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L15: Tokenlearn is a method to pre-train Model2Vec static embedding models. The original version, used to train the firs
> L25: Tokenlearn consists of two steps: **featurize** (create mean token embeddings from a sentence transformer) and **tr

## 星数曲线

```mermaid
xychart-beta
    title "MinishLab/tokenlearn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 110 --> 112
    line [111, 111]
```

2026-10-18 111 → 2026-10-27 111（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ec480a2f7439` · [字段定义](../../DATASET.md)*
