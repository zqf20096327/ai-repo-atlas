# repotracer/repotracer

⭐ 38 · Rust · MIT · 推送 2026-10-08 · [GitHub](https://github.com/repotracer/repotracer) · [官网](https://repotracer.tech) · 组织维护

**为 Claude Code / Codex 分流代码库调查的 MCP 服务器**

用 Rust 编写的 MCP 服务器：在独立会话中运行调查 agent，将代码库调查报告回传给 Claude Code 或 Codex，以减少主编码会话的 token 消耗；通过单一 MCP 工具 repo_scout 供编码 agent 调用，支持调查续接与并行。调查后端可使用已登录的原生 CLI，也可接入任意 OpenAI 兼容端点（含 Ollama/vLLM），由 RepoTracer 自行驱动调查。安装经 npx setup 或 npm/cargo，另提供 CLI 的 scout/symbols 等命令；受 FastContext 论文启发但与 Microsoft 无关联。

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

- 独立会话执行代码库调查，报告回传 Claude Code / Codex
- 单一 MCP 工具 repo_scout，调查可续接不重复开始
- 支持任意 OpenAI 兼容端点（含 Ollama / vLLM）作为调查后端
- Rust 实现，另带 CLI（serve / scout / symbols 等本地命令）

## 适用场景

- 让 Claude Code / Codex 在固定限额内完成更多任务
- 把大型代码库的行为追踪、调用链排查交给独立调查 agent
- 用本地 Ollama / vLLM 模型承担调查工作以降低成本

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L137: RepoTracer is a Rust MCP server. Native investigations run through the Claude Code or Codex CLI you already use. F
> L5:  RepoTracer has a separate agent investigate the repo and report back to Claude Code or Codex.

## 星数曲线

```mermaid
xychart-beta
    title "repotracer/repotracer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `502515141566` · [字段定义](../../DATASET.md)*
