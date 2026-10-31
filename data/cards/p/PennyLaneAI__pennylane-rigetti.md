# PennyLaneAI/pennylane-rigetti

⭐ 46 · Python · BSD-3-Clause · 推送 2026-08-18 · [GitHub](https://github.com/PennyLaneAI/pennylane-rigetti) · [官网](https://docs.pennylane.ai/projects/rigetti) · 组织维护

**PennyLane 的 Rigetti 量子设备接入插件**

面向量子机器学习开发者的 PennyLane 插件：提供 rigetti.numpy_wavefunction、rigetti.wavefunction、rigetti.qvm、rigetti.qpu 四个设备，将 pyQuil 波函数模拟器、量子虚拟机（QVM）与 Rigetti 量子处理单元（QPU）接入 PennyLane 的混合量子-经典计算与自动微分工作流。依赖 Python>=3.10、PennyLane>=0.18.0、pyQuil>=3.0.0；本地运行 Quil 需另装 Forest SDK，使用真实 QPU 需 QCS 账号。限制：仅兼容 PennyLane v0.40 及以下，更新版本需改用 PennyLane-Braket 插件。BSD 3-Clause 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供四个设备接入 pyQVM、pyQuil 模拟器、QVM 与 QPU
- 支持全部核心 qubit PennyLane 操作与可观测量
- 通过 pip 安装，依赖 pyQuil 与 Forest SDK/QCS 运行量子程序

## 适用场景

- 在 PennyLane 中运行 Rigetti 真实量子硬件做电路优化
- 用量子虚拟机（QVM）模拟量子电路训练变分算法
- 量子机器学习研究中混合量子-经典自动微分实验

## 场景标签

 · 领域:量子计算/量子机器学习

## 证据(README 行号)

> L33: The PennyLane Rigetti plugin allows different Rigetti devices to work with
> L50: * Provides four devices to be used with PennyLane: ``rigetti.numpy_wavefunction``,
> L41: `PennyLane <https://pennylane.readthedocs.io>`__ is a cross-platform Python library for quantum machine

## 星数曲线

```mermaid
xychart-beta
    title "PennyLaneAI/pennylane-rigetti 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f5330c80c14c` · [字段定义](../../DATASET.md)*
