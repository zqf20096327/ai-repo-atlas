# lucidrains/blackbox-gradient-sensing

⭐ 20 · Python · MIT · 推送 2026-04-17 · [GitHub](https://github.com/lucidrains/blackbox-gradient-sensing) · 个人维护

**Google DeepMind 乒乓球论文中 BGS 进化策略的 PyTorch 实现**

实现并探索 Blackbox Gradient Sensing（BGS），一种 Google DeepMind 论文提出的进化策略方法，最初用于乒乓球机器人策略训练。以 Python 库形式提供，支持 mock 环境调用，附 train.py 训练脚本与连续 Lander 示例，可通过 🤗 accelerate 进行分布式训练，并计划引入 EPO 的 latent population 变体。作者注明原论文为 2022 年工作，PPO 已用于人形机器人 sim2real。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- BGS 进化策略的 Python 实现与训练脚本
- 支持 🤗 accelerate 分布式训练
- 计划纳入 EPO 的 latent population 变体
- 提供连续 Lander 示例，ES 在 20 次更新内开始工作

## 适用场景

- 研究生成策略训练的进化策略方法
- 复现并扩展 DeepMind 乒乓球 BGS 论文
- 在连续控制任务上对比 ES 与 PPO 训练效果

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: Implementation and explorations into Blackbox Gradient Sensing (BGS), an evolutionary strategies approach proposed i
> L5: Note: This paper is from 2022, and PPO is now being used for sim2real for humanoid robots (contradicting the author)

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/blackbox-gradient-sensing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0ac3e99155c8` · [字段定义](../../DATASET.md)*
