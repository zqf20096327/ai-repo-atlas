# yokingma/time-mcp

⭐ 72 · JavaScript · MIT · 推送 2026-01-31 · [GitHub](https://github.com/yokingma/time-mcp) · 个人维护

**为 LLM 提供时间感知能力的 MCP 服务器**

基于 Model Context Protocol 的服务器实现，向 LLM 暴露 6 个时间相关工具：current_time（UTC 与本地时间）、relative_time、get_timestamp、days_in_month、convert_time（跨时区转换）、get_week_year。面向在 Claude Desktop、Claude Code、Cursor、Windsurf 等 MCP 客户端中使用自然语言询问时间的场景。支持 Smithery 自动安装、npm 全局安装或 npx 直接运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 current_time/convert_time 等 6 个时间工具
- 支持 Smithery 一键安装到 Claude Desktop
- 兼容 Claude Code、Cursor、Windsurf 等 MCP 客户端配置

## 适用场景

- 让 Claude Code 等客户端回答当前时间与时区转换问题
- 为接入 MCP 的 LLM 应用补充时间感知能力

## 场景标签

 · 领域:LLM 基础设施/MCP 工具

## 证据(README 行号)

> L5: A Model Context Protocol (MCP) server implementation that allows LLMs to have time awareness capabilities.
> L9: ## Tools

## 星数曲线

```mermaid
xychart-beta
    title "yokingma/time-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-29 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d974b5464dc8` · [字段定义](../../DATASET.md)*
