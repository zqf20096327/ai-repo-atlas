# 2233admin/obsidian-llm-wiki

⭐ 37 · TypeScript · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/2233admin/obsidian-llm-wiki) · [官网](https://github.com/2233admin/obsidian-llm-wiki/wiki) · 个人维护 · 中文 README

**把团队研究资料编译成可审查 Obsidian 知识库的 MCP 工具链**

面向使用 Claude Code、Codex、OpenCode、Gemini CLI 等 MCP 主机的团队：将 Markdown 笔记库（vault）编译为摘要、概念页、反链与矛盾报告，agent 基于引用回答问题，回答经人工审查后晋升为决策/架构/运行手册。核心机制为 capture→compile→ask→file→review→promote 循环，Git/Gitea 审查作账本。检索默认 Postgres 全文+trigram 关键词、无需嵌入；语义检索为可选升级（Ollama bge-m3 或 OpenAI 兼容端点）。另含本地项目管理层与可选媒体摄入（ChubbySkills，覆盖抖音/B站/小红书/微信等平台）。Claude Code 以 /plugin 安装，其他主机 git clone 后注册 MCP server，需 Node.js 20.18.1+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- capture→compile→ask→file→review→promote 的团队知识编译循环
- MCP server 暴露 vault 知识，agent 回答带引用并可归档至收件箱待审
- 关键词检索零配置（Postgres 全文+trigram，无嵌入无守护进程），语义检索可选
- 支持 Claude Code/Codex/OpenCode/Gemini CLI 等任意 stdio MCP 主机

## 适用场景

- 把团队的论文、会议记录、repo 发现编译成可查询的团队 wiki
- 让 coding agent 基于自己笔记库带引用地回答问题
- 通过 Git 审查流程管理团队知识的晋升与废弃
- 本地摄入抖音/B站/播客等平台内容并纳入同一知识库

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: **LLM Wiki turns a team's raw research folder into a reviewed, queryable, self-improving Obsidian wiki. Headless-fir
> L29: Inspired by Andrej Karpathy's LLM Wiki. Markdown is the source of truth; the compiler turns structure into a graph;
> L111: Anything else speaking stdio MCP transport should work: the server is one `node .../mcp-server/bundle.js` command 

## 星数曲线

```mermaid
xychart-beta
    title "2233admin/obsidian-llm-wiki 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-31 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `766c6d0059a7` · [字段定义](../../DATASET.md)*
