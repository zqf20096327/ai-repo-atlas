# Qwen-Applications/STAR

⭐ 66 · Python · Apache-2.0 · 推送 2026-04-23 · [GitHub](https://github.com/Qwen-Applications/STAR) · 组织维护 · 中文 README

**把 LLM 函数调用能力蒸馏到超小模型的训练框架**

ICLR 2026 论文的官方代码库：STAR 框架通过两阶段课程将大模型的函数调用能力迁移到超小模型（如 0.6B）。第一阶段用受约束知识蒸馏（CKD）将教师模型知识转移到学生模型，第二阶段用相似度引导强化学习（Sim-RL）进一步提升泛化能力。面向复现实验的研究者，基于打补丁的 OpenRLHF 与 Ray 训练，提供教师 rollout 生成、数据准备脚本（XLAM/ToolMind/ToolAce/Hammer 数据集）与两阶段训练脚本。训练依赖 8 GPU 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两阶段训练课程：CKD 知识蒸馏 + Sim-RL 强化学习
- 教师 rollout 生成合成轨迹与推理链训练数据
- 提供 scripts/prepare_rl_data.sh 自动下载预处理 4 个数据集
- 基于打补丁的 OpenRLHF 框架实现

## 适用场景

- 复现论文中 STAR 超小函数调用模型的训练实验
- 把 8B 教师模型的函数调用能力蒸馏到 0.6B 学生模型
- 准备函数调用 RL 训练数据集

## 场景标签

`强化学习` `微调` · 领域:训练与推理

## 证据(README 行号)

> L12: This repository contains the code and instructions necessary to reproduce the experiments presented in the paper: *
> L14: **STAR (Similarity-guided Teacher-Assisted Refinement)** is a novel holistic framework designed to effectively tran
> L15: 1. **Constrained Knowledge Distillation (CKD):** The selected teacher's knowledge is transferred to a super-tiny st
> L16: 2. **Similarity-guided Reinforcement Learning (Sim-RL):** The distilled student model is polished with **Sim-RL** t

## 星数曲线

```mermaid
xychart-beta
    title "Qwen-Applications/STAR 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-27 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ed314da531c1` · [字段定义](../../DATASET.md)*
