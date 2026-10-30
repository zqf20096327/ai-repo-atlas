# bgheneti/Amazing-Marvin-MCP

⭐ 44 · Python · 推送 2026-06-11 · [GitHub](https://github.com/bgheneti/Amazing-Marvin-MCP) · 个人维护

**让 AI 助手读写 Amazing Marvin 任务数据的 MCP 服务器**

Python 实现的 Model Context Protocol 服务器，把 Amazing Marvin 任务管理应用的 API 暴露为 28 个 MCP 工具，供 Claude Desktop、Cursor、Windsurf、VS Code 等 MCP 客户端调用。AI 助手可读取任务、项目、分类、标签、目标、已完成任务与时间跟踪数据，并可创建任务、标记完成、启停计时。运行在本机，需 Amazing Marvin API key；限制：不能删除或编辑既有任务，高级功能 API 访问受限。经 Smithery（npx）或 pip 安装，要求 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 28 个 MCP 工具覆盖任务/项目/分类/标签/目标/时间跟踪的读取
- 写操作支持创建任务、标记完成、启停时间跟踪
- 历史完成任务含智能缓存（10 分钟）与按日期/时间范围查询
- 本机运行，数据不经外部服务器存储

## 适用场景

- 在 Claude 或 Cursor 中直接询问今日任务与逾期事项
- 让 AI 根据真实任务数据做每日规划与进度回顾
- 通过对话创建任务、标记完成和管理时间跟踪

## 场景标签

 · 领域:生产力工具/AI 集成

## 证据(README 行号)

> L6: Model Context Protocol
> L21: This connects your Amazing Marvin productivity system with AI assistants like Claude, Cursor, and others. Instead o
> L354: The MCP provides 28 comprehensive tools to AI assistants:

## 星数曲线

```mermaid
xychart-beta
    title "bgheneti/Amazing-Marvin-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-30 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d9c3261253a1` · [字段定义](../../DATASET.md)*
