# ageborn-dev/architect-mcp-server

⭐ 25 · TypeScript · MIT · 推送 2026-06-12 · [GitHub](https://github.com/ageborn-dev/architect-mcp-server) · 个人维护

**自扩展 MCP 服务器：让 AI agent 动态创建并安全运行自己的工具**

面向 Model Context Protocol 的 MCP 服务器，供 AI agent 在运行中编写、测试并持久化自定义 JavaScript 工具：工具代码在可复用子进程池与独立 vm 上下文中沙箱执行，网络/文件等能力需经用户按 capability scope 审批（绑定代码 SHA-256 哈希，改动即失效）。提供 8 个网关工具压缩上下文 token 占用、端口 3001 的实时管理仪表盘、cron 调度、webhook、SQLite 持久层与基于 GitHub token 的工具市场。支持 npm/npx 或 Docker Compose 部署。

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

- agent 动态创建/测试/持久化自定义 JS 工具，沙箱子进程池隔离执行
- capability 审批绑定代码 SHA-256 哈希，代码变更需重新审批
- 8 个网关工具聚合 170+ 管理操作，降低约 21K token 占用
- 内置仪表盘、cron 调度、webhook、SQLite 存储与工具市场

## 适用场景

- 让 Claude/Cursor 等 MCP 客户端中的 agent 按需生成缺失工具
- 在隔离沙箱中安全运行 agent 编写的代码并管控其网络/文件权限
- 将工具设为定时任务或发布到市场复用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: AI agents are incredibly smart, but they hit a wall when they need a tool that doesn't exist yet. **Architect MCP re
> L11: Instead of giving your AI agent a fixed, rigid toolbox, you give it an entire *workshop*. If your agent needs to ca
> L17: - **Automated Tool Creation:** Agents construct, test, and permanently save their own JavaScript tools on the fly.

## 星数曲线

```mermaid
xychart-beta
    title "ageborn-dev/architect-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7d87ce9436e8` · [字段定义](../../DATASET.md)*
