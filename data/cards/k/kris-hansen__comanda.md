# kris-hansen/comanda

⭐ 330 · Go · MIT · 推送 2026-10-20 · [GitHub](https://github.com/kris-hansen/comanda) · [官网](https://comanda.sh) · 个人维护

**终端原生的 AI agent 工作流编排运行时，用 YAML 编排编码代理**

面向开发者的 CLI 工具：将英文描述生成为可审查的 YAML 工作流程序，在一个流程中协调 Claude Code、Codex、Gemini CLI、Kimi Code、API 模型与本地模型（Ollama/vLLM/llama.cpp）。核心机制包括带检查点持久化的 agentic loop（可中断/恢复）、基于自有测试与安全检查的质量门禁、Git worktree 隔离并行实现、代码库索引与知识图谱（SQLite FTS5 语义记忆），并可将工作流以 HTTP 端点或 MCP 服务暴露。MIT 许可，Go 编写，提供 brew/go 安装与三平台预编译二进制。

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

- 英文描述生成可版本化审查的 YAML 工作流
- agentic loop 持久化状态、检查点恢复、质量门禁定义完成条件
- 代码库索引与确定性知识图谱（含 PostgreSQL DDL 自动建图）
- 工作流可作为 HTTP 端点或 MCP 工具/提示暴露

## 适用场景

- 在仓库内编排多个编码代理协同完成特性实现与审查
- 让长时运行的 agent 循环在测试与安全检查通过后才停止
- 把代码库结构做成可导航的知识图谱与 agent 上下文
- 将签入的工作流接入 CI 或 MCP 客户端复用

## 场景标签

`编码 Agent` `知识图谱` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: > Comanda is the terminal-native runtime for durable, self-improving agent work in a repository. Describe a workflow
> L52: Coordinate Claude Code, Gemini CLI, OpenAI Codex, Kimi Code, API models, and local models in one workflow. Give age
> L121: - Call OpenAI, Anthropic, Google, xAI, DeepSeek, Moonshot, Sakana, Ollama, vLLM, llama.cpp, and compatible provide

## 星数曲线

```mermaid
xychart-beta
    title "kris-hansen/comanda 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 329 --> 331
    line [330, 330]
```

2026-10-18 330 → 2026-10-22 330（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fef6f06af44d` · [字段定义](../../DATASET.md)*
