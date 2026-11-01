# ipiton/agent-memory-mcp

⭐ 44 · Go · MIT · 推送 2026-10-22 · [GitHub](https://github.com/ipiton/agent-memory-mcp) · 个人维护

**给工程 agent 的持久记忆与项目文档上下文 MCP 服务器**

面向工程团队（DevOps/平台/基础设施）的 MCP server，为 Claude、Cursor、Codex 等 MCP 客户端提供持久记忆层：4 种类型化记忆（episodic/semantic/procedural/working）、项目文档 RAG 索引、仓库感知文件工具、SQLite 存储。检索采用嵌入+BM25 混合排序，附带知识维护机制（去重、冲突解决、过期检测、时间线）。支持 stdio 与 HTTP/JSON-RPC 双传输，嵌入可用 Jina/OpenAI 托管或 Ollama/llama.cpp 本地后端；通过 Homebrew 或 go install 安装，提供 Docker Compose 共享部署方案。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 种类型化持久记忆与混合检索（嵌入+BM25）
- 项目文档 RAG 索引与仓库感知文件工具，SQLite 单存储
- 知识维护：去重、冲突解决、时间线与可信度感知检索
- 双传输（stdio/HTTP）与本地嵌入模式（Ollama/llama.cpp）

## 适用场景

- 让 AI agent 跨会话记住工程决策、事故与 runbook
- 对仓库文档做 RAG 索引供 agent 检索
- 团队以共享服务形式部署统一记忆层

## 场景标签

`Agent 记忆` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L7: `agent-memory-mcp` helps agents work with live engineering context, not just isolated notes. It combines typed memor
> L50: - **Dual transport**: stdio for MCP clients, HTTP/JSON-RPC for APIs and shared setups


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `549c8769293b` · [字段定义](../../DATASET.md)*
