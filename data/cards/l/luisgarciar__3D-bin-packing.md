# luisgarciar/3D-bin-packing

⭐ 69 · Jupyter Notebook · MIT · 推送 2026-07-07 · [GitHub](https://github.com/luisgarciar/3D-bin-packing) · 个人维护

**用强化学习求解三维装箱问题的 Gymnasium 环境**

提供兼容 Gymnasium API 的三维装箱（3D bin packing）强化学习环境：给定不同尺寸的箱体列表与固定尺寸容器，目标是装箱尽量多的箱子并最小化空余体积（假设不可旋转）。实例由 Ranked Reward 论文中的算法生成；packing_kernel 模块实现 Container/Box 对象，附带 First Fit Decreasing 启发式与 Maskable PPO 训练示例 notebook、单元测试与 MkDocs 文档。通过 git clone 源码 + uv 安装运行，推荐 Python 3.12。限制：不支持箱体旋转（自定义需改模块）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gymnasium API 兼容的 3D 装箱 RL 环境
- 基于 Ranked Reward 论文算法生成问题实例
- 提供 First Fit Decreasing 启发式与 Maskable PPO 训练 demo notebook
- 策略 rollout 可保存为 .gif 文件

## 适用场景

- 研究组合优化问题的强化学习方法
- 训练和评测装箱策略（如 Maskable PPO）
- 对比 RL 与启发式算法在装箱问题上的表现

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains an environment compatible with Gymnasium's API to solve the
> L4: 3D bin packing problem with reinforcement learning (RL).

## 星数曲线

```mermaid
xychart-beta
    title "luisgarciar/3D-bin-packing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-26 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1b79f2efaf13` · [字段定义](../../DATASET.md)*
