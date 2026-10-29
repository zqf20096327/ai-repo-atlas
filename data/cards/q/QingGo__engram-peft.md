# QingGo/engram-peft

⭐ 52 · Python · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/QingGo/engram-peft) · 个人维护 · 中文 README

**DeepSeek Engram 论文的非官方 PEFT 实现，为 LLM 注入条件记忆**

对 DeepSeek Engram 架构（arXiv:2601.07372）的非官方 PyTorch 实现：以 PEFT 风格接口通过 forward hooks 向任意 Transformer LLM 注入稀疏检索式条件记忆，不增加推理 FLOPs，支持 engram_only/preserve_trainable/full_finetune 三种训练模式及 LoRA+Engram 叠加训练。提供 engram-peft CLI 的 YAML 声明式训练流程、自动生成推理脚本、跨模型权重迁移、bitsandbytes/GPTQ 量化兼容，设备后端覆盖 CUDA/NPU(Ascend)/CPU，并兼容 torchrun DDP 与 DeepSpeed ZeRO-1/2。面向需要向模型注入大规模知识且控制推理开销的研究者与开发者。

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

- forward hooks 零侵入注入，不增加推理 FLOPs，每步仅约 1% 参数激活
- LoRA+Engram 叠加训练与跨模型 Engram 权重迁移（如 Llama→Qwen）
- YAML 驱动 CLI 训练并自动生成可运行的 inference.py
- CUDA/NPU(Ascend)/CPU 统一设备后端，兼容 DDP 与 DeepSpeed ZeRO-1/2

## 适用场景

- 在推理开销不变的前提下向基础模型注入大规模事实性知识
- 用 LoRA+Engram 同时做结构适配与知识注入的实验对比
- 在华为昇腾 NPU 上进行分布式条件记忆训练

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L11: **Engram-PEFT** is a high-performance, 100% paper-aligned implementation of the DeepSeek Engram architecture. It pr
> L13: Engram decouples **static knowledge storage** from **dynamic reasoning** using a sparse retrieval mechanism, allowi
> L123: - **Hugging Face Hub Integration**: Support for pushing adapters via `push_to_hub` and loading directly from Hub I

## 星数曲线

```mermaid
xychart-beta
    title "QingGo/engram-peft 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-29 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c91c0a028301` · [字段定义](../../DATASET.md)*
