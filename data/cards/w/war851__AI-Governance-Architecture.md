# war851/AI-Governance-Architecture

⭐ 56 · NOASSERTION · 推送 2026-07-22 · [GitHub](https://github.com/war851/AI-Governance-Architecture) · [官网](https://toldi.io) · 个人维护

**数据库治理的 LLM 应用架构模式与 Claude Code 配置工作区**

将 Claude Code 的配置模型（CLAUDE.md 级联、Skills、Hooks 等）转化为数据库治理应用模式的参考仓库：数据库持有步骤、函数、技能与审计日志，LLM 作为无状态语义引擎。含 6 条架构原则、4 个设计技能（价值链映射、数据演化、TDD 黄金样例、治理架构，共 17 种制品类型）、JD 解析实现示例、可运行的 Governed Agent，以及可克隆复用的 Claude Code/Cursor 配置。方法论以 CC BY-NC 4.0 提供，商用需另行许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude Code 概念到 DB 治理应用的映射表（12 项对应关系）
- 6 条治理原则：DB 拥有流程、LLM-agnostic、全量存储可审计
- 4 个设计技能产出 17 种带 YAML 信封与生命周期的制品
- 含 JD Parsing 示例与可运行的 Governed Agent

## 适用场景

- 设计可审计、GDPR/EU AI Act 合规的 LLM 应用架构
- 复用 Claude Code + Cursor 的工程配置与规范
- 按技能化流程从需求访谈推进到治理架构设计

## 场景标签

 · 领域:AI 架构/治理

## 证据(README 行号)

> L33: 1. **DB owns the process, LLM is the semantic engine.** The database defines every step, message, function, and ski
> L66: For the same primitives in a small runnable agent (steps, orchestration, a constrained LLM, hash-chained logs) appl

## 星数曲线

```mermaid
xychart-beta
    title "war851/AI-Governance-Architecture 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-28 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e51c29b969d6` · [字段定义](../../DATASET.md)*
