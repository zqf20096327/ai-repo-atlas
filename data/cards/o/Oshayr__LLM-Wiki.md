# Oshayr/LLM-Wiki

⭐ 50 · Python · MIT · 推送 2026-04-26 · [GitHub](https://github.com/Oshayr/LLM-Wiki) · 个人维护

**Claude Code 知识库插件：自动沉淀研究/决策为互链 wiki**

面向 Claude Code 用户的知识管理插件，提供 5 个入口命令与 10 个自主 agent：写作时自动捕获研究、想法与决策到 .wiki/ 目录的 Markdown 页面；/wiki-read 查询时先检索 wiki，未命中则自动调用可用工具（WebSearch、Wikipedia API、MCP 等）研究并入库；/wiki-serve 在 localhost:8420 提供 Wikipedia 风格 Web UI，含知识图谱、FSRS 间隔重复复习、RAG 问答；/wiki-maintain 做 lint、去重、置信度升级与过期检测。数据以 YAML frontmatter 的 Markdown 为真源，9 级新鲜度分层控制刷新。依赖 fastapi/uvicorn/mcp 在首次会话自动安装。

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

- research-on-miss：查询未命中时自动研究并带引用入库
- Wikipedia 风格 Web UI：知识图谱、Canvas、FSRS 间隔重复、RAG 问答
- 9 级新鲜度分层（live 15 分钟到 permanent 永不过期）
- 自维护流水线：lint、去重、置信度升级、事实核查、概念合成

## 适用场景

- 在 Claude Code 工作流中持续积累可检索的项目知识与决策记录
- 让 AI 助手基于既有 wiki 给出带引用的回答，缺失时自动补研究
- 以 Wikipedia 式浏览、图谱与间隔重复方式复习个人知识库

## 场景标签

`知识库管理` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L10: LLM Wiki is a Claude Code plugin that captures research, ideas, and decisions into an interlinked wiki with semanti
> L64:    claude plugin install ./llm-wiki
> L188: LLM Wiki consists of 5 entry points (skills), 10 autonomous agents, utilities in the bin/, and a persistent data l

## 星数曲线

```mermaid
xychart-beta
    title "Oshayr/LLM-Wiki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-30 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `feab509bc7ca` · [字段定义](../../DATASET.md)*
