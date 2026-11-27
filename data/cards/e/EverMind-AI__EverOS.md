# EverMind-AI/EverOS

⭐ 14,012 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/EverMind-AI/EverOS) · [官网](https://evermind.ai/everos) · 组织维护

**给 AI agent 的便携本地记忆层，Markdown 存储**

Python 库与本地优先记忆运行时：把对话、文件、agent 轨迹存为可读 Markdown，并同步本地 SQLite 与 LanceDB 索引以供检索。支持按 user_id/agent_id/app_id 等多维检索、离线反思（合并 episode、精炼 profile 与 skills）、可编辑知识 Wiki。一个 OpenRouter key 即可启动核心流程；嵌入/重排/多模态为可选配置，办公文档解析需系统安装 LibreOffice。提供 MCP 服务器（uvx everos-mcp）接入 Claude Code、Codex、Cursor 等编码助手，并有 Dify 等平台集成指南。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.9 天,年发版 19,9 位贡献者
- 涨星:近 1 天 **+18**(自 20261016 起算)
- 安装:pypi 包 `everos` 月下载 20,408
- 平台:— · 协议:MCP

## 能力要点

- Markdown 为事实源：可读、可编辑、可 diff、可 Git 版本化，编辑后级联 watcher 同步索引
- 本地三件套 Markdown+SQLite+LanceDB，不需要 MongoDB/Elasticsearch/Redis
- 用户侧 episodes/profile 与 agent 侧 cases/skills 作为独立一等表面
- 离线反思：会话间合并 episode 簇、精炼 profile 与 skills

## 适用场景

- 给编码助手接入跨会话持久记忆
- 为 agent 平台统一管理对话与轨迹记忆
- 摄取图片/PDF/音频/办公文档到记忆库
- 需要 Git 版本化、可人工编辑的记忆存储

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: EverOS is a Python library and local-first memory runtime for agents and
> L78: EverOS adds durable memory to the agent and workflow platforms below—and comes
> L325: Plug EverOS memory into Claude Code, Codex, Claude Desktop or Cursor with `uvx everos-mcp`. Works with EverOS Clou

## 星数曲线

```mermaid
xychart-beta
    title "EverMind-AI/EverOS 星数(近 27 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 13546 --> 14054
    line [13588, 13600, 13642, 13662, 13685, 13704, 13721, 13735, 13751, 13588, 13853, 13869, 13887, 13894, 13906, 13913, 13921, 13923, 13930, 13939, 13940, 13953, 13960, 13969, 13980, 14003, 14012]
```

2026-10-25 13,588 → 2026-11-27 14,012（+424）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `bdee5c770f85` · [字段定义](../../DATASET.md)*
