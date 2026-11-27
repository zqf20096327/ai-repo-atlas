# Sidiora-Labs/llm-training-clearforge

⭐ 5 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/Sidiora-Labs/llm-training-clearforge) · 组织维护

**从零预训练并微调小型语言模型的可复现训练系统**

Clearforge 将本地文本与对话数据集经过校验、去重、tokenization、预训练、监督微调、评估到模型导出的完整流程；内置紧凑 PyTorch decoder、TOML 严格配置与可断点续跑的 CLI。提供 100M/300M/1B 预设，支持 CPU/CUDA/分布式训练、LoRA/DPO/PPO 等后训练方法，可导出 Transformers 兼容模型并起 chat API 服务。要求 Python 3.11+ 与 Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 PyTorch decoder 从零预训练，100M/300M/1B 预设可自定义
- 支持 LoRA、DPO、蒸馏、PPO、GRPO、CISPO 等后训练方法
- 原子检查点恢复优化器/调度器/数据位置，支持断点续跑
- 可导出 Transformers 兼容模型并提供 /v1/chat/completions API

## 适用场景

- 在本地数据上从零预训练小型语言模型
- 对自训模型做对话微调与偏好优化
- 导出模型到 Transformers 生态并部署 chat 服务

## 场景标签

`模型训练` `微调` `强化学习` · 领域:训练与推理

## 证据(README 行号)

> L18: Clearforge takes local text and conversation datasets through validation,
> L32: - Fine-tune with LoRA, DPO, distillation, PPO, GRPO, and CISPO.
> L121: `torchrun` with Gloo on CPU or NCCL on CUDA. Optional `serving` and `huggingface`

## 星数曲线

```mermaid
xychart-beta
    title "Sidiora-Labs/llm-training-clearforge 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-25 5 → 2026-11-27 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `c92c1a4a1e09` · [字段定义](../../DATASET.md)*
