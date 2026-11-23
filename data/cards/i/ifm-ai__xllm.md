# ifm-ai/xllm

⭐ 138 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/ifm-ai/xllm) · [官网](https://ifm.ai/) · 组织维护

**长上下文 LLM 预训练框架：分布式训练与数据处理一体化**

xLLM 是基于 PyTorch 的长上下文语言建模训练框架，将分布式训练、在线数据准备、评估与模型导出集成在一个仓库中。支持 dense、MoE、MoVA 架构，提供 FSDP1/FSDP2、数据/模型/上下文并行，内置自定义 CUDA 内核与 FlashAttention 后端，支持 checkpoint 恢复、困惑度与任务评估、Hugging Face 导出，并通过 xBridges 与 vLLM 集成部署。要求 PyTorch ≥ 2.11 与 CUDA ≥ 12.8，从源码构建安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 dense、MoE、MoVA 模型架构
- FSDP1/FSDP2 与数据/模型/上下文并行训练
- 在线数据管线：并行分词、异步准备、buffered shuffle、bestfit packing
- 自定义 CUDA 内核与 FlashAttention 2/3/4 后端可选

## 适用场景

- 预训练长上下文语言模型
- 在多 GPU 集群上进行分布式训练
- 训练后将 checkpoint 导出 Hugging Face 并用 vLLM 部署

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L15: xLLM is a PyTorch-based framework for long-context language modeling, with
> L27: |**Training to deployment**|Checkpoint/resume, perplexity and task evaluation, Hugging Face export, and vLLM integr
> L40: ### 1. Install xLLM


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `1759410927ec` · [字段定义](../../DATASET.md)*
