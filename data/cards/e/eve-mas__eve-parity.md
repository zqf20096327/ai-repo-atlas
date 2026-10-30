# eve-mas/eve-parity

⭐ 21 · Python · GPL-3.0 · 推送 2026-08-31 · [GitHub](https://github.com/eve-mas/eve-parity) · 组织维护

**多智能体博弈时序均衡性质的形式化验证工具**

EVE（Equilibrium Verification Environment）是面向并发与多智能体系统的形式化验证工具：用 SRML 将系统建模为多玩家博弈，玩家目标以 LTL 公式表达，工具检查纳什均衡存在性并支持理性合成与验证（A-Nash、E-Nash、Non-Emptiness 及纯无记忆策略 profile 检查）。LTL 到自动机转换基于 Spot，e/a/n 问题需外部 OCaml 工具 PGSolver。运行于 Linux/macOS（推荐 Conda 环境），Windows 需 WSL，另提供 OVA 虚拟机镜像与 Oxford 网页服务。面向形式化方法与多智能体系统研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SRML 建模多玩家博弈，LTL 表达玩家目标，检查纳什均衡存在性
- 支持 A-Nash/E-Nash/Non-Emptiness 与纯无记忆 profile 检查（问题 m）
- 基于 Spot 的 LTL-to-automaton 转换，e/a/n 问题调用外部 PGSolver
- 提供 OVA 虚拟机镜像与 Oxford 在线服务，附 8 个实验脚本

## 适用场景

- 验证多智能体系统的时序均衡性质
- 检查给定策略 profile 是否为纳什均衡并给出偏离证人策略
- 运行博弈协议（如 gossip、副本控制）的可扩展性实验

## 场景标签

 · 领域:形式化方法/多智能体系统

## 证据(README 行号)

> L4: __EVE__ (Equilibrium Verification Environment) is a formal verification tool for the automated analysis of temporal 
> L12: - J. Gutierrez, M. Najib, G. Perelli, and M. Wooldridge. __Automated Temporal Equilibrium Analysis: Verification an

## 星数曲线

```mermaid
xychart-beta
    title "eve-mas/eve-parity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `df265fdff6ff` · [字段定义](../../DATASET.md)*
