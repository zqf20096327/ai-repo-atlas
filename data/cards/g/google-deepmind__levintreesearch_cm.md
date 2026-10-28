# google-deepmind/levintreesearch_cm

⭐ 38 · Racket · Apache-2.0 · 推送 2026-07-15 · [GitHub](https://github.com/google-deepmind/levintreesearch_cm) · 组织维护

**IJCAI 2023 论文复现代码：上下文模型引导的 Levin 树搜索求解器**

DeepMind 发布的 "Levin Tree Search with Context Models" 论文官方代码，用 Racket 语言实现。在 Sokoban、滑块拼图、The Witness、魔方四个规划问题上运行 Levin 树搜索，收集解轨迹并优化策略参数以减少搜索扩展数，支持 server-worker 架构并行。提供图形界面可视化解轨迹与复现论文全部结果的命令。复现结果需每 worker 最多 2GB 内存与每实验 5GB 磁盘，最耗时实验需数天（64 核 2GHz 机器）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Levin 树搜索 + 在线策略参数优化（扩展数随优化减少）
- 覆盖 Sokoban/滑块拼图/The Witness/魔方四个规划域
- server-worker 多核并行架构，日志断点续跑
- 图形界面可视化求解轨迹

## 适用场景

- 复现论文中四个规划问题的实验结果
- 研究上下文模型引导的树搜索算法
- 在自定义规划问题上测试 Levin 树搜索

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Code for the paper "Levin Tree Search with Context Models", published in the IJCAI 2023 proceedings.
> L9: This code allows to reproduce the results of the paper.
> L52: * optimizes the parameters of the policy for these trajectories,

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/levintreesearch_cm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1c4472fac498` · [字段定义](../../DATASET.md)*
