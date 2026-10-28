# Himalayas-App/himalayas-mcp

⭐ 21 · MIT · 推送 2026-10-21 · [GitHub](https://github.com/Himalayas-App/himalayas-mcp) · [官网](https://himalayas.app/mcp) · 组织维护

**远程招聘平台 Himalayas 的 MCP 服务器：求职/招聘工具接入 AI 助手**

通过 Streamable HTTP 端点将 Himalayas 远程工作平台接入 Claude、ChatGPT、Cursor、VS Code、Windsurf、Gemini CLI 等 MCP 客户端。提供 79 个工具：13 个无需账户的公共工具（职位搜索、公司查询、薪资基准、远程工作统计、付费发帖），46 个求职者工具（申请跟踪、简历生成、收件、面试练习），20 个雇主工具（候选人搜索、发帖、站内信）。登录采用浏览器 OAuth 2.1 + PKCE，无需 API key；仅支持 stdio 的客户端需配合 mcp-remote 桥接。旧 SSE 端点已停用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 79 个工具分公共/求职者/雇主三层，13 个无需账户即可用
- OAuth 2.1 + PKCE 浏览器登录，无 API key，Token 自动刷新
- 支持 Claude/Claude Code/ChatGPT/Cursor/VS Code/Windsurf/Gemini CLI 及任意 Streamable HTTP MCP 客户端
- 提供 Claude Code 与 Gemini CLI 插件包，含求职/招聘命令与技能

## 适用场景

- 用 AI 助手按国家/薪资/技能搜索远程职位与薪资基准
- 通过 AI 管理求职申请跟踪、生成针对性简历与求职信
- 雇主经 AI 助手发布职位、搜索候选人并站内沟通

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L7: The Himalayas MCP server connects AI assistants to the Himalayas remote jobs marketplace in real time. It has 79 too
> L111: Any MCP client with Streamable HTTP support can connect to `https://mcp.himalayas.app/mcp`.

## 星数曲线

```mermaid
xychart-beta
    title "Himalayas-App/himalayas-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ee2924b3d417` · [字段定义](../../DATASET.md)*
