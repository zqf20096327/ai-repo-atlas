# Portkey-AI/hoot

⭐ 22 · TypeScript · MIT · 推送 2026-02-11 · [GitHub](https://github.com/Portkey-AI/hoot) · [官网](https://hoot.run) · 组织维护

**面向开发者的 MCP 服务器测试与调试客户端工具**

Portkey 维护的 Model Context Protocol（MCP）测试工具，定位类似 Postman 之于 HTTP：连接任意 MCP 服务器（HTTP/SSE 传输、自动检测），执行并测试工具、管理 OAuth 2.1 认证、持久化配置与令牌（SQLite）、一键分享 "Try in Hoot" 链接。含 AI 辅助的上下文感知工具过滤与对话式测试界面。Node.js 后端作为 MCP 客户端避免 CORS 问题；可通过 npx 本地运行或使用 hoot.run 在线版，也支持部署到 Cloudflare Workers。README 标注为 Beta 阶段，暂不支持 resources 与 prompts。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 连接任意 MCP 服务器，支持 HTTP/SSE 传输与自动检测
- OAuth 2.1 自动发现、合规测试与令牌持久化（SQLite）
- AI 驱动的上下文感知工具过滤与对话式测试界面
- npx 一条命令本地运行，或部署至 Cloudflare Workers

## 适用场景

- 开发和调试 MCP 服务器时可视化测试工具调用
- 测试需要 OAuth 2.1 认证的 MCP 服务器
- 团队内通过链接分享 MCP 服务器配置

## 场景标签

 · 领域:AI 开发者工具/MCP

## 证据(README 行号)

> L8: **MCP Testing Tool** — Like Postman, but for the Model Context Protocol.
> L35: - **Connect to any MCP server** — HTTP and SSE transport support
> L37: - **Execute tools** — Test tools with parameters and view responses

## 星数曲线

```mermaid
xychart-beta
    title "Portkey-AI/hoot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-28 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4235696cc9e0` · [字段定义](../../DATASET.md)*
