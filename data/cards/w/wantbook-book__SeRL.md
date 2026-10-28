# wantbook-book/SeRL

⭐ 26 · Python · Apache-2.0 · 推送 2026-01-24 · [GitHub](https://github.com/wantbook-book/SeRL) · 组织维护

**论文官方代码库：少量数据下用自我博弈强化学习训练 LLM 推理**

SeRL 论文的官方训练代码库，基于 OpenRLHF 框架实现，评测基于 Qwen2.5-Math、Math-Verify 与 MMLU-Pro。方法由两个模块组成：self-instruction 在每步基于现有数据生成新指令并做在线过滤（质量/多样性/难度），self-rewarding 用多数投票机制估计奖励，免除外部标注，随后执行常规 RL 迭代自博弈。支持 Reinforce++、GRPO、RLOO 三种算法脚本模板，提供数学基准与 MMLU-Pro 的 Pass@1/Maj@K 评测脚本。实验配置示例为 8×A6000(48GB) GPU，代码以 Apache-2.0 许可发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- self-instruction 在线过滤指令生成（质量/多样性/难度）
- 多数投票奖励机制，无需外部标注与可验证奖励
- 支持 Reinforce++/GRPO/RLOO 三种训练算法模板
- 内置 10 个数学基准数据集与 MMLU-Pro 评测脚本

## 适用场景

- 在缺乏高质量指令与可验证奖励的领域对 LLM 做 RL 训练
- 复现论文中 LLaMA-3.2-3B 与 Qwen-2.5-7B 的训练结果
- 对数学推理与 MMLU-Pro 基准做 Pass@1/Maj@K 评测

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L4: 📄 **"SeRL: Self-Play Reinforcement Learning for Large Language Models with Limited Data"**. This training code is ba
> L8: **Abstract:** Recent advances have demonstrated the effectiveness of Reinforcement Learning (RL) in improving the re
> L14: - Finally, SeRL performs conventional RL based on the generated data, facilitating iterative self-play learning.

## 星数曲线

```mermaid
xychart-beta
    title "wantbook-book/SeRL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e405168efccc` · [字段定义](../../DATASET.md)*
