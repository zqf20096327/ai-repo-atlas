# Adoit/open-data-agent

⭐ 14 · Python · MIT · 推送 2026-06-19 · [GitHub](https://github.com/Adoit/open-data-agent) · 个人维护

**本地 CLI 数据库查询工具：供人及 AI agent 只读安全地用 SQL 查数据**

命令行工具 oda，连接 PostgreSQL/MySQL/SQLite，面向数据分析师、开发者和 AI 编程 agent。它自身不调用 LLM：通过 SQL 前缀白名单+黑名单双重校验强制只读，自动注入 LIMIT、超时控制、查询历史 JSONL 记录，并从活动 schema 生成 markdown 目录作为上下文。零行或报错时输出结构化诊断（行数、样本值、NULL 计数），供 agent 自我修正重试。配合 OpenCode 时渲染 .opencode/rules/data-agent.md，实现自然语言→SQL→结果闭环。密码存 OS 钥匙串，无钥匙串环境回退为明文。

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

- SQL 白名单+黑名单双重校验强制只读，无绕过机制
- 从活动 schema 生成 markdown 目录供人和 agent 作上下文
- 零行/报错时自动输出结构化诊断支持 agent 自愈重试
- memory 目录以 markdown+YAML frontmatter 保存数据知识

## 适用场景

- 在探索性数据分析中查任意已连接数据库而无需记 schema
- 让 OpenCode 等 AI agent 通过自然语言安全查询数据库
- 为 AI 编程 agent 提供只读、带 LIMIT 注入的数据库工具接口

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: - **AI coding agents** (primarily OpenCode) — `oda` acts as a structured, read-only database interface that an agen
> L64: This means **no extra LLM setup is required for natural language queries** — OpenCode reads your schema docs, under
> L184: OpenCode is an AI coding agent that runs in your terminal. When paired with `oda`, it acts as a natural language i

## 星数曲线

```mermaid
xychart-beta
    title "Adoit/open-data-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `af6881c56081` · [字段定义](../../DATASET.md)*
