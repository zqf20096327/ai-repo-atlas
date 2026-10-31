# nano-step/nano-brain

⭐ 13 · Go · MIT · 推送 2026-09-07 · [GitHub](https://github.com/nano-step/nano-brain) · 组织维护

**面向 AI 编码 agent 的持久记忆与代码智能 MCP 服务器**

自托管的 Go 单二进制服务，通过 MCP 协议向 AI 编码 agent（Claude Code、OpenCode、Cursor 等）提供 18 个工具：跨会话持久记忆（自动收割 OpenCode/Claude Code 会话并做 LLM 摘要）、混合检索（BM25 + pgvector + RRF + 时间衰减）、符号查找、调用链追踪、HTTP 路由流程与变更影响分析。部署依赖 PostgreSQL 17 + pgvector，可用 Docker 或远程数据库；向量嵌入默认走 Ollama 或任意 OpenAI 兼容服务。提供一行安装脚本、交互式初始化向导和 REST API。

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

- 18 个 MCP 工具覆盖记忆、检索与代码智能
- 混合检索：BM25 全文 + pgvector HNSW 余弦 + RRF + 时间衰减
- 代码图与调用链/影响面分析，支持多语言（含 Ruby/Rails 路由）
- 自动收割 OpenCode 与 Claude Code 会话并做 map-reduce LLM 摘要

## 适用场景

- 让编码 agent 跨会话记住决策与教训
- 修改代码前查询反向影响面与调用链
- 在多台机器/VPS 上共享团队记忆库

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L5: Agent-oriented memory and code intelligence over MCP. AI agents don't read docs — they call tools. nano-brain gives 
> L22: Self-hosted (Go binary + PostgreSQL), works with any MCP client (Claude Code, OpenCode, Cursor, …), and returns str

## 星数曲线

```mermaid
xychart-beta
    title "nano-step/nano-brain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `581dbd1cbeaa` · [字段定义](../../DATASET.md)*
