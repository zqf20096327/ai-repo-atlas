# nasroykh/foxmayn_frappe_cli

⭐ 16 · Go · MIT · 推送 2026-10-28 · [GitHub](https://github.com/nasroykh/foxmayn_frappe_cli) · 个人维护

**面向 Frappe/ERPNext 的 CLI、MCP 服务器与桌面应用**

由 Foxmayn 独立开发的工具集：ffc 命令行通过 REST API 操作 Frappe/ERPNext 的文档、报表、工作流、文件与权限，输出 JSON/NDJSON/CSV 支持 --jq 与 --dry-run；`ffc mcp` 作为 MCP 服务器让 Claude Desktop、Claude Code、Cursor、VS Code、Codex 等 AI 客户端访问站点，提供每站点限额、确认审批与本地 JSON 审计日志；另有 Windows/macOS 桌面应用（beta，未代码签名），内置 Assistant 对话操作站点，默认只读，写操作需卡片审批。安装脚本下载发布产物并校验 SHA-256。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- CLI 覆盖文档/报表/工作流/文件/权限，输出 JSON/NDJSON/CSV 并支持 --jq 与 --dry-run
- MCP 服务器支持 Claude Desktop/Claude Code/Cursor/VS Code/Codex 接入，含每站点策略与审计日志
- 安全机制：默认只读、删除/取消/工作流操作需审批、每站点 allow/deny 工具与 DocType
- Windows/macOS 桌面应用带 Ask-before-changes 卡片式变更审批

## 适用场景

- 用脚本批量处理 ERPNext 文档并导出 CSV/JSON
- 让 Claude/Cursor 等 AI 助手在我的 Frappe 站点上代跑报表和任务
- 对 AI 的每次工具调用留本地审计日志并限制其权限

## 场景标签

`工作流自动化` `AI 助手` · 领域:效率与自动化

## 证据(README 行号)

> L10: - **`ffc mcp`** lets AI assistants (Claude Desktop, Claude Code, Cursor, VS Code, Codex) use your sites, with per-s
> L74: ffc mcp install --client claude-desktop    # or claude-code, cursor, vscode, codex; --read-only allows reads only

## 星数曲线

```mermaid
xychart-beta
    title "nasroykh/foxmayn_frappe_cli 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-26 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `17094125d0d5` · [字段定义](../../DATASET.md)*
