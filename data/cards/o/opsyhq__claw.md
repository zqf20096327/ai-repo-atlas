# opsyhq/claw

⭐ 25 · TypeScript · Apache-2.0 · 推送 2026-03-15 · [GitHub](https://github.com/opsyhq/claw) · [官网](https://www.npmjs.com/package/@opsyhq/claw) · 组织维护

**把 AI agent 的文件与命令工具经 SSH 扩展到远程机器的 MCP 服务器**

面向使用 Claude Code、Cursor、Claude Desktop 等 MCP 客户端的开发者：Claw 作为 MCP 服务器，提供 8 个工具（bash/read/write/edit/grep/glob/ls/machines），让 agent 能在任意可 SSH 登录的远程主机上执行命令与编辑文件。机制上首次连接时自动部署小型二进制 pincer 到远程 ~/.claw/pincer，经 stdin/stdout JSON-RPC 执行工具，连接持久化复用；复用现有 SSH 密钥与配置，无需远程开放端口、常驻进程或 root。限制：仅限用户 SSH 已有权限的机器；工具调用记录在本地审计日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个 MCP 工具将本地开发工具（bash/read/write/edit/grep/glob/ls 等）扩展到远程机器
- 首次连接自动部署 pincer 二进制，JSON-RPC over stdio 执行，会话结束不驻留
- 复用现有 ~/.ssh/config（密钥、端口、跳板机），远程零配置
- 支持全局 machines.yaml 与项目级 claw.yaml 两种机器配置，工具调用写审计日志

## 适用场景

- 让 Claude Code / Cursor 等 agent 直接查看生产日志、排查 500 错误并修改远程 nginx 配置
- 跨多台远程机器 grep 日志、查找或编辑文件
- 团队通过提交 claw.yaml 共享机器配置，各自使用自己的 SSH 密钥

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: **Claw is an MCP server that extends your agent's tools to any remote machine.** 8 tools. Any host you can SSH into
> L120: Claw exposes 8 MCP tools. These match the tools agents already know from local development (Claude Code's Read/Wri

## 星数曲线

```mermaid
xychart-beta
    title "opsyhq/claw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `13b72ccc0225` · [字段定义](../../DATASET.md)*
