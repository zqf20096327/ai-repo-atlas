# TrySita/AutoDocs

⭐ 196 · Python · Apache-2.0 · 推送 2026-06-06 · [GitHub](https://github.com/TrySita/AutoDocs) · [官网](https://trysita.com/) · 组织维护 · 中文 README

**自动生成并维护代码库技术文档的工具，附 MCP 深度搜索**

面向需要维护代码文档的开发者与团队：用 tree-sitter 做 AST 解析、SCIP 做符号解析，构建代码依赖图并拓扑排序，遍历该图生成仓库级依赖感知文档与摘要；LLM 摘要与嵌入走 OpenAI 兼容接口（默认 OpenRouter/OpenAI）。提供 FastAPI 后端、Next.js Web UI（对话与浏览），并内置 MCP 服务器，供编码 agent 通过 codebase-qna 工具查询仓库。本地运行依赖 Docker Compose、pnpm、uv；语言支持限于 TS/JS/Python，不支持多语言混合仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- tree-sitter AST + SCIP 符号解析构建依赖图并拓扑排序
- 遍历依赖图生成仓库级依赖感知文档与摘要
- 内置 MCP 服务器暴露 codebase-qna 工具供编码 agent 深度检索
- FastAPI 后端 + Next.js Web UI，Docker Compose 一键本地运行

## 适用场景

- 为我的代码库自动生成并更新技术文档
- 让 Claude/Cursor 等编码 agent 通过 MCP 理解我的仓库结构与约定
- 在 Web UI 中对话式浏览和检索代码库文档

## 场景标签

`AI 写作` `文档问答` · 领域:内容生成

## 证据(README 行号)

> L28: Automate documentation for any repo: we traverse your codebase, parse the AST, build a dependency graph, and walk t
> L36: - Traverses that graph to create repository-wide, dependency-aware documentation and summaries.

## 星数曲线

```mermaid
xychart-beta
    title "TrySita/AutoDocs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 195 --> 197
    line [196, 196]
```

2026-10-18 196 → 2026-10-30 196（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `21efa2c14490` · [字段定义](../../DATASET.md)*
