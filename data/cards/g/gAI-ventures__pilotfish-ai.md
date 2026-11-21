# gAI-ventures/pilotfish-ai

⭐ 5 · TypeScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/gAI-ventures/pilotfish-ai) · [官网](https://pilotfish.gai.ventures/docs/open) · 组织维护

**给 MCP agent 提供本机真实 Chrome 的浏览器自动化 MCP 服务器**

pilotfish 是浏览器自动化 MCP 服务器与 SDK 集合：本地版在本机启动真实 Chrome，通过 browser_* 工具让接入的 MCP agent（模型自备）逐步读页与操作，服务器本身不做模型调用；页面以紧凑大纲加 refs 输出，之后只发送变更差异。附带 TypeScript/Python SDK（可驱动本机 Chrome 或调用其托管云浏览器 REST API）、CDP 客户端、页面快照与 Cookie 横幅等确定性处理模块。本地版 MIT 许可免费；managed 云浏览器为付费服务。需 Node 22+ 与本机 Chrome/Chromium。

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

- 本地 MCP 服务器不做模型调用，由 agent 自带模型逐步决策
- 页面以紧凑大纲输出，后续仅发送变更差异以减少 token
- TypeScript 与 Python SDK 双语言同名接口，含托管 REST API（任务/批次/身份/调度/webhook）
- 提供 Claude Code 插件与 Cursor 插件安装途径

## 适用场景

- 让 Claude Code、Codex CLI、Cursor 等 MCP 客户端操作本机真实 Chrome 完成网页任务
- 在自有代码中以 SDK 驱动浏览器自动化流程
- 使用托管云浏览器执行需持续在线或保存登录态的任务

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: pilotfish is an AI browser agent and a browser automation MCP server: a real Chrome for AI agents and for your own 
> L14: - **Open MCP** (`@gaiventures/pilotfish-mcp`): give any MCP agent (Claude Code, Codex CLI, Cursor, ...) a real Chro
> L15:  your own computer. Free, no account, no API key: your agent's own model reads each page and decides every step thr


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ab075b41f0ea` · [字段定义](../../DATASET.md)*
