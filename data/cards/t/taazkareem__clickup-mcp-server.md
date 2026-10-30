# taazkareem/clickup-mcp-server

⭐ 53 · Dockerfile · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/taazkareem/clickup-mcp-server) · 个人维护

**连接 ClickUp 与 AI Agent 的 MCP 服务器**

基于 Model Context Protocol 的 ClickUp 集成服务器，让 AI Agent 通过自然语言管理任务、清单、冲刺、评论、标签、空间、列表、文件夹、文件、文档、聊天与时间追踪。提供 MCP 规范 OAuth 2.1 与 API Key 混合认证、多账户/多工作区支持、任务与文档的全 CRUD、模糊搜索自动解析实体等功能。覆盖 Cursor、VS Code、Claude、Claude Code、n8n、Codex 等多种 MCP 宿主。限制：该项目已从开源转为付费模式，需 License Key（月付 $9/年付 $59/买断 $89）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 规范 OAuth 2.1 与 API Key/Team ID 混合认证，多账户单会话管理
- 任务全 CRUD、批量操作、嵌套子任务、清单、冲刺、自然语言日期
- 跨任务/列表/文件夹/空间的分层全局模糊搜索，自动解析无需 ID
- 支持 Cursor、VS Code、Claude、Claude Code、n8n、Codex、Docker 自托管等多种接入方式

## 适用场景

- 在 IDE 的 AI Agent 中直接创建和管理 ClickUp 任务
- 通过对话式 Agent 追踪工时、评论和冲刺进度
- 在 n8n 等自动化工作流中接入 ClickUp 操作

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L14: _A high-performance Model Context Protocol (MCP) server for managing tasks, checklists, sprints, comments, tags, sp
> L23: |•&nbsp;Features •&nbsp;Premium&nbsp;Access •&nbsp;Available&nbsp;Tools •&nbsp;Adv.&nbsp;Config •&nbsp;FAQ •&nbsp;D

## 星数曲线

```mermaid
xychart-beta
    title "taazkareem/clickup-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-30 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `86d92a491f10` · [字段定义](../../DATASET.md)*
