# Constantine-Kostikas/memorable

⭐ 3 · Go · MIT · 推送 2026-11-24 · [GitHub](https://github.com/Constantine-Kostikas/memorable) · [官网](https://constantine-kostikas.github.io/memorable/) · 个人维护

**为 Claude Code 提供本地持久化可检索记忆的 MCP 服务器**

用 Go 编写的本地 MCP 服务器：Claude Code 在工作时把决策、偏好与项目事实保存为记忆，存入 Docker 中带 pgvector 的 Postgres，嵌入由本地 Ollama 生成，全部运行在 127.0.0.1。检索为语义加关键词混合排序，并在会话开始与每次提交提示词时注入相关记忆指针（默认相关度阈值 70%、会话内不重复、1.5 秒超时）。提供 CLI 与 Web UI 用于搜索、审阅、编辑记忆；内置密钥拒绝、提示注入隔离与版本化历史。要求 macOS/Linux、Docker、Ollama 与 Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合语义+关键词检索，提示词时注入带相关度百分比的记忆指针
- 本地运行：Postgres+pgvector（Docker）与 Ollama 嵌入均在 127.0.0.1
- 密钥拒绝、提示注入隔离、每次变更版本化
- CLI 与 Web UI 搜索、审阅、编辑 Claude 保存的记忆

## 适用场景

- 让 Claude Code 跨会话记住项目决策与个人偏好
- 按目录管理隔离的记忆上下文（work/personal）
- 审阅并修正 Claude 自动保存的记忆内容

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: Claude Code forgets everything between sessions, and its built-in memory is Markdown files with no search index. mem
> L12: - **Local:** Postgres with pgvector in Docker and embeddings from Ollama, both on `127.0.0.1`.
> L96: 6. Register the MCP server with Claude Code (`claude mcp add --scope user`).


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `c087b57e3337` · [字段定义](../../DATASET.md)*
