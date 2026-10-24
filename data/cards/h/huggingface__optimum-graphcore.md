# huggingface/optimum-graphcore

⭐ 87 · Python · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/huggingface/optimum-graphcore) · 组织维护

**在 Graphcore IPU 上训练/微调/推理 🤗 Transformers 的接口库**

Hugging Face 维护的 🤗 Transformers 与 Graphcore IPU 之间的接口库：提供模型并行化与 IPU 加载工具，支持训练、微调与推理，兼容 🤗 Hub 上的模型。用户以最小代码改动即可切换：将 transformers 的 pipeline 替换为 optimum.graphcore 的 pipeline，或将 Trainer 替换为 IPUTrainer。支持 BERT、GPT-2、T5、ViT、Whisper 等架构及其对应任务矩阵。运行需先启用 Graphcore Poplar SDK 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 pipeline 与 IPUTrainer API，从 🤗 Transformers 最小改动切换到 IPU
- 支持预训练、掩码/因果 LM、Seq2Seq、序列分类、图像分类、CTC 等任务
- 兼容 🤗 Hub 全部模型
- examples 目录提供各任务的 IPU 运行示例

## 适用场景

- 在 IPU 硬件上微调和训练 Transformers 模型
- 把已有 🤗 Transformers 训练代码迁移到 IPU
- 在 IPU 上运行文本/图像/音频任务的推理 pipeline

## 场景标签

`微调` `模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: 🤗 Optimum Graphcore is the interface between the 🤗 Transformers library and Graphcore IPUs.
> L6: It provides a set of tools enabling model parallelization and loading on IPUs, training, fine-tuning and inference o

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/optimum-graphcore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 86 --> 88
    line [87, 87]
```

2026-10-18 87 → 2026-10-24 87（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `17d95f4763f7` · [字段定义](../../DATASET.md)*
