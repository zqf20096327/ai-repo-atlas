# THU-BPM/d-TreeRPO

⭐ 13 · Python · MIT · 推送 2026-01-06 · [GitHub](https://github.com/THU-BPM/d-TreeRPO) · [官网](https://arxiv.org/abs/2512.09675) · 组织维护 · 中文 README

**扩散语言模型的树结构强化学习训练框架（论文代码）**

ACL 2026 论文 d-TreeRPO 的官方代码库，为扩散语言模型（dLLMs）提供强化学习策略优化训练框架。核心机制：将 rollout 组织为树结构并自底向上传播可验证结果奖励，得到细粒度步骤级优势；引入时间调度自蒸馏损失，在训练后期逐步增加模型确定性。训练基于 Diffu-GRPO 与 wd1 代码库，采用 LoRA，提供 LLaDA-8B-Instruct 与 LLaDA-MoE-7BA1B-Instruct 的训练与评测脚本，在 Sudoku、Countdown、GSM8K、Math500 等推理基准上给出结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 树结构 rollout 与自底向上奖励传播得到步骤级优势
- 时间调度自蒸馏损失，逐步增加模型确定性
- 提供 LLaDA-8B-Instruct / LLaDA-MoE-7BA1B-Instruct 训练与评测脚本，采用 LoRA 训练
- 在 Sudoku、Countdown、GSM8K、Math500 等基准上给出结果

## 适用场景

- 用强化学习训练扩散语言模型的推理能力
- 复现论文实验并评测 checkpoint
- 在自定义可验证奖励任务上训练 dLLM

## 场景标签

`强化学习` `微调` · 领域:训练与推理

## 证据(README 行号)

> L7: d-TreeRPO is a reliable reinforcement learning framework for diffusion language models (dLLMs). It improves policy o
> L8: - organizing rollouts into a tree structure and propagating verifiable outcome rewards bottom-up to obtain **fine-gr

## 星数曲线

```mermaid
xychart-beta
    title "THU-BPM/d-TreeRPO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `625b0302269c` · [字段定义](../../DATASET.md)*
