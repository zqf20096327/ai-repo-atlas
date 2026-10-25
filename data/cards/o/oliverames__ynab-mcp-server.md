# oliverames/ynab-mcp-server

⭐ 40 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/oliverames/ynab-mcp-server) · [官网](https://www.npmjs.com/package/@oliverames/mcp-server-for-ynab) · 个人维护

**YNAB 的本地 MCP 服务器：让 AI 助手安全读写预算数据**

面向 YNAB 用户的 stdio MCP 服务器，将自然语言预算问题转为 YNAB API 操作：提供 67 个工具与 4 个发现辅助、6 个引导提示，默认只注册 45 个只读操作；写操作需显式开启（YNAB_ALLOW_WRITES=1），每次写入需 preview_write_tool 预览、单次 previewToken 与 confirmed 确认，并记录 undo journal。金额自动在美元与 YNAB milliunits 间转换。支持 Claude Code、Codex、Hermes、Antigravity 等 stdio MCP 宿主，另有托管 OAuth 连接器。部分操作仍需在 YNAB 中手动恢复。

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

- 67 个工具 + 4 个发现辅助，默认 45 个只读操作
- 写入需预览令牌 + 人工确认三重校验，并记录 undo journal
- 美元与 YNAB milliunits 金额自动转换
- 支持 Claude Code / Codex / Hermes / Antigravity 等宿主及托管 OAuth 连接器

## 适用场景

- 用自然语言查询本月某类支出、未审批交易
- 批量整理和归类历史交易
- 在受控确认流程下记账、设定期交易、调整预算分配

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L27: Run YNAB through Claude Code, Codex, Hermes, Antigravity, or any stdio MCP host. For clients that need a remote URL
> L33: This server gives your AI assistant a local interface to YNAB's API, turning natural language into structured budge

## 星数曲线

```mermaid
xychart-beta
    title "oliverames/ynab-mcp-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `efa8f0825d71` · [字段定义](../../DATASET.md)*
