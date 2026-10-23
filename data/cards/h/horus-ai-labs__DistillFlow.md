# horus-ai-labs/DistillFlow

⭐ 169 · Python · Apache-2.0 · 推送 2026-09-20 · [GitHub](https://github.com/horus-ai-labs/DistillFlow) · 组织维护

**将大语言模型蒸馏为小模型的开源工具包**

用于将大语言模型（LLM）蒸馏为更小模型的开源工具包：通过可配置的 YAML 管线指定教师模型、学生模型与 HuggingFace 数据集，支持 logits、attention、layers 等多种蒸馏策略，以及下游微调。基于 GPU/节点可用内存动态分配任务，模型加载兼容 Unsloth、Liger Kernel、Flash Attention 等优化，兼容 Hugging Face Transformers、PyTorch、DeepSpeed。要求 Python 3.12+，支持 Linux/macOS，通过 git clone 与 Poetry 安装，状态标记为 beta。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 logits/attention/layers 等多策略蒸馏
- 基于可用内存在 GPU 或节点间动态分配任务
- 兼容 Hugging Face Transformers、PyTorch、DeepSpeed
- 支持 ShareGPT/Alpaca 格式的 HuggingFace 数据集

## 适用场景

- 用大模型蒸馏出更小的模型以降低部署成本
- 对学生模型做领域或下游任务微调
- 在多 GPU 环境下运行蒸馏训练实验

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L24: DistillFlow is an open-source toolkit designed to simplify and scale the distillation of large language models (LLM
> L40: - **Multi-Strategy Distillation:** Supports multiple distillation techniques such as logits, attention and layers b
> L43: - **Model Loading Optimizations:** Supports optimized model loading using Unsloth, Liger Kernel, Flash Attention et

## 星数曲线

```mermaid
xychart-beta
    title "horus-ai-labs/DistillFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 168 --> 170
    line [169, 169]
```

2026-10-18 169 → 2026-10-23 169（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `96dbc14677da` · [字段定义](../../DATASET.md)*
