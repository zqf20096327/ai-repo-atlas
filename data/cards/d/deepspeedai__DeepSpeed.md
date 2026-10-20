# deepspeedai/DeepSpeed

⭐ 43,242 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/deepspeedai/DeepSpeed) · [官网](https://www.deepspeed.ai/) · 组织维护 · 中文 README

**面向大模型训练与推理的分布式优化库**

DeepSpeed 是一个深度学习优化库，提供分布式训练与推理能力，核心机制包括 ZeRO、ZeRO-Infinity、3D 并行、Ulysses 序列并行、DeepSpeed-MoE 等。支持 NVIDIA（Pascal 至 Hopper）、AMD MI100/MI200，并有华为昇腾 NPU、Intel Gaudi 2/Xeon/XPU、Tecorigin SDAA 等社区贡献的硬件适配。通过 pip 安装，C++/CUDA 扩展默认以 JIT 方式在运行时构建；Windows 支持部分训练与推理功能。曾用于训练 MT-530B、BLOOM 等大模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 17,433 位贡献者
- 涨星:近 1 天 **+2**(自 20261016 起算)
- 安装:pypi 包 `deepspeed` 月下载 1,054,708

## 能力要点

- ZeRO/ZeRO-Infinity、3D 并行、Ulysses 序列并行、DeepSpeed-MoE 等系统机制
- 多硬件后端：NVIDIA/AMD/CPU/Gaudi2/XPU/昇腾 NPU/SDAA
- 与 Transformers、Accelerate、Lightning、MosaicML、Determined、MMEngine 等框架集成
- pip 安装 + torch JIT 编译扩展，ds_report 校验环境

## 适用场景

- 训练数百亿到万亿参数规模的大模型
- 分布式训练/推理的显存与通信优化
- 在 AMD、昇腾、Gaudi 等多类加速器上运行训练任务

## 场景标签

`模型训练` `推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L52: # Extreme Speed and Scale for DL Training
> L54: ***DeepSpeed enabled the world's most powerful language models (at the time of this writing) such as MT-530B and BL
> L100: # Installation
> L110: ## Requirements

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `0b10b97597a6` · [字段定义](../../DATASET.md)*
