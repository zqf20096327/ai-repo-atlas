# LLM360/Reasoning360

⭐ 154 · Python · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/LLM360/Reasoning360) · [官网](https://guru-reasoning.github.io/) · 组织维护

**面向大推理模型开放研究的 RL 训练与评测工具库**

Reasoning360 官方仓库，围绕大规模推理模型的开源研究：提供数据准备与过滤工具、基于 veRL 初始化的强化学习训练管线、17 项任务的评测套件，配套 Guru-7B 模型、92K Guru RL 数据集与公开 wandb 日志。训练支持多节点 SLURM、SandboxFusion 代码沙箱执行、llm-as-verifier 奖励验证；聊天模板定制目前仅支持 Qwen 系列。面向开展 LLM 推理 RL 研究的开发者与科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据准备/过滤 + RL 训练管线 + 17 任务评测套件
- 基于 veRL 初始化，支持多节点 SLURM 训练与推理
- 配套 Guru-7B 模型、92K Guru RL 数据集与公开训练日志
- SandboxFusion 安全代码执行与 llm-as-verifier 奖励验证

## 适用场景

- 用 Guru 数据复现或开展 LLM 推理 RL 训练研究
- 在多节点集群上训练推理模型并做多任务评测
- 为自定义数据集添加预处理脚本与奖励函数

## 场景标签

`强化学习` `模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L17: This is the official repository of Reasoning360, a project dedicated to *open research on large-scale reasoning mod
> L43: The full ready-to-train 92K Guru RL data is already released under LLM360 huggingface! If you would like to build (

## 星数曲线

```mermaid
xychart-beta
    title "LLM360/Reasoning360 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 153 --> 155
    line [154, 154]
```

2026-10-18 154 → 2026-10-23 154（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `896b669ceaff` · [字段定义](../../DATASET.md)*
