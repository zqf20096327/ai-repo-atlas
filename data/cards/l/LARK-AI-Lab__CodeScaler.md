# LARK-AI-Lab/CodeScaler

⭐ 51 · Python · 推送 2026-09-27 · [GitHub](https://github.com/LARK-AI-Lab/CodeScaler) · [官网](https://lark-ai-lab.github.io/codescaler.github.io/) · 组织维护

**免执行的代码奖励模型：用于代码 LLM 的 RL 训练与测试时推理扩展**

NeurIPS 2026 论文的官方仓库，发布 CodeScaler 免执行奖励模型（1.7B/4B/8B 三个规模）及 CodeScalerPair-51K 偏好数据集。模型基于 Skywork-Reward-V2-Qwen3 系列在已验证代码问题上训练，采用语法感知代码提取与保有效性奖励塑形，用于代码生成的强化学习训练和测试时推理打分。仓库提供环境搭建、数据准备、训练与评测脚本，以及用 transformers 加载模型打分的用法示例；训练基于 DeepCoder 数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1.7B/4B/8B 三个规模的免执行代码奖励模型
- CodeScalerPair-51K 偏好数据集
- 支持 RL 训练与测试时推理两类用法
- 提供 transformers 直接加载进行 RM 打分的示例

## 适用场景

- 用奖励模型替代单元测试为代码生成做强化学习训练
- 测试时对多个候选代码方案打分选优
- 复现论文的模型训练与基准评测流程

## 场景标签

`强化学习` `模型评测` `微调` · 领域:评测与运维

## 证据(README 行号)

> L37: - We propose **CodeScaler**, an execution-free reward model designed to scale both reinforcement learning training 
> L134: ### 💻 Use CodeScaler for RM Scoring

## 星数曲线

```mermaid
xychart-beta
    title "LARK-AI-Lab/CodeScaler 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-10-18 50 → 2026-10-26 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7d263b0a6d75` · [字段定义](../../DATASET.md)*
