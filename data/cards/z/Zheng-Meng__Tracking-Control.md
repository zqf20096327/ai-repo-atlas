# Zheng-Meng/Tracking-Control

⭐ 34 · MATLAB · MIT · 推送 2025-11-24 · [GitHub](https://github.com/Zheng-Meng/Tracking-Control) · 个人维护

**MATLAB 代码：机器学习实现复杂动力系统轨迹的无模型跟踪控制**

Nature Communications 论文（Zhai 等 2023）的配套代码，实现基于机器学习（储备池计算方向，涉及 echo state networks）的无模型跟踪控制，可跟踪混沌系统（如 Lorenz）与周期轨迹。使用方式为 MATLAB 运行 main.m 并切换 traj_type 参数；需自行从 Zenodo 下载混沌轨迹数据集放入 read_data 文件夹，周期轨迹由代码生成；另需通过 MATLAB Add-Ons 安装内置包 matsplit。面向科研复现者。

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

- 提供 main.m 运行入口，traj_type 可切换 circle/lorenz 等轨迹类型
- 混沌轨迹数据集托管于 Zenodo（DOI: 10.5281/zenodo.8044994）
- 依赖 MATLAB 内置包 matsplit（经 Add-Ons 安装）
- 对应论文发表于 Nature Communications

## 适用场景

- 复现论文中的无模型轨迹跟踪控制结果
- 研究储备池计算/回声状态网络在混沌系统控制中的应用
- 基于示例改写以跟踪其他动力系统轨迹

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4: Model-free tracking control of complex dynamical trajectories with machine learning has been published in Nature Com
> L13: Run 'main.m' with traj_type = 'circle', you will get the ground truth and tracked trajectories in the picture bello

## 星数曲线

```mermaid
xychart-beta
    title "Zheng-Meng/Tracking-Control 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `04f5624589a0` · [字段定义](../../DATASET.md)*
