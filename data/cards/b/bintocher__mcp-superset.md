# bintocher/mcp-superset

⭐ 60 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/bintocher/mcp-superset) · 个人维护

**管理 Apache Superset 的 MCP server，提供 137 个工具**

面向 AI 助手（Claude 等）的 Model Context Protocol 服务器，通过 137 个工具覆盖 Superset REST API：仪表盘/图表/数据集/数据库的 CRUD 与导入导出、SQL Lab 查询执行与 CSV 导出、用户/角色/RLS/分组等安全管理、权限审计矩阵。内置安全机制：破坏性操作确认标记、SQL Lab 的 DDL/DML 阻断、系统角色保护。认证支持 JWT 自动刷新与 CSRF，或 SSO 场景下的浏览器会话 Cookie。传输支持 streamable-http/SSE/stdio，提供 CLI 参数配置，经 pip 安装后运行。

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

- 137 个工具覆盖仪表盘、图表、数据集、SQL Lab、用户/角色/RLS
- 破坏性操作确认标记（14 类）与 SQL Lab DDL/DML 阻断
- 支持 streamable-http、SSE、stdio 三种传输与 CLI 参数（--host/--port/--transport）
- JWT 自动刷新 + CSRF 处理，SSO 场景可用会话 Cookie 认证

## 适用场景

- 让 Claude 等 AI 助手直接操作我的 Superset 实例管理仪表盘和图表
- 通过对话执行 SQL Lab 查询并导出结果
- 让 AI 助手管理 Superset 用户、角色与行级安全策略
- 对 Superset 实例做资产导出导入备份与权限审计

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L18: A comprehensive Model Context Protocol (MCP) server for Apache Superset. Gives AI assistants (Claude, GPT, etc.) fu
> L44: |Transport|HTTP, SSE, stdio|stdio|stdio|stdio|
> L186: Any MCP-compatible client can connect via:

## 星数曲线

```mermaid
xychart-beta
    title "bintocher/mcp-superset 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-30 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `85bc2b986c93` · [字段定义](../../DATASET.md)*
