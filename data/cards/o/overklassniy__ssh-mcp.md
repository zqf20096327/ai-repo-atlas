# overklassniy/ssh-mcp

⭐ 33 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/overklassniy/ssh-mcp) · 个人维护

**给 AI 助手用的受限 SSH MCP 服务器：远程执行命令与传文件**

基于 Go 实现的 stdio MCP 服务器，向 AI 客户端（Claude Desktop/Code、Cursor、Devin、VS Code、Cline）暴露 8 个工具：远程命令执行、SFTP 上传下载、目录列表与递归同步、端口转发、系统状态采集与服务器列表。命令经白名单/黑名单正则策略校验，SFTP 受本地/远程路径白名单限制，密码/口令/2FA 经环境变量传入。以 TOML 配置多服务器并支持热重载。限制：不校验远端主机密钥（InsecureIgnoreHostKey）。提供源码构建、Docker、MCPB 包与预编译二进制四种安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个 MCP 工具：命令执行、SFTP 传输、目录同步、端口转发、系统状态采集
- 命令白名单/黑名单正则策略与本地/远程路径限制
- TOML 多服务器配置，支持 --config 热重载
- Docker、MCPB 包、预编译二进制（amd64/arm64）多种安装方式

## 适用场景

- 让 Claude Code/Cursor 等 AI 客户端在策略控制下操作远程服务器
- 通过 MCP 工具做 SFTP 文件传输与目录同步
- 让 agent 开关端口转发并采集远程系统状态

## 场景标签

 · 领域:开发运维/AI Agent 工具

## 证据(README 行号)

> L11: An MCP (Model Context Protocol) server that gives AI assistants secure,
> L14: `ssh-mcp` runs over stdio and works with any MCP-compatible client:
> L16: exposes eight tools for command execution, SFTP file transfer, directory

## 星数曲线

```mermaid
xychart-beta
    title "overklassniy/ssh-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-28 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c61ee2832989` · [字段定义](../../DATASET.md)*
