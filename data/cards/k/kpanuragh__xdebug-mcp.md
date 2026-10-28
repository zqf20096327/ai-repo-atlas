# kpanuragh/xdebug-mcp

⭐ 28 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/kpanuragh/xdebug-mcp) · [官网](https://www.npmjs.com/package/xdebug-mcp) · 个人维护

**让 AI 助手通过 MCP 协议直接调试 PHP 的 Xdebug 服务器**

基于 Node.js 的 MCP 服务器，通过 Xdebug 的 DBGp 协议把 PHP 调试能力暴露给 Claude 等 AI 助手：提供 41 个 MCP 工具，覆盖断点（行/条件/异常/函数调用，含 pending 断点）、单步执行、变量检查与赋值、表达式求值、watch 表达式、logpoint、内存/耗时分析、代码覆盖率、请求上下文捕获与会话导出。支持 TCP 与 Unix socket 两种监听模式，支持 Docker 容器内 PHP 的路径映射与 DBGp 代理注册，可同时调试多个 PHP 脚本。经 npm 全局安装或从源码构建，需 PHP 侧启用 Xdebug 扩展。

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

- 41 个 MCP 工具：断点/单步/变量检查/求值/堆栈跟踪
- TCP 与 Unix socket 双连接模式，Unix socket 自动清理陈旧套接字
- 支持 Docker 路径映射与 DBGp 代理注册，可多会话并行调试
- 内存/耗时分析、代码覆盖率、watch 表达式与 logpoint

## 适用场景

- 让 Claude 等 AI 助手代我设置断点、单步并检查 PHP 变量
- 调试运行在 Docker 容器里的 PHP 应用
- 在 AI 辅助调试过程中捕获 $_GET/$_POST/$_SESSION 等请求上下文
- 导出调试会话为 JSON/HTML 报告

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L6: An MCP (Model Context Protocol) server that provides PHP debugging capabilities through Xdebug's DBGp protocol. This
> L346: 1. **MCP Server starts** and listens for Xdebug connections (TCP port 9003 or Unix socket)
> L349: 4. **AI uses MCP tools** to control debugging (set breakpoints, step, inspect)

## 星数曲线

```mermaid
xychart-beta
    title "kpanuragh/xdebug-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b27a6fa9a05e` · [字段定义](../../DATASET.md)*
