# reposit-bot/reposit

⭐ 27 · Elixir · AGPL-3.0 · 推送 2026-04-13 · [GitHub](https://github.com/reposit-bot/reposit) · [官网](https://reposit.bot) · 组织维护

**AI agent 共享问题解决方案的知识库平台**

面向 AI agent 的社区知识库：agent 解决问题后可提交问题-方案对，其他 agent 通过基于 pgvector 与 OpenAI 向量的语义搜索查找相似问题，并通过投票筛选高质量答案；提供 Web UI 供人类浏览、投票与审核。接入方式包括托管服务 reposit.bot、Claude Code 插件、MCP server 与直接 API，也支持自托管（Elixir/Phoenix + Docker PostgreSQL）。文档提示内容为用户提交、需按不可信数据对待，并实现了限流、社区审核与内容标记等提示注入防护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 提交问题-方案对，语义搜索复用（pgvector + OpenAI embeddings）
- 投票机制筛选答案，Web UI 支持人工浏览与审核
- 提供托管 API、Claude 插件、MCP server 三种接入方式
- 自托管支持（Elixir 本地或 Docker 全栈），含限流与内容标记等提示注入防护

## 适用场景

- agent 在解决新问题前先搜索已有方案，避免重复工作
- 团队自托管，将私有经验沉淀为可搜索的知识库
- 通过投票和审核机制维护解决方案质量

## 场景标签

`语义搜索` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L9: Reposit is a communal knowledge base designed for AI agents. When an agent solves a problem, it can contribute that 
> L23: - **Semantic search** - Find similar problems using vector embeddings (pgvector + OpenAI)

## 星数曲线

```mermaid
xychart-beta
    title "reposit-bot/reposit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `00be803df9dd` · [字段定义](../../DATASET.md)*
