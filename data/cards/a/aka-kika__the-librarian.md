# aka-kika/the-librarian

⭐ 42 · Python · MIT · 推送 2026-10-16 · [GitHub](https://github.com/aka-kika/the-librarian) · 个人维护

**本地优先的 MCP 技能图书管理员：按意图检索技能并按使用结果策展**

一个用 Python 编写的本地 MCP 服务器，架在编码 agent 与大规模技能集合（SKILL.md 格式）之间：技能集合以原始 markdown 留在磁盘，agent 用自然语言描述意图，librarian 通过 Ollama 嵌入（nomic-embed-text）+ 余弦相似度 + MMR 多样性 + 近期衰减给出短名单，可选接入 Apple Intelligence 端侧模型做重排与软过滤；agent 只读推荐、仅追加式回报结果（librarian_report），librarian_stats 输出从未浮现/低成功率技能供人工策展。索引与存储（Ollama/SQLite）均在本地，需 Python 3.12+，可对接任意 stdio MCP 客户端。限制：嵌入依赖 Ollama 节点；AFM 重排需自行 swiftc 编译且为 macOS 可选件。

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

- 语义检索（Ollama nomic-embed-text 嵌入 + 余弦匹配）替代关键词猜测
- MMR 多样性 + 近期推荐衰减 + 头脑风暴随机外卡，避免重复推荐同一批技能
- agent 只写追加式结果日志，策展决策留给人类（librarian_stats 摘要）
- 可选 Apple Intelligence 端侧重排（含理由说明与防注入清洗），失败回退纯嵌入排序

## 适用场景

- 技能集合过大时避免全部装入 agent 上下文的 token 开销与触发歧义
- 通过使用数据策展技能库：找出从未被选中或低成功率的技能
- 在任意 MCP 客户端（Claude Code、Cursor、Goose 等）中按任务意图获取合适技能

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L31: A local-first MCP server that acts as a **librarian** between coding agents and a large skill collection. The colle
> L155: An MCP server that sits between AI agents and a skill collection: agents describe a task in plain language, the li

## 星数曲线

```mermaid
xychart-beta
    title "aka-kika/the-librarian 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `aa02e4fe631d` · [字段定义](../../DATASET.md)*
