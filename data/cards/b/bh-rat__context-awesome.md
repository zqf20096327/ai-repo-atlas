# bh-rat/context-awesome

⭐ 61 · TypeScript · MIT · 推送 2026-06-10 · [GitHub](https://github.com/bh-rat/context-awesome) · [官网](https://www.context-awesome.com) · 个人维护

**为 AI agent 提供 awesome 清单检索的 MCP 服务与 CLI**

将 GitHub 上 8500+ 个 awesome 清单及其 100 万+条目封装为可查询服务：MCP 服务器（托管远程 URL 或本地 stdio/HTTP 启动）与 CLI 共用同一 npm 包与托管后端，提供 find_awesome_section（发现清单分区）、search_awesome_items（全文搜索条目）、get_awesome_items（按 token 预算取条目）三类操作，供 Claude Desktop、Cursor、Windsurf、VS Code、Gemini CLI 等约 20 种 MCP 客户端接入。后端服务承担清单处理，README 称即将开源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 8500+ awesome 清单、100 万+条目的分区发现与全文搜索
- MCP 服务器与 CLI 一一对应，共用同一 npm 包与托管后端
- 条目获取带 token 预算控制
- 提供约 20 种 MCP 客户端的安装配置说明

## 适用场景

- 让编程 agent 在编码时引用经过社区筛选的工具库参考
- 深度研究 agent 快速按主题收集高质量资源
- 在脚本或 CI 中用 CLI 检索 awesome 条目

## 场景标签

 · 领域:AI agent 基础设施/知识检索

## 证据(README 行号)

> L5: A Model Context Protocol (MCP) server that provides access to all the curated awesome lists and their items. It can 
> L23: |**MCP Server**|point your agent at the hosted URL or spawn `context-awesome-mcp`|Claude Desktop, Cursor, Windsurf,
> L30: Every MCP tool has a 1:1 CLI subcommand — the server and the CLI expose the same operations.

## 星数曲线

```mermaid
xychart-beta
    title "bh-rat/context-awesome 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-29 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `055d6f17f203` · [字段定义](../../DATASET.md)*
