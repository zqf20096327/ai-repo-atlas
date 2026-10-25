# reichenbach/iwork_mcp

⭐ 39 · TypeScript · 推送 2026-10-20 · [GitHub](https://github.com/reichenbach/iwork_mcp) · 个人维护

**用 AI agent 自动化操作 macOS iWork 三件套的 MCP 服务器**

面向 Claude、Codex、Cursor、Grok 等 MCP 客户端的 agent 中立服务器，暴露 117 个工具，覆盖 Numbers 电子表格、Pages 文档与 Keynote 演示的创建、编辑、公式、图表及多格式导出；通过 JavaScript for Automation 控制本机 iWork 应用。支持本地 stdio 与带 OAuth 2.1/PKCE 认证的 Streamable HTTP 两种传输，远程模式须跑在装有 iWork 的 Mac 上、经 Cloudflare Tunnel 暴露。要求 macOS 13+、Node.js 18+，首次使用需授予自动化权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 117 个工具覆盖 Numbers/Pages/Keynote 的创建、编辑与多格式导出
- 本地 stdio 与远程 Streamable HTTP 双传输，共享同一工具集
- 远程模式内置 OAuth 2.1 动态注册、PKCE、轮换刷新令牌与速率限制
- npx 一行安装，适配 Claude/Codex/Cursor/Grok 等客户端

## 适用场景

- 让 Claude 或 Codex 等 agent 直接生成和编辑 Numbers 表格、Pages 文档、Keynote 演示
- 把 Mac 上的 iWork 自动化能力以远程 MCP 端点形式提供给客户端
- 批量或组合操作（compound batch）处理 iWork 文档

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: An agent-neutral MCP server for automating Numbers, Pages, and Keynote on macOS. It exposes 117 tools over local std
> L94: For local use, an MCP client communicates with the server over stdio. For remote use, the official SDK's Streamable

## 星数曲线

```mermaid
xychart-beta
    title "reichenbach/iwork_mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-25 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2adaa1fe00cd` · [字段定义](../../DATASET.md)*
