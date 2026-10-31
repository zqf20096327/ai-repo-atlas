# sh1nj1/plan42

⭐ 13 · Ruby · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/sh1nj1/plan42) · [官网](https://collavre.com) · 个人维护

**人与 AI agent 共用的自托管协作工作区：文档/任务/讨论/上下文合一**

Rails 8 实现的自托管协作平台：每个 block 同时是文档、任务、讨论线程和 agent 上下文单元，块嵌套成树；在任一节点固定上下文块（编码规范、设计文档等），所有后代自动继承。支持 Markdown 导入（标题深度映射为树深度）、Lexical 富文本编辑、块级实时聊天、层级权限、WebAuthn/OAuth 登录。内置 MCP server 供 agent 遍历树结构，并提供 OpenAI 兼容补全 API；支持与 GitHub/Linear/Slack/Notion 双向同步。已知限制：无 token 预算控制、内部命名未完成重构。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- block 同时是文档/任务/讨论/agent 上下文，单一对象而非三份拷贝
- 词法作用域的上下文继承：根节点固定的规则被所有后代任务继承
- 内置 MCP server 与 OpenAI 兼容补全 API
- 与 GitHub/Linear/Slack/Notion 双向同步

## 适用场景

- 团队用一棵树同时管理规格文档、任务和讨论，避免三处重复维护
- 让 AI agent 通过 MCP 读取带边界和继承上下文的任务树
- 自托管部署团队协作与知识库平台

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L38: **Context is lexically scoped.** Pin a context block at any node — coding conventions, a
> L62: We ship an MCP server too, and agents search and traverse the tree through it. Still:
> L89: - An **MCP server** and an **OpenAI-compatible completion API**

## 星数曲线

```mermaid
xychart-beta
    title "sh1nj1/plan42 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5a1b66847656` · [字段定义](../../DATASET.md)*
