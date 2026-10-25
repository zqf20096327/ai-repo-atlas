# junkyard22/Orca

⭐ 41 · TypeScript · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/junkyard22/Orca) · 个人维护

**多角色 AI agent 编排运行时，用于编码任务的分解与质检**

TypeScript/Node.js monorepo，面向 Windows 的多角色 AI 编排运行时：Benson 意图解析、Brain 分解任务、专家角色（coder/reviewer/debugger 等）执行、QC 层校验输出。提供 Electron 桌面端（含 Cargo 上下文托盘）与 CLI runner。支持 MCP、SQLite 持久化、自改进蒸馏循环、自定义扩展工具与训练数据导出。LLM 后端可配 OpenRouter 或 Ollama，许可为 PolyForm Noncommercial 1.0.0（禁商用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多角色流水线（意图解析→任务分解→专家执行→QC 校验）
- Electron 桌面端 + CLI runner 两种使用方式
- Ollama 本地模型与 OpenRouter 均可作为后端
- 运行历史导出为训练数据、支持自定义扩展工具

## 适用场景

- 用多角色 agent 流水线完成编码任务并自动质检
- 本地 Ollama 模型离线运行编码助手
- 导出通过质检的运行记录用于微调

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: Orca is a TypeScript/Node.js monorepo for orchestrating multiple AI roles to solve coding tasks. A **brain** role de
> L10:        └── Orca Runtime (orchestration + repair loop)

## 星数曲线

```mermaid
xychart-beta
    title "junkyard22/Orca 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-25 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3fc4b84ab2c3` · [字段定义](../../DATASET.md)*
