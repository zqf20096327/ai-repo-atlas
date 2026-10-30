# lucidrains/x-evolution

⭐ 53 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/lucidrains/x-evolution) · 个人维护

**PyTorch 进化算法库：进化策略训练与分布式运行**

由 lucidrains 实现的进化算法库，首个算法为进化策略（EvoStrategy）。以 Python 库形式提供，基于 PyTorch，支持通过 HuggingFace accelerate CLI 或 torchrun 进行多进程 CPU 分布式训练；附带 LunarLander 快速演示与 Microduck 双足机器人 sim-to-real 步态训练脚本（CPG 控制、命令条件化、checkpoint 恢复与评估视频渲染）。README 引用多篇进化策略相关论文作为算法出处。

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

- 进化策略（EvoStrategy）的 PyTorch 实现
- 支持 accelerate 与 torchrun 多进程 CPU 分布式训练
- 提供 LunarLander 与 Microduck 双足机器人 sim-to-real 训练示例

## 适用场景

- 用进化策略替代反向传播/强化学习训练策略
- 在多核 CPU 上并行运行进化策略训练
- 训练双足机器人步态并导出评估视频

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: Implementation of various evolutionary algorithms, starting with evolutionary strategies
> L16: import torch

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/x-evolution 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-30 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3d4bba84640a` · [字段定义](../../DATASET.md)*
