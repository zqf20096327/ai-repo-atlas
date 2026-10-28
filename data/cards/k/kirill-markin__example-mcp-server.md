# kirill-markin/example-mcp-server

⭐ 38 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/kirill-markin/example-mcp-server) · 个人维护

**面向 Cursor IDE 的 MCP 服务器模板，用于扩展自定义工具**

基于 Model Context Protocol 的服务器模板：开发者从模板创建自己的仓库，修改工具定义后接入 Cursor IDE。提供一键部署到 Heroku 的方式，也支持 Docker Compose、uv + Python 传统安装以及在 Cursor 内直接通过 stdio 脚本运行三种途径；SSE 与 stdio 两种传输方式均支持。内置示例工具为返回消息的 'mood response'，环境变量可配置端口、主机、调试模式与自定义 User-Agent。另可通过 Smithery 为 Claude Desktop 自动安装。

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

- 一键 Deploy to Heroku 部署按钮
- Docker Compose、uv/Python、Cursor 内 stdio 脚本三种运行方式
- 支持 SSE 与 stdio 两种 MCP 传输方式
- 环境变量配置端口/主机/调试/User-Agent

## 适用场景

- 为 Cursor IDE 添加自定义 MCP 工具的起步模板
- 快速部署一个可被 IDE agent 调用的 MCP 服务器
- 学习 MCP 服务器的基本结构与接入方式

## 场景标签

 · 领域:开发工具/MCP 服务器模板

## 证据(README 行号)

> L1: # MCP Server Template for Cursor IDE
> L3: A simple template for creating custom tools for Cursor IDE using Model Context Protocol (MCP). Create your own repos

## 星数曲线

```mermaid
xychart-beta
    title "kirill-markin/example-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `817284642132` · [字段定义](../../DATASET.md)*
