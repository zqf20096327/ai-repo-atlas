# anshupriyan/cli-bridge

⭐ 15 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/anshupriyan/cli-bridge) · 个人维护

**给 Claude Desktop 等 MCP 客户端的本地文件系统与受控命令执行服务器**

用 TypeScript 编写的 MCP server，接入 Claude Desktop、Qwen Studio 等任意 MCP 兼容客户端后，为其提供限定在单一工作区根目录内的文件读取/写入/编辑/搜索/grep 工具，以及默认关闭、需显式开启 Dev Mode 的 shell 命令执行（无命令白名单）。附带仅追加的项目日志 PROJECT_LOG.md 供 agent 跨会话恢复上下文，所有工具调用以 JSON 记录到本地审计日志。全程本地运行，无云依赖与遥测。Windows 11 已测试，macOS/Linux 架构支持但未经实测。

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

- 文件工具限定于单一工作区根目录，路径穿越与越界符号链接被拦截
- execute_command 默认阻断，需显式 toggle_dev_mode 开启且无命令白名单
- 每次工具调用写入本地 JSON 审计日志
- 仅追加的 PROJECT_LOG.md 项目日志供 agent 跨会话恢复上下文

## 适用场景

- 让 Claude Desktop 直接读写我指定项目目录里的文件
- 给 MCP 客户端受控地执行构建、git 等本地命令
- 审计 agent 执行过的全部工具调用

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **A local Model Context Protocol (MCP) server that gives Claude Desktop — or any MCP-compatible client — sandboxed f
> L18: `cli-bridge` is a lightweight MCP server that plugs into Claude Desktop (or any MCP client) and gives it:

## 星数曲线

```mermaid
xychart-beta
    title "anshupriyan/cli-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1c708eab965a` · [字段定义](../../DATASET.md)*
