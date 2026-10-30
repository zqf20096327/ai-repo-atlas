# asashiki/mcp-switch

⭐ 23 · TypeScript · MIT · 推送 2026-09-22 · [GitHub](https://github.com/asashiki/mcp-switch) · [官网](https://github.com/asashiki/mcp-switch) · 个人维护 · 中文 README

**自托管 MCP 网关：把多个本地/远程 MCP 服务器聚合成一个 OAuth 端点**

部署在用户 VPS 上的单一服务，聚合任意数量的上游 MCP 服务器（远程 HTTP 或本地 stdio 进程），对外暴露一个 OAuth 2.1 端点，使 claude.ai、ChatGPT 等仅支持远程连接且连接槽位有限的 Web/App AI 一次接入即可访问全部工具。内置管理控制台，支持工具分组、按 agent 授权范围、审计日志与 WebMCP 检查；数据存于单个 SQLite 文件。纯转发，自身不携带工具。通过 Docker compose 或 pnpm 本地开发运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聚合远程 HTTP 与本地 stdio MCP 服务器为单一 OAuth 2.1 端点
- 控制台管理服务器、工具分组、agent 授权范围与审计日志（SQLite 存储）
- 纯转发设计：透明转发工具、schema、结果与 MCP-Apps UI 组件
- 控制台可通过 WebMCP 被支持的浏览器 agent 检查与操作

## 适用场景

- 让 claude.ai/ChatGPT 等仅支持远程 MCP 的 AI 访问我本地的 stdio 工具
- 用一个自定义连接器槽位接入全部 MCP 工具集
- 对不同 AI agent 分配可见的工具范围并留审计记录

## 场景标签

 · 领域:AI 基础设施/MCP 网关

## 证据(README 行号)

> L21: ```
> L27: - **Aggregate** any number of MCP servers — remote (URL) or local (stdio, hosted on
> L44: |MCP gateway|Public MCP endpoint (`/mcp`), OAuth 2.1, management console (`/console`)|

## 星数曲线

```mermaid
xychart-beta
    title "asashiki/mcp-switch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `28372e383302` · [字段定义](../../DATASET.md)*
