# yihaosun1124/OfflineRL-Kit

⭐ 393 · Python · MIT · 推送 2026-08-09 · [GitHub](https://github.com/yihaosun1124/OfflineRL-Kit) · 组织维护

**面向科研人员的 PyTorch 离线强化学习算法库**

基于纯 PyTorch 的离线强化学习库，实现 model-free（CQL、TD3+BC、IQL、EDAC、MCQ）与 model-based（MOPO、COMBO、RAMBO、MOBILE）共 9 种算法，提供 D4RL 基准结果（4 seeds，进行中）。以组件化结构组织（策略、回放缓冲、日志、训练器），支持基于 Ray 的并行调参，日志系统输出 txt/csv/tfevents/json 多种格式，并附训练曲线绘图脚本。安装需先装 MuJoCo 引擎、mujoco-py 与 D4RL，再从源码安装本库。

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

- 实现 9 种 offline RL 算法（model-free 与 model-based）
- 组件化结构，可基于库内组件构建新算法
- 支持基于 Ray 的并行调参
- 多格式日志系统与基准结果绘图脚本

## 适用场景

- 复现或运行 offline RL 算法在 D4RL 任务上的实验
- 基于现有组件实现自定义 offline RL 算法
- 科研中进行超参数并行调参与实验管理

## 场景标签

`强化学习` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: OfflineRL-Kit is an offline reinforcement learning library based on pure PyTorch. This library has some features whi
> L8: - State-of-the-art offline RL algorithms, including model-free and model-based approaches

## 星数曲线

```mermaid
xychart-beta
    title "yihaosun1124/OfflineRL-Kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 392 --> 394
    line [393, 393]
```

2026-10-18 393 → 2026-10-30 393（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `a1d12d58c49f` · [字段定义](../../DATASET.md)*
