# parallax-labs/context-harness

⭐ 43 · Rust · AGPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/parallax-labs/context-harness) · 组织维护

**本地优先的知识摄取与检索运行时，服务 Cursor/Claude 等 AI 工具**

面向开发者的本地知识基础设施：通过文件系统、Git、S3 与 Lua 脚本连接器将多格式文档（含 PDF/Word/PPT/Excel）摄取进 SQLite 索引，支持 FTS5 关键词、本地（fastembed/tract）、Ollama 与 OpenAI 向量的混合检索；通过 MCP HTTP 服务器与可复用 profiles 暴露给 Cursor、Claude 等 MCP 客户端，并可运行带作用域工具、检查点与恢复能力的本地受管 agent。以 Rust 实现，CLI 优先（ctx 命令），提供预编译二进制、Nix 与 cargo 安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文件系统/Git/S3/Lua 脚本四类连接器，SQLite+FTS5 本地存储
- 关键词+语义混合检索，支持本地 fastembed、Ollama、OpenAI 向量
- MCP HTTP 服务器与可复用 profiles，面向 Cursor/Claude 等 MCP 客户端
- 带作用域工具、检查点与恢复能力的本地 agent 运行时

## 适用场景

- 为 Cursor/Claude 等 AI 编辑器提供本地项目知识库
- 将 Git 仓库、S3 文档统一索引并混合检索
- 在工作区内运行受权限约束的本地研究 agent

## 场景标签

`RAG` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L13: Context Harness turns project knowledge into infrastructure AI can actually use. It
> L27: - **MCP server** — expose context to Cursor and other AI tools via HTTP

## 星数曲线

```mermaid
xychart-beta
    title "parallax-labs/context-harness 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-28 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `52abfd48f561` · [字段定义](../../DATASET.md)*
