# PennyLaneAI/pennylane-cirq

⭐ 65 · Python · Apache-2.0 · 推送 2026-07-08 · [GitHub](https://github.com/PennyLaneAI/pennylane-cirq) · [官网](https://docs.pennylane.ai/projects/cirq) · 组织维护

**将 Google Cirq 量子框架接入 PennyLane 的插件**

连接 Cirq 量子计算框架与 PennyLane 量子机器学习能力、自动微分与混合量子-经典计算优化功能的插件。为 PennyLane 提供 Cirq 内置后端（cirq.simulator、cirq.mixedsimulator）、Pasqal 中性原子设备通道（cirq.pasqal）以及 qsim/qsimh 模拟器设备，并支持 PennyLane 核心功能。要求 Python 3.11 以上及 PennyLane>=0.29、Cirq>=0.10.0；qsim 设备需另装 qsimcirq。Apache 2.0 许可，由 PennyLaneAI（Xanadu）团队维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接入 Cirq 内置模拟器后端 cirq.simulator / cirq.mixedsimulator
- 通过 cirq.pasqal 提供 Pasqal 中性原子设备通道
- 提供 qsim / qsimh 模拟器设备（需 qsimcirq）
- 支持全部 PennyLane 核心功能

## 适用场景

- 在 PennyLane 工作流中使用 Cirq 模拟器运行量子电路
- 将量子机器学习模型指向 qsim 模拟器或 Pasqal 设备做验证
- 在 PennyLane 中对 Cirq 电路做自动微分与优化

## 场景标签

 · 领域:量子计算/量子机器学习

## 证据(README 行号)

> L32: The PennyLane-Cirq plugin integrates the Cirq quantum computing framework with PennyLane's
> L35: `PennyLane <https://pennylane.readthedocs.io>`__ is a cross-platform Python library for quantum machine
> L46: * Provides access to built-in Cirq backends including ``cirq.simulator`` and ``cirq.mixedsimulator``

## 星数曲线

```mermaid
xychart-beta
    title "PennyLaneAI/pennylane-cirq 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-26 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4d5cff2a27ad` · [字段定义](../../DATASET.md)*
