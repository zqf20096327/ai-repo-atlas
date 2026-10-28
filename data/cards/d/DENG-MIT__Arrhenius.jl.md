# DENG-MIT/Arrhenius.jl

⭐ 61 · Julia · MIT · 推送 2026-10-19 · [GitHub](https://github.com/DENG-MIT/Arrhenius.jl) · [官网](https://deng-mit.github.io/Arrhenius.jl/dev/) · 组织维护

**可微分反应流与燃烧模拟的 Julia 软件包**

面向反应流与燃烧计算的 Julia 软件包：提供原生化学、热力学、输运、零维反应器与一维火焰求解器（自由传播、驻定、对撞流、催化、电离火焰等），直接读取气相 Cantera YAML 机理文件，可选 sidecar 提供拟合输运数据。计算组件可微分，ODE 积分器由调用方选择，可用于机器学习相关的可微分仿真场景。通过 Julia 包管理器安装，附论文引用与 MIT 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零维反应器与反应器网络、多种一维火焰求解器
- 直接读取 Cantera YAML 机理，可选 sidecar 拟合输运数据
- Julia 原生可微分计算组件，调用方自选 ODE 积分器
- 覆盖表面化学、等离子体、多孔输运与真实气体模型

## 适用场景

- 开展燃烧与反应流的机理仿真和火焰计算
- 在可微分仿真流程中接入燃烧物理模型
- 复用 Cantera 机理文件进行反应器模拟

## 场景标签

 · 领域:科学计算/燃烧与反应流

## 证据(README 行号)

> L3: Arrhenius.jl is a Julia package for reacting-flow and combustion calculations. It provides native chemistry, thermod
> L12: - Julia-native calculations with differentiable components and caller-selected ODE integrators

## 星数曲线

```mermaid
xychart-beta
    title "DENG-MIT/Arrhenius.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-28 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `050c483dc19d` · [字段定义](../../DATASET.md)*
