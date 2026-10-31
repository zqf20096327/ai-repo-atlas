# developer2013/bricks-mcp-open

⭐ 92 · PHP · MIT · 推送 2026-09-09 · [GitHub](https://github.com/developer2013/bricks-mcp-open) · 个人维护

**Bricks Builder 的 MCP 服务器：让 AI 助手管理 WordPress 页面**

面向 Bricks Builder（WordPress 页面构建器）的开源 MCP 服务器，提供 105 个工具，覆盖页面与模板 CRUD、样式系统、SEO（含自动修复与站点地图）、内容管理、快照备份、多站点切换及 Elementor→Bricks 迁移等。由 Node.js 服务端与随附的 WordPress REST API 插件（Bricks API Bridge）组成，通过 WordPress Application Passwords 认证。支持接入 Claude Code、Cursor、Windsurf 等 MCP 兼容客户端，可部署到 Railway/Docker 供移动端 Claude Code 远程使用；并提供 CSS 可编辑性守卫与多站点 sites.json 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 105 个工具覆盖页面、模板、样式、SEO、内容、备份、多站点等 17 类操作
- 随附 WordPress 插件注册 REST API，经 MCP stdio 协议与 AI 助手通信
- Elementor 模板到 Bricks 元素的结构化迁移工具（含覆盖率报告）
- 可部署为自托管 MCP 环境（Railway/Docker），供手机端 Claude Code 全天候使用

## 适用场景

- 让 Claude Code/Cursor 等 AI 助手直接创建和修改 WordPress 页面
- 批量执行 SEO 审计与元信息修复
- 管理多个 WordPress 站点的页面与样式
- 从 Elementor 迁移模板到 Bricks

## 场景标签

 · 领域:Web 开发/WordPress 站点管理

## 证据(README 行号)

> L12: **The most comprehensive open-source MCP server for Bricks Builder.**
> L25: Claude Code / Cursor / AI Assistant
> L27:    bricks-mcp (Node.js)

## 星数曲线

```mermaid
xychart-beta
    title "developer2013/bricks-mcp-open 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-31 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ca8e4e20cb8d` · [字段定义](../../DATASET.md)*
