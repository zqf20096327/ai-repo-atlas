# herdodp/snapgent-connector

⭐ 53 · JavaScript · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/herdodp/snapgent-connector) · [官网](https://herdodp.github.io/snapgent-connector/) · 个人维护

**让任意 AI 聊天网站直接操作 VS Code 工作区的浏览器扩展**

由浏览器扩展、本地桥接程序与 MCP 服务器三部分组成：用户在 AI 聊天网页中用自然语言描述任务，扩展检测聊天中的命令，经本地 WebSocket 桥接路由到 VS Code 等 MCP 目标执行，并把结果返回聊天继续对话。支持 ChatGPT、Claude、Gemini、Kimi、Grok、GLM、通义千问等 10 个聊天站点。免费开源，无需 API key 或注册；要求 Edge/Chrome 浏览器，Windows 附带桥接可执行文件，macOS/Linux 需 Python 3.9+ 运行 bridge.py。另可选接入 EffectCraft 与 Roblox Studio MCP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器扩展 + 本地桥接 + MCP 三层架构，自动使用当前打开的 VS Code 工作区
- 支持 10 个 AI 聊天站点（ChatGPT/Claude/Gemini/Kimi/Grok/GLM/通义千问等）
- 无需 API key、订阅或登录，免费开源
- 可选接入 EffectCraft CLI 与 Roblox Studio MCP 目标

## 适用场景

- 在 ChatGPT/Claude 等网页聊天中直接让 AI 检查和修改 VS Code 项目文件
- 不配 API key 复用已有聊天账号驱动编码任务
- 把 AI 聊天连接到 Roblox Studio 或 EffectCraft 等 MCP 目标

## 场景标签

`编码 Agent` `GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L19: snapgentV3 is a browser extension plus a local bridge that connects a normal AI chat to **VS Code**. It automatical
> L33: │  AI chat    │ ───  commands  ───▶ │ snapgentV3       │ ──────────────▶ │  Bridge    │ ────────▶ │ Selected MCP   
> L41: 4. The **bridge** routes it to the VS Code MCP server.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0c80a2a7e311` · [字段定义](../../DATASET.md)*
