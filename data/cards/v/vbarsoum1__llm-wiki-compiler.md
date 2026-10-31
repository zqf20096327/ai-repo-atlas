# vbarsoum1/llm-wiki-compiler

⭐ 27 · Python · MIT · 推送 2026-04-10 · [GitHub](https://github.com/vbarsoum1/llm-wiki-compiler) · [官网](https://github.com/vbarsoum1/llm-wiki-compiler#quick-start) · 个人维护

**将文档编译为 Obsidian 知识库的 LLM 上下文工具**

Klore 把 PDF、网页、Markdown 等来源编译成结构化的 Obsidian 兼容 markdown 知识库，含来源摘要、概念页、实体页、交叉引用与持续更新的总览。基于 Karpathy 的 LLM Wiki 模式，扩展为三层模型架构：Director 模型承担编辑决策（判断什么值得建页、发现矛盾、质量审查），Strong 模型写概念与实体页，Fast 模型做抽取与标签归一。模型经 OpenRouter 访问，单一 API key、无向量数据库，每次编译自动 Git 提交。支持 Claude Code、Cursor、Windsurf、Codex、Gemini、Copilot 等编码 agent 读取同一份 wiki 作为持久项目记忆。以 pipx/pip 安装的 CLI 提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 步 Director 驱动编译流水线（三层模型分工）
- 输出纯 markdown，含 wikilinks，Obsidian 可直接浏览，无需向量数据库
- klore ask --save 的问答答案归档进语料，参与后续合成
- Claude Code/Cursor/Windsurf/Codex/Gemini/Copilot 共用同一 wiki 上下文，setup.sh 自动配置

## 适用场景

- 把论文、书籍、网页整理成可持续增长的团队/个人知识库
- 给编码 agent 提供基于源文档而非聊天记录的持久项目记忆
- 用 klore ask 基于已编译 wiki 提问并保存答案供后续引用
- 以 Git 追踪知识库每次编译的演变

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L15: **Klore turns raw source material into a persistent, agent-readable knowledge base.** LLMs forget. RAG retrieves fr
> L88: Klore gives coding agents persistent project memory made from your sources, not just chat history. Run `bash setup.

## 星数曲线

```mermaid
xychart-beta
    title "vbarsoum1/llm-wiki-compiler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c8c92c82ff25` · [字段定义](../../DATASET.md)*
