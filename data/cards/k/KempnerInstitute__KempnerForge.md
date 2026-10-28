# KempnerInstitute/KempnerForge

⭐ 21 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/KempnerInstitute/KempnerForge) · [官网](https://kempnerinstitute.github.io/KempnerForge/) · 组织维护

**面向 AI 集群的基础模型容错分布式训练框架**

Kempner Institute 维护的 PyTorch 原生训练框架：通过 TOML 配置切换 125M–70B 的 decoder-only Transformer（含 MoE、VLM 四种视觉-语言架构），自动组合 FSDP2/张量/专家/流水线并行，提供 FP8 混合精度、异步 DCP 检查点与自动恢复、SLURM 抢占处理、NaN/GPU/NCCL 健康监控。面向做 scaling law 实验、机制可解释性与稀疏架构研究的科研用户，另附 AI 编码助手插件技能集。当前为 v0.1，MoE 工程路线图部分项仍在推进。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TOML 配置切换 125M–70B 架构，四种并行策略自动组合
- dense 与 MoE 一键切换（softmax top-k 或 DeepSeek-V3 sigmoid 路由）
- SLURM 抢占处理、异步检查点、自动恢复与 GPU/NCCL 健康监控
- 四种 VLM 架构（Joint-Decoder/Cross-Attention/MoT/MoMa）与激活提取钩子

## 适用场景

- 在共享集群上跑 125M 到 70B 的 scaling law 实验
- 提取各层激活与注意力权重做机制可解释性研究
- 对比 Muon/Lion/Schedule-Free AdamW 等优化器与调度器组合
- 训练 dense 或 MoE 基础模型并从中断处自动恢复

## 场景标签

`模型训练` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L11: PyTorch-native framework for fault-tolerant distributed training of foundation models on AI clusters.
> L15: - **Scaling law experiments**: train the same architecture from 125M to 70B by swapping a TOML config. FSDP, tensor
> L19: - **Long-running jobs on shared clusters**: SLURM preemption handling, async DCP checkpointing, auto-resume, NaN de

## 星数曲线

```mermaid
xychart-beta
    title "KempnerInstitute/KempnerForge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a191c3e15983` · [字段定义](../../DATASET.md)*
