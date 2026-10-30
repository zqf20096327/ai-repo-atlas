# asystemoffields/disco-torch

⭐ 15 · Python · Apache-2.0 · 推送 2026-09-03 · [GitHub](https://github.com/asystemoffields/disco-torch) · 个人维护

**DeepMind Disco103 元学习 RL 更新规则的 PyTorch 移植库**

将 DeepMind 在 Nature 2025 论文中提出的元学习强化学习更新规则 Disco103 从 JAX 移植到 PyTorch：用 754K 参数的小型神经网络替代手工设计的 RL 损失函数（如 PPO/GRPO），输入 agent 经验并输出损失目标，agent 通过最小化对目标的 KL 散度训练。提供 DiscoTrainer 高层 API（自动管理 meta 状态、目标网络、replay buffer、优化器）与低层 DiscoUpdateRule，作者报告在 Catch 基准上达到 100% catch rate。要求 Python>=3.11、PyTorch>=2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 754K 参数神经网络替代手工 RL 损失函数，作为即插即用更新规则
- DiscoTrainer 自动处理 meta 状态、目标网络、replay buffer 与损失计算
- 提供低层 DiscoUpdateRule API 与参考 agent 架构示例
- 可选 extras：HuggingFace Hub 权重下载、pytest 开发环境

## 适用场景

- 在 PyTorch 项目中用 DiscoTrainer 训练 RL agent
- 复现并研究元学习 RL 更新规则的训练细节
- 与 A2C 基线对比验证 Disco103 的训练效果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: A PyTorch port of DeepMind's **Disco103** — the meta-learned reinforcement learning update rule from *Discovering St
> L5: Disco103 is a small neural network (754K params) that **replaces hand-crafted RL loss functions**. Instead of PPO or

## 星数曲线

```mermaid
xychart-beta
    title "asystemoffields/disco-torch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `27fc4f4bc590` · [字段定义](../../DATASET.md)*
