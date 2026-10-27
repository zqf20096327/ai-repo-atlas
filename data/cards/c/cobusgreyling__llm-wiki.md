# cobusgreyling/llm-wiki

⭐ 44 · Python · MIT · 推送 2026-07-06 · [GitHub](https://github.com/cobusgreyling/llm-wiki) · 个人维护

**LLM agent 自维护个人知识库的模板与工具包**

Karpathy LLM Wiki 模式的参考实现：以 GitHub 模板形式提供脚手架，用户在 raw/ 目录投放原始资料，LLM agent（Claude Code/Cursor/Codex 等）读取 AGENTS.md 后承担维护工作——摄取来源、更新实体页、修订综述、标记矛盾，知识编译一次并持续更新。工具包提供 wiki CLI（init/search/lint/ingest-status）、默认 BM25 检索（可选 qmd 后端）与 MCP 服务器，输出为结构化互链 markdown，可用 Obsidian 浏览图谱。面向希望用 agent 管理研究笔记、读书笔记、会议记录等个人知识库的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 摄取来源时自动更新关联页面并修订综述
- wiki CLI 提供 init/search/lint/ingest-status 操作，默认 BM25 检索
- MCP 服务器暴露 wiki_search/wiki_lint/wiki_graph 等 12 个工具
- wiki init 自动生成 Cursor/Claude Code/Windsurf/OpenCode 的 agent 配置

## 适用场景

- 让 agent 持续维护科研论文笔记并构建演化中的综述
- 把会议记录、Slack 讨论整合为互链的业务知识库
- 逐章读书笔记自动建立人物/主题页面
- 用 Obsidian 图谱浏览不断增长的知识网络

## 场景标签

`知识库管理` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L9: A **reference implementation** of Andrej Karpathy's LLM Wiki pattern — a compounding personal knowledge base where t
> L95: Point Claude Code, Cursor, Codex, or any agent at the wiki folder. The agent reads **`AGENTS.md`** and becomes your

## 星数曲线

```mermaid
xychart-beta
    title "cobusgreyling/llm-wiki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `e5ce020a6ce1` · [字段定义](../../DATASET.md)*
