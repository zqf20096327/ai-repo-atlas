# KHOAAI-HILL/llm-wiki-template

⭐ 22 · Python · MIT · 推送 2026-07-24 · [GitHub](https://github.com/KHOAAI-HILL/llm-wiki-template) · 个人维护

**AI 维护个人知识库的 Obsidian 模板：LLM 编写并维护结构化 wiki**

基于 Karpathy LLM Wiki Pattern 的 Obsidian vault 模板：用户将原始资料（文章、论文、视频等）放入 raw/，由外部 LLM 编码代理按 10 个工作流（/ingest、/compile、/ask 等）编译为结构化 wiki 文章，并通过 /ask 基于个人知识库回答问题。采用文件方案替代 RAG 与向量数据库，含矛盾检测、质量守则（文章 15-120 行、更新前重读）、知识图谱分析与 MCP Server（FTS5 搜索）。需配合 Gemini CLI、Claude Code 等代理使用，语言可自定义，附 Python 批量导入脚本与 brain CLI 更新工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个自动化工作流（ingest/compile/ask/autoresearch 等），代理读取 AGENTS.md 即可运行
- 编译时自动检测矛盾声明，以 warning 标注并要求人工审核，不静默覆盖
- 文件化架构：Markdown 可检视，无数据库与厂商锁定，声明不用 RAG 向量库
- 内置 MCP Server（FTS5 搜索，绑定 127.0.0.1）供 AI 代理访问知识库

## 适用场景

- 把研究资料编译成可持续积累的个人 wiki 并基于其问答
- 让代理自主检索网络、评估来源并生成研究综述
- 在 Obsidian 中搭建带质量审计的第二大脑

## 场景标签

`知识库管理` `科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: > An AI-managed personal knowledge base using the **Karpathy LLM Wiki Pattern** — where LLMs write and maintain a st
> L22: Instead of relying on complex RAG pipelines or vector databases, this system uses a simpler approach:
> L26: 3. **You ask questions** and get answers grounded in your personal knowledge base

## 星数曲线

```mermaid
xychart-beta
    title "KHOAAI-HILL/llm-wiki-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e3e429b5e459` · [字段定义](../../DATASET.md)*
