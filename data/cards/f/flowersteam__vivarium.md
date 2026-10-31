# flowersteam/vivarium

⭐ 33 · Jupyter Notebook · MIT · 推送 2026-04-11 · [GitHub](https://github.com/flowersteam/vivarium) · 组织维护

**基于 Jax 的多智能体模拟框架，面向 AI/人工生命研究与教学**

Vivarium 是用 Jax 构建和运行多智能体模拟的框架：智能体配备两个马达与两个传感器（受 Braitenberg Vehicles 启发），在由 Jax-MD 驱动的 2D 刚体物理环境中运行。提供预定义与自定义场景（Hydra YAML 配置）、Web 界面实时交互、Jupyter 编程控制三种使用方式，服务器与客户端通过 gRPC 通信。附带教程与六节教学 Notebook。项目自述为 alpha 状态，v0.2 预计 2026 年初发布；需 Python 3.10-3.12，从源码克隆安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 Jax/Jax-MD 的 2D 刚体物理多智能体模拟
- 服务器运行、Web 界面交互、Jupyter 编程控制三种使用方式
- Hydra YAML 场景文件自定义模拟初始参数
- 提供教程与六节教学 Notebook，覆盖行为分配、环境控制与数据记录

## 适用场景

- AI/ALife 课程中教学多智能体模拟基础概念
- 构建生态演化类多智能体实验环境
- 在 Notebook 中编程控制并记录分析模拟数据

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **Vivarium** is framework for for building and running multi-agents simulations using Jax. It allows you to design s
> L98: We offer a series of educational Jupyter Notebooks designed to teach the fundamentals of multi-agent simulation. Th

## 星数曲线

```mermaid
xychart-beta
    title "flowersteam/vivarium 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `91428d51adfb` · [字段定义](../../DATASET.md)*
