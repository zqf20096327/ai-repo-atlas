# nameforjt-afk/session-knowledge

⭐ 305 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/nameforjt-afk/session-knowledge) · 个人维护 · 中文 README

**把 Claude Code 会话历史索引成本地可搜索知识库的 MCP 服务器**

面向 Claude Code 用户的本地 MCP 服务器：读取磁盘上已有的 ~/.claude/projects/**/*.jsonl 会话转录，建立 SQLite FTS5 全文索引与代码索引，向 Claude 提供 13 个 MCP 工具，用于跨会话全文检索、决策追踪、查过往命令、按外部服务标签找已有实现、变量名凭证登记等。纯 Python 标准库实现，无第三方依赖、无嵌入、无 API 调用，数据不出本机；索引进程包含凭据脱敏（模式匹配替换为指纹）与 0600 权限限制。限制：仅支持 Claude Code 转录，代码索引仅读 Python/JS/TS，需 Python 3.10+ 且 sqlite3 带 FTS5。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个 MCP 工具覆盖会话全文检索、时间线重建、决策演化追踪、重复实现检测
- 凭据指纹脱敏 + vault.db 0600 权限 + verify-redaction 泄漏抽查
- 纯 Python 标准库，无嵌入、无 API 调用、数据不出本机
- CJK 搜索采用 bigram 预分词，两字中文词可精确匹配且保留 BM25 排序

## 适用场景

- 换目录后仍能查到过去所有 Claude Code 会话里的决策和踩坑记录
- 写新集成前先搜是否已有同类实现（按外部服务标签而非函数名）
- 查某个变量名在不同环境下的全部真实取值及来源调用点

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L14: This indexes all of it and hands Claude 13 MCP tools to search it. You just ask normally.
> L20: Pure Python standard library. No third-party dependencies, no embeddings, no API calls,
> L135: ~/.claude/projects/**/*.jsonl      transcripts Claude Code already writes

## 星数曲线

```mermaid
xychart-beta
    title "nameforjt-afk/session-knowledge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 304 --> 306
    line [305, 305]
```

2026-10-18 305 → 2026-10-24 305（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b5fbd5c26b26` · [字段定义](../../DATASET.md)*
