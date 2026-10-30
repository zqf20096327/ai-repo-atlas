# lucidrains/streaming-deep-rl

⭐ 32 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/lucidrains/streaming-deep-rl) · 个人维护

**流式深度强化学习算法的 PyTorch 实现库，面向持续学习场景**

University of Alberta 提出的 Streaming Deep Reinforcement Learning 方法的探索性实现库，以 Python/PyTorch 包形式提供，pip 可安装。核心提供 Streaming AC(λ) 等流式（在线、单样本更新）深度强化学习算法，附 Cartpole 与 Lunar Lander 训练脚本（通过 uv run 执行）。README 引用了 Streaming Deep RL 论文（Elsayed 2024）及多项相关研究（正则化、可塑性维持、表征学习等）。文档极简，未说明支持的完整算法列表与硬件要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Streaming AC(λ) 等流式深度强化学习算法实现
- pip 安装的 Python 库，基于 PyTorch
- 附 Cartpole 与 Lunar Lander 训练脚本

## 适用场景

- 研究者复现流式深度强化学习算法
- 在 Cartpole/Lunar Lander 等环境上做流式 RL 实验
- 持续学习/在线强化学习方法探索

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L5: Explorations into the proposed Streaming Deep Reinforcement Learning, from University of Alberta.
> L24: from streaming_deep_rl import StreamingACLambda

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/streaming-deep-rl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `89fdd86bb2cb` · [字段定义](../../DATASET.md)*
