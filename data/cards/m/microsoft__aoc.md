# microsoft/aoc

⭐ 45 · Python · MIT · 推送 2025-12-14 · [GitHub](https://github.com/microsoft/aoc) · 组织维护

**微软模拟-光学模拟计算加速器的数字孪生仿真库**

Microsoft Research AOC（Analog-Optical Computer）项目的数字孪生代码，用于在普通计算设备上模拟模拟-光学硬件的物理行为（含各类非理想效应），以便在数字环境中训练定点模型（DEQ、Hopfield 等），使其能在实际 AOC 设备（2300 权重或 256 权重机型）上正确评估。核心为 AOCCell 类，支持多种结构化矩阵与两种硬件代际配置，另提供理想化的 SimpleCell。面向从事新型 AI 硬件与定点模型研究的科研人员，以 pip 包形式提供。

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

- AOCCell 类对模拟-光学器件物理与非理想效应进行建模
- 支持 DEQ / Feedforward / Hopfield 三种矩阵连接结构
- HardwareParameters16/48 对应两代 AOC 硬件配置（yaml）
- 提供 DEQInputOutputProjection 工厂方法快速构建模型

## 适用场景

- 在实际 AOC 设备上部署前，先在数字孪生中训练定点模型
- 研究非理想效应对模拟计算结果的影响
- 实验 2300 权重或 256 权重机型的模型结构配置

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: This repo contains the code for the Digital Twin (DT) used in Microsoft Research's AOC project.
> L19: However, various non-idealities perturb the computation in the AOC device away from the equation above, creating th
> L26: The core of the digital twin is the `AOCCell` class which attempts to model the physics of the analog-optical devic

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/aoc 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 43 --> 46
    line [44, 45, 45]
```

2026-10-18 44 → 2026-10-27 45（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `be6d59274735` · [字段定义](../../DATASET.md)*
