# deepspeedai/DeepSpeed

⭐ 43,351 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/deepspeedai/DeepSpeed) · [官网](https://www.deepspeed.ai/) · 组织维护

**面向开发者的大模型分布式训练与推理优化库**

PyTorch 生态的深度学习优化库，提供 ZeRO、ZeRO-Infinity、3D 并行、Ulysses 序列并行、DeepSpeed-MoE 等系统创新，支持大规模模型训练与推理，含压缩与 MoE 能力。以 pip 安装，C++/CUDA 扩展默认通过 JIT 在运行时编译链接，需要预先安装 PyTorch 及 nvcc/hipcc 编译器。已与 Transformers、Accelerate、Lightning、MosaicML、Determined、MMEngine 等框架集成，Windows 上多数功能可用但 AIO/GDS 不支持。

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

- ZeRO/ZeRO-Infinity 内存优化与 3D 并行（数据/模型/流水线）
- 支持万亿参数规模训练，曾被用于训练 MT-530B、BLOOM 等模型
- 与 Transformers、Accelerate、Lightning 等多个框架集成
- 支持 NVIDIA/AMD GPU、CPU、华为昇腾、Intel Gaudi/XPU 等硬件

## 适用场景

- 单机多卡或多节点训练大参数量模型
- 通过 ZeRO-Offload 在有限显存下训练 LLM
- 为 Hugging Face 模型自动配置张量并行训练

## 场景标签

`模型训练` `微调` · 领域:训练与推理

## 证据(README 行号)

> L54: ***DeepSpeed enabled the world's most powerful language models (at the time of this writing) such as MT-530B and BL
> L76: DeepSpeed has been integrated with several different popular open-source DL frameworks such as:
> L101: # Installation

## 星数曲线

```mermaid
xychart-beta
    title "deepspeedai/DeepSpeed 星数(近 27 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 43235 --> 43361
    line [43245, 43251, 43259, 43263, 43272, 43278, 43270, 43269, 43270, 43277, 43278, 43279, 43263, 43312, 43317, 43322, 43326, 43327, 43325, 43326, 43332, 43335, 43339, 43344, 43349, 43347, 43351]
```

2026-10-21 43,245 → 2026-11-23 43,351（+106）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `7c174cb4f561` · [字段定义](../../DATASET.md)*
