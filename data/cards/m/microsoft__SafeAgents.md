# microsoft/SafeAgents

⭐ 15 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/microsoft/SafeAgents) · 组织维护

**构建与评测安全多智能体系统的统一框架**

SafeAgents（又称 SafeAgentEval）提供框架无关的 API 用于创建多智能体系统，代码写一次即可在 Autogen、LangGraph、OpenAI Agents 上运行，支持集中式/去中心式架构。内置安全能力：攻击检测（工具调用监控、Bash 命令跟踪、日志模式匹配、自定义检测逻辑）与安全评估指标（ARIA、DHARMA）。支持在 AgentHarm、ASB 基准上运行并带断点续跑，另提供网页浏览、文件操作、代码执行的预置智能体。通过 git clone 源码安装，MIT 许可，由 Microsoft 维护。

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

- 一套 API 跨 Autogen / LangGraph / OpenAI Agents 运行
- 攻击检测：工具调用监控、Bash 命令跟踪、日志模式匹配
- ARIA / DHARMA 安全评估指标，检测到攻击自动赋 ARIA=4
- 支持 AgentHarm / ASB 基准，长实验可断点续跑

## 适用场景

- 用统一 API 编写多智能体系统并随时切换底层框架
- 在 AgentHarm / ASB 安全基准上评测智能体行为
- 运行时检测危险工具调用等恶意行为

## 场景标签

`Agent 框架` `多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **A unified framework for building and evaluating safe multi-agent systems**
> L5: SafeAgents provides a simple, framework-agnostic API for creating multi-agent systems with built-in safety evaluatio

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/SafeAgents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0e4da4201720` · [字段定义](../../DATASET.md)*
