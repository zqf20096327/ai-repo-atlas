# kris-hansen/comanda

⭐ 333 · Go · MIT · 推送 2026-11-26 · [GitHub](https://github.com/kris-hansen/comanda) · [官网](https://comanda.sh) · 个人维护

**终端原生的 AI coding agent 工作流编排器**

Comanda 以声明式 YAML 程序编排既有 coding agent CLI（Claude Code、Gemini CLI、Codex、Kimi Code）与 API/本地模型，通过 comanda generate 从自然语言生成工作流，支持带检查点恢复的 agentic loop、质量门、重试/中止/跳过策略、多 agent 并行与 Git worktree 隔离。附代码库索引、SQLite FTS5 语义记忆、知识图谱构建与 localhost 可视化浏览，可经 MCP、HTTP、shell 管道运行。MIT 许可，Go 实现，提供 brew/go install 与预编译二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agentic loop 支持持久化状态、检查点恢复与质量门
- 统一编排 Claude Code/Gemini CLI/Codex/Kimi Code 及 API/本地模型
- 代码库索引可转为知识图谱并提供 localhost-only 可视化
- 工作流可作为 MCP 工具、HTTP 端点或 shell 管道环节运行

## 适用场景

- 让 coding agent 迭代执行任务直到测试与安全检查通过
- 多个 agent 以不同角色并行评审代码变更
- 把既有 agent 工作流以声明式文件纳入版本管理与 CI

## 场景标签

`多智能体` `编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: > Comanda is the terminal-native runtime for durable, self-improving agent work in a repository. Describe a workflow
> L109: Comanda sits between a coding agent and an agent framework: it turns agent work into a durable, reviewable program

## 星数曲线

```mermaid
xychart-beta
    title "kris-hansen/comanda 星数(近 9 点)"
    x-axis ["2026-10-25", "2026-10-28", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-21", "2026-11-27"]
    y-axis "stars" 328 --> 335
    line [329, 331, 332, 329, 332, 333, 334, 333, 333]
```

2026-10-25 329 → 2026-11-27 333（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `a93b8324ad8f` · [字段定义](../../DATASET.md)*
