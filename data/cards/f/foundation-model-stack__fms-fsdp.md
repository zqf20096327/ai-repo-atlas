# foundation-model-stack/fms-fsdp

⭐ 289 · Python · Apache-2.0 · 推送 2025-11-24 · [GitHub](https://github.com/foundation-model-stack/fms-fsdp) · [官网](https://pytorch.org/docs/stable/fsdp.html) · 组织维护

**基于 PyTorch FSDP 的基础模型高效预训练示例代码库**

Foundation Model Stack 的配套仓库，提供使用 PyTorch 原生特性（FSDP 分布式训练、SDPA 实现的 Flash Attention v2、torch.compile、选择性激活检查点）高效预训练 FMS 模型（以 Llama2 为主）的示例与脚本。给出在 128×A100 与 96×H100 上的吞吐与 MFU/HFU 基准，并分享一个训练至 2.2T tokens 的 Llama2 7B 复现模型。README 声明其非端到端框架，不含数据准备与对齐微调，需 Slurm 等集群环境运行。

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

- FSDP + SDPA Flash v2 + torch.compile 的高效预训练实现
- 7B-70B 模型在 A100/H100 集群的吞吐与 MFU/HFU 基准数据
- FMS 格式模型转换为 Hugging Face 格式的脚本
- 以 128×A100 训练 Llama2 7B 复现模型至 2.2T tokens 的实践记录

## 适用场景

- 参考脚本在 GPU 集群上预训练 Llama2 类模型
- 了解 FSDP 大规模训练的配置与最佳实践
- 对比不同分片策略与激活检查点下的训练吞吐

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L4: The goal of this repo is to provide a (pre)training example to efficiently train
> L5: FMS models, in particular Llama2 by leveraging native PyTorch features - FSDP for training and SDPA implementation o

## 星数曲线

```mermaid
xychart-beta
    title "foundation-model-stack/fms-fsdp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 287 --> 290
    line [288, 289]
```

2026-10-18 288 → 2026-10-23 289（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a3b755b620b0` · [字段定义](../../DATASET.md)*
