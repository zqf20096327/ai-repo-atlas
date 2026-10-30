# Trae1ounG/Pretrain_Space_RLVR

⭐ 20 · Python · MIT · 推送 2026-04-16 · [GitHub](https://github.com/Trae1ounG/Pretrain_Space_RLVR) · 组织维护

**论文代码：DSRL 双空间 RL 训练，预训练空间负样本强化热身后转标准 RL**

NeurIPS 2026 Pre-to-Post 投稿论文《From P(y|x) to P(y)》的官方实现：DSRL 将预训练空间的负样本强化（NSR-PreRL）与标准后训练空间 RL 通过 Policy Reincarnation 策略结合——先用仅负样本、仅预训练损失的 warmup 剪除错误推理路径，再切换到标准 RL（如 GRPO）做细粒度优化。提供 Qwen3-4B 的基线与 DSRL 训练脚本、关键超参数表及四种消融变体。面向复现论文或开展 LLM 强化学习研究的科研人员，需从源码安装（conda + pip install -e .，含 flash-attn）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- NSR-PreRL warmup：仅负样本参与预训练损失，warmup 期间关闭 RL 损失
- 提供 GRPO 基线与完整 DSRL 双空间训练流水线脚本
- 四种消融变体（NSR/PSR-Pretrain、NSR/PSR-RL）可在脚本中切换
- warmup 步数等关键参数附默认值与推荐范围

## 适用场景

- 复现论文中的 DSRL 双空间 RL 训练实验
- 在 Qwen3-4B 上对比预训练空间 RL 与标准 GRPO
- 研究正/负样本与预训练/RL 损失组合的消融影响

## 场景标签

`强化学习` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: DSRL combines Negative Sample Reinforcement in the Pre-train Space (NSR-PreRL) with standard Post-train Space RL via
> L29: **DSRL:** Complete Dual Space RL pipeline: NSR-PreRL warmup for N steps (negative samples only, pre-train loss only

## 星数曲线

```mermaid
xychart-beta
    title "Trae1ounG/Pretrain_Space_RLVR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `de683881faa6` · [字段定义](../../DATASET.md)*
