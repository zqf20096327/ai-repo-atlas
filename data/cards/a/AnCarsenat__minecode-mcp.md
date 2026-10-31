# AnCarsenat/minecode-mcp

⭐ 15 · Python · GPL-3.0 · 推送 2026-09-09 · [GitHub](https://github.com/AnCarsenat/minecode-mcp) · [官网](https://pypi.org/project/minecode-mcp/) · 个人维护

**面向 AI 助手的 Minecraft 版本数据 MCP 服务器**

本地运行的 Model Context Protocol (MCP) 服务器，为 GitHub Copilot、Claude 等 AI 助手提供版本精确的 Minecraft 数据访问：注册 30 个工具，包括从 pack.mcmeta 检测目标版本、查询版本间技术变更、基于游戏 Brigadier 语法编译的命令用法与校验、检查数据包目录结构等，并可读取用户本地 Minecraft 日志。通过 JSON-RPC over stdio 由 AI 客户端启动。以 pip/pipx 安装，需 Python 3.10+。作者自述为黑客马拉松项目、经重写后可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 pack.mcmeta 检测目标版本并返回相关破坏性变更
- get_technical_changes 查询两版本间的技术变更
- 基于 Brigadier 语法的命令用法生成与校验（validate_command）
- 注册 30 个工具，JSON-RPC over stdio 通信

## 适用场景

- 让 AI 编码助手在写数据包/模组时获取版本准确的语法
- 检查 AI 生成命令或 JSON 是否符合目标版本
- 排查数据包因版本目录改名而静默失效的问题

## 场景标签

 · 领域:游戏开发工具/AI 基础设施

## 证据(README 行号)

> L15: MineCode is a **local** Model Context Protocol (MCP) server that gives AI assistants like **GitHub Copilot** and **
> L126: MineCode is an **MCP server**, not an app you sit in front of. It speaks JSON-RPC over stdin/stdout and is normall
> L146: [INFO] Registered 30 tools, 1 prompts, 2 resources

## 星数曲线

```mermaid
xychart-beta
    title "AnCarsenat/minecode-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1a8b3924f5ba` · [字段定义](../../DATASET.md)*
