# TIGER-AI-Lab/Critique-Coder

⭐ 13 · Python · MIT · 推送 2026-04-11 · [GitHub](https://github.com/TIGER-AI-Lab/Critique-Coder) · [官网](https://tiger-ai-lab.github.io/Critique-Coder) · 组织维护

**训练代码模型的批判强化学习方法（ICLR26 论文）**

研究项目，提出用批判强化学习（Critique RL）训练代码模型：基于 rStar-Coder 过滤构建 rStar-Coder-Critique 数据集，提供 HuggingFace 数据与模型下载、conda 环境搭建、训练脚本（如 Qwen3-4B-16K 示例）与评测流程（EvalPlus、BigCodeBench、Aider-Polyglot、LiveCodeBench）。面向从事 LLM 代码能力训练与评测的研究者和开发者。

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

- 批判强化学习训练方法（ICLR26 论文）
- 基于 rStar-Coder 过滤构建的 rStar-Coder-Critique 数据集
- 提供 Qwen3-4B 训练示例脚本
- 使用 EvalPlus/BigCodeBench/Aider-Polyglot/LiveCodeBench 评测

## 适用场景

- 复现批判强化学习训练代码模型的实验
- 获取代码批判数据集用于训练
- 对代码模型进行多基准评测

## 场景标签

`强化学习` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Critique-Coder: Training Coder Models with Critique Reinforcement Learning [ICLR26]
> L27: bash examples/train/train_qwen3_4b_16k.sh

## 星数曲线

```mermaid
xychart-beta
    title "TIGER-AI-Lab/Critique-Coder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `7266629bc808` · [字段定义](../../DATASET.md)*
