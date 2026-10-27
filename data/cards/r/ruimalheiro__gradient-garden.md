# ruimalheiro/gradient-garden

⭐ 27 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/ruimalheiro/gradient-garden) · 个人维护

**面向研究的模型训练/评测一体化实验代码库**

个人维护的开源研究代码库，把模型架构、训练目标、优化器、数据准备、分布式执行、检查点、推理与评测放在同一代码库中，便于检视与修改。支持预训练、SFT、DPO、LoRA、知识蒸馏；包含自研 Tendril/TendrilMoE 架构与 Hugging Face 模型包装器；执行支持单机 CPU 调试到多机 DDP/FSDP2。实验以 recipe（YAML）描述配置与数据，数据准备支持数据集 revision 固定、加权混合与按源 token 预算、可断点续跑。评测覆盖 HellaSwag/WinoGrande/ARC/IFEval 等。当前聚焦 CUDA 语言模型训练。

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

- 预训练/SFT/DPO/LoRA/蒸馏训练工作流，支持 DDP/FSDP2 多机多卡
- recipe 机制将实验配置与数据定义绑定在一起
- 可复现数据准备：数据集 revision 固定、确定性混合、断点续跑
- 自研 Tendril/TendrilMoE 架构（GQA/RoPE/MoE）与 Hugging Face 模型包装器

## 适用场景

- 研究者在同一代码库里做训练方法与架构实验
- 做带精确 token 预算与数据混合配方的预训练实验
- 在标准基准（HellaSwag/IFEval 等）上评测自训模型

## 场景标签

`模型训练` `微调` `模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L3: Gradient Garden is an open research codebase for experimenting with machine learning models, training methods, data,
> L5: The goal is to keep the important parts of the research stack easy to inspect and modify: model architectures, train
> L7: The project currently focuses on CUDA-based language-model training, but it is not intended to be limited to languag

## 星数曲线

```mermaid
xychart-beta
    title "ruimalheiro/gradient-garden 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9532ed88b375` · [字段定义](../../DATASET.md)*
