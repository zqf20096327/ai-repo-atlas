# amol21p/mcp-interactive-terminal

⭐ 19 · TypeScript · MIT · 推送 2026-02-16 · [GitHub](https://github.com/amol21p/mcp-interactive-terminal) · 个人维护

**给 AI agent 提供真实交互终端会话的 MCP 服务器**

基于 Model Context Protocol 的终端服务器，让 Claude Code、Cursor、Windsurf 等 AI 编程代理运行 REPL、SSH、数据库客户端和任意交互式 CLI。通过 node-pty + xterm-headless 提供干净输出，无法加载时自动回退到 pipe 模式。提供 7 个工具（创建/发送/读取/关闭会话、控制字符等），采用提示符检测等 4 层命令完成判定，并内置危险命令两步确认、命令黑白名单、可选内核级沙箱等 7 层安全机制。经 npx 安装，要求 Node.js >= 18。

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

- PTY 模式（node-pty + @xterm/headless）与自动回退 pipe 模式双通道
- 7 个 MCP 工具覆盖会话创建、输入输出、控制字符与危险命令两步确认
- 4 层命令完成检测（进程退出/提示符/输出静默/超时）
- 7 层安全机制：MCP 工具注解、确认流、模式检测、黑白名单、可选沙箱与密钥脱敏

## 适用场景

- 让 Claude Code/Cursor 等代理打开 rails console、python、psql、SSH 等交互会话
- 在运行容器内通过 docker exec 执行命令并查看日志
- 为代理终端操作配置命令黑白名单与危险命令人工审批

## 场景标签

 · 领域:AI agent 基础设施/开发工具

## 证据(README 行号)

> L7: MCP server that gives AI agents (Claude Code, Cursor, Windsurf, etc.) real interactive terminal sessions. Run REPLs,
> L15:     ↕  MCP (JSON-RPC over stdio)

## 星数曲线

```mermaid
xychart-beta
    title "amol21p/mcp-interactive-terminal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8d400baf2ebd` · [字段定义](../../DATASET.md)*
