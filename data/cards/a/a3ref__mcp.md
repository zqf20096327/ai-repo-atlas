# a3ref/mcp

⭐ 3 · JavaScript · MIT · 推送 2026-11-04 · [GitHub](https://github.com/a3ref/mcp) · [官网](https://a3ref.github.io/) · 个人维护

**给 AI 编码代理提供 Arma 3 SQF 参考资料与 lint 检查的 MCP server**

以 MCP server 与 Claude Code 插件形式提供 Arma 3 SQF 脚本参考：每日从 Bohemia Interactive 社区 Wiki 镜像全部命令、BIS_fnc_* 函数与核心概念页，提供 search/get/list_group/recent_changes 查询工具及 lint_sqf 静态检查（捕捉编造命令、缺左操作数、弃用命令、未知事件处理器等）。需 Node.js 18+，服务器为单文件、无额外依赖，数据从 wiki.arma3.io 在线拉取并内存缓存一小时。

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

- 五个 MCP 工具：search、get、list_group、lint_sqf、recent_changes
- 每日镜像 BI 社区 Wiki，服务器不打包数据、在线拉取并缓存一小时
- lint_sqf 只报告不可能合法的 SQF，遵循 HEMTT 的 L-S08/L-S02 规则
- 同时以插件形式提供 Claude Code、Codex、Antigravity 安装途径

## 适用场景

- 让 Claude/Cursor 等 AI 编码代理在写 Arma 3 脚本时查询准确的命令语法
- AI 生成 SQF 代码后自动 lint 检查编造或误用的命令
- 无 MCP 客户端时直接读取 wiki.arma3.io 的 Markdown/JSON 参考页

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L1: # a3ref MCP server — Arma 3 SQF reference and linter for AI agents
> L7: plus a static checker that catches the mistakes models make most in SQF.
> L33: Requires Node.js 18 or newer. The server is a single file with no dependencies to install. Step-by-step

## 星数曲线

```mermaid
xychart-beta
    title "a3ref/mcp 星数(近 2 点)"
    x-axis ["2026-11-23", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-23 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `0a4ec4f5f481` · [字段定义](../../DATASET.md)*
