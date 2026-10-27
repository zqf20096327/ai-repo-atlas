# botingw/langgraph-dev-navigator

⭐ 23 · HTML · MIT · 推送 2026-05-20 · [GitHub](https://github.com/botingw/langgraph-dev-navigator) · 个人维护

**面向 LangGraph 开发的 AI 编程助手接地框架：RAG+知识图谱**

一套让 AI 编程助手（Cursor、Cline、Gemini CLI、GitHub Copilot 等）基于本地官方文档生成可靠代码的开发框架：以 langchain-ai/langgraph 官方仓库 git submodule 作为本地知识源，通过 mcp-crawl4ai-rag 服务器提供文档语义检索（RAG，Supabase 向量库）与库结构知识图谱（Neo4j），并含 AI 生成代码幻觉校验工具。依赖 Docker、Python 3.12+、OpenAI API key、Supabase 与 Neo4j；也提供托管 MCP 远程接入路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 官方 langgraph 仓库 submodule 作为版本化本地知识源
- mcp-crawl4ai-rag 服务器提供 RAG 语义检索与代码示例查找
- 基于 Neo4j 知识图谱的 AI 代码幻觉校验（check_ai_script_hallucinations）
- 支持 Docker 容器部署与托管远程 MCP 两种接入路径

## 适用场景

- 让 Cursor/Copilot 等编程助手生成适配当前 LangGraph 版本的代码
- 校验 AI 生成代码是否使用了不存在的类或错误参数
- 基于官方文档做 LangGraph 开发问答与代码检索

## 场景标签

`RAG` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L9: AI coding assistants are powerful, but their general knowledge can be outdated or lead to plausible-but-incorrect co
> L50: 1. **A Local Knowledge Source:** It uses a local git submodule of the official `langchain-ai/langgraph` repository 
> L51: 2. **An Advanced Knowledge Server:** It includes the `mcp-crawl4ai-rag` server, which provides two powerful capabil

## 星数曲线

```mermaid
xychart-beta
    title "botingw/langgraph-dev-navigator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `dcb4e272bb5f` · [字段定义](../../DATASET.md)*
