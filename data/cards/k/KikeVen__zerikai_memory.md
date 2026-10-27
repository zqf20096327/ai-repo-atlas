# KikeVen/zerikai_memory

⭐ 37 · Python · MIT · 推送 2026-10-17 · [GitHub](https://github.com/KikeVen/zerikai_memory) · 个人维护

**给 IDE 的本地 MCP 记忆服务器：代码库索引与跨会话上下文注入**

以本地 STDIO MCP server 形式运行在 IDE 与 LLM 之间：用 tree-sitter 解析代码库，将函数/类/docstring 等实体索引到本地 ChromaDB 向量库（.brain/ 目录），按工作区 UUID 隔离；查询时通过向量检索与 L2/Lexical 重排返回带 file:line 出处的高相关上下文片段，替代原始文件转储以降低 token 消耗。回答合成经 Ollama 或 DeepSeek 自动路由，可接入 DeepSeek API。需 Python 3.11+，通过 git clone 源码安装；主要在 Windows 开发维护，PR 与 Issue 已关闭。

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

- tree-sitter 解析 + ChromaDB 本地向量索引，工作区 UUID 隔离
- query_memory 返回纯文本答案并附 file:line 出处与相关度分数
- LLM 合成经 Ollama/DeepSeek 自动路由，含 token 用量与成本报告工具
- Jev 语义判断层（可选，默认关闭，fail-open）

## 适用场景

- 跨聊天会话保留代码库架构决策与约定，避免冷启动重复解释
- 在 VS Code/Cursor/Claude Desktop 等支持 MCP 的 IDE 间共享同一份项目记忆
- 用紧凑上下文片段替代原始文件转储以控制 token 成本

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L6: zerikai_memory provides persistent, workspace-isolated memory for every IDE that is local-first, cost-aware, and ins
> L51: Zerikai Memory runs as a **local STDIO MCP server** between your IDE and your LLM. It parses your codebase using tr
> L123: 1. Press `Ctrl+Shift+P` → **MCP: Add Local Server**

## 星数曲线

```mermaid
xychart-beta
    title "KikeVen/zerikai_memory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-27 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f3068a24cd80` · [字段定义](../../DATASET.md)*
