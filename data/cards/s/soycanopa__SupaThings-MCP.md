# soycanopa/SupaThings-MCP

⭐ 26 · JavaScript · NOASSERTION · 推送 2026-03-31 · [GitHub](https://github.com/soycanopa/SupaThings-MCP) · 个人维护

**macOS 上 Things 3 的 MCP 服务器：SQLite 读取与 URL 写入供 AI agent 使用**

面向 macOS Things 3 用户的 MCP 服务器，供 AI 客户端（Codex、Claude Code、Gemini CLI）以编程方式操作任务管理器。读路径查询本地 Things SQLite 数据库获取项目/标题/待办结构，写路径执行官方 things:/// URL 动作，另含语义规划工具（标题推断、校验、项目摘要、任务放置建议）与可选 AppleScript 动作。暴露 37 个 MCP 工具，提供 compact/full 与 limit 参数控制上下文消耗。限制：需 macOS、本地安装 Things 3、Node.js 22+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SQLite 读 + 官方 things:/// URL 写的双路径设计
- 37 个 MCP 工具，覆盖读取、语义规划、写入与导航
- 语义规划层：标题推断/校验、项目摘要、任务放置建议
- compact/full 与 limit 参数降低 token 消耗

## 适用场景

- 让 AI agent 读取我的 Things 项目结构并创建任务
- 为已有项目推断和校验标题结构
- 通过对话在正确的标题下放置待办任务

## 场景标签

 · 领域:工具/生产力（MCP 服务器）

## 证据(README 行号)

> L7: SupaThings MCP is a Things 3 MCP server for macOS.
> L74: MCP servers expose tools over a standard protocol so AI clients can call them programmatically.
> L102: - Tool surface: `37` MCP tools

## 星数曲线

```mermaid
xychart-beta
    title "soycanopa/SupaThings-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0bdf0c6f11bb` · [字段定义](../../DATASET.md)*
