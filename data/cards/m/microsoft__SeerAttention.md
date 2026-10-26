# microsoft/SeerAttention

⭐ 222 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/microsoft/SeerAttention) · 组织维护

**可训练稀疏注意力机制：通过自蒸馏加速 LLM 长上下文推理**

微软发布的 SeerAttention 与 SeerAttention-R 官方实现：一种可训练的块级稀疏注意力机制，在 post-training 阶段通过自蒸馏训练注意力门控（AttnGates），原始模型权重冻结，推理时将蒸馏出的 AttnGates 与基础模型组合，实现长上下文 prefill 与解码（长推理）加速。提供 Block-sparse FlashAttention 内核、HuggingFace 上多组预蒸馏 AttnGates 权重（Llama-3.1、Qwen2.5/Qwen3、DeepSeek-R1-Distill 系列），以及自训练脚本（目前仅支持 Qwen2/Qwen3 架构）。

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

- 块级稀疏注意力 + Block-sparse FlashAttention 内核
- 自蒸馏训练 AttnGates，原始模型权重冻结
- 提供多组基础模型的预蒸馏 AttnGates 权重（HuggingFace）
- 支持 Threshold / TopK 两种稀疏化方法

## 适用场景

- 为 Llama/Qwen/DeepSeek 蒸馏模型加速长上下文推理
- 长推理（reasoning）场景下做稀疏解码加速
- 为自己的 Qwen2/Qwen3 模型训练注意力门控

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: Official implementation of SeerAttention and SeerAttention-R - a novel trainable sparse attention mechanism that lea
> L12: **Self-Distillation** - Lightweight training of attention gates (original weights frozen)

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/SeerAttention 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 221 --> 223
    line [222, 222]
```

2026-10-18 222 → 2026-10-26 222（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9322b6ffa514` · [字段定义](../../DATASET.md)*
