# sunblaze-ucb/FedAgent

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/sunblaze-ucb/FedAgent) · [官网](https://fed-agent.github.io) · 组织维护

**面向研究者的 LLM agent 联邦强化学习训练库（verl 之上的轻量覆盖层）**

FedAgent 是用于 LLM agent 联邦强化学习训练的 Python 库：在 verl 0.8 之上以薄覆盖层形式实现 FedAvg 聚合（可选 FedProx）、联邦 PPO/GRPO 训练器与两级异质性套件（任务级 vs 环境级），本地数据不出客户端。内置 WebShop 与 ALFWorld 基准、194 配置的论文复现矩阵、单卡 H100 与加速版本，支持任意 HuggingFace 骨干模型与 Harbor 任务环境。安装需三个 conda 环境（训练器/WebShop/ALFWorld 依赖互斥，经 HTTP 通信），WebShop 环境需 JDK。面向开展联邦 agent RL 研究的科研用户，为 NeurIPS 2026 论文的参考实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 联邦 GRPO/PPO 训练器，FedAvg 聚合 + 可选客户端侧 FedProx
- 两级异质性套件：任务级（Preference/Coverage/Hardness）与环境级划分
- 194 配置论文矩阵，含 ×2.5–×3.5 加速版与单 H100 版本
- 内置 WebShop/ALFWorld 基准（经 per-client HTTP env 服务隔离依赖）与 Harbor 任务环境支持

## 适用场景

- 复现论文的联邦 LLM agent RL 实验矩阵
- 研究数据不出本地的多方协作 agent 训练
- 在自有数据集/环境/聚合规则上扩展联邦训练实验

## 场景标签

`科研工具` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L55: FedAgent is a library for **federated RL training of LLM agents**. It implements a
> L58: and federated **PPO/GRPO** trainers, built as a **thin overlay on stock
> L59: verl 0.8** (no trainer fork: verl is imported as a

## 星数曲线

```mermaid
xychart-beta
    title "sunblaze-ucb/FedAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `595799a9235b` · [字段定义](../../DATASET.md)*
