# bharatrameshwar/commonplace

⭐ 19 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/bharatrameshwar/commonplace) · 个人维护

**macOS 本地活动追踪器：AI 分类活动并生成每日 commonplace book**

本地优先的 macOS 活动追踪应用：捕获守护进程每 5 秒读取前台应用、窗口标题与浏览器 URL，每 30 秒截屏；通过本地 Ollama 模型（默认 qwen3:8b）将活动分类为开发/会议/沟通等类别，并抽取联系人、文档、工单、链接形成每日 commonplace book；附带 Flask 仪表盘（SQLite+FTS5 存储）与供 Claude/Claude Code 查询活动记录的 MCP 服务器。所有数据留在本机，无云端与遥测。捕获仅支持 macOS（AppleScript/screencapture/launchd），其余组件为跨平台 Python。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每 5 秒捕获前台应用/窗口标题/浏览器 URL，每 30 秒截屏
- 本地 Ollama 模型做活动分类与记忆抽取，默认 qwen3:8b
- Flask 仪表盘：时间线、专注分、周报、可搜索的 commonplace book
- 内置 MCP 服务器，供 Claude/Claude Code 查询活动历史

## 适用场景

- 跟踪我每天的时间分配与专注情况
- 回顾我这周和谁谈了什么、读过哪些文档链接
- 让 Claude 基于我的真实活动回答'上周我读了什么'类问题

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L6: A local-first macOS activity tracker with AI-powered classification, a daily commonplace book, and an MCP server for
> L12: - **Captures** the frontmost app, window title, and browser URL every 5 seconds. Takes a screenshot every 30 second
> L13: - **Classifies** activity into categories (Development, Meetings, Communication, …) using a local Ollama model.
> L99: The capture daemon, dashboard rendering, search, and people-extraction don't use AI — they're plain Python and SQL.

## 星数曲线

```mermaid
xychart-beta
    title "bharatrameshwar/commonplace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `09090e5244d9` · [字段定义](../../DATASET.md)*
