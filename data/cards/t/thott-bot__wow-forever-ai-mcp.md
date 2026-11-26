# thott-bot/wow-forever-ai-mcp

⭐ 3 · MIT · 推送 2026-11-24 · [GitHub](https://github.com/thott-bot/wow-forever-ai-mcp) · [官网](https://thott.bot) · 组织维护

**把魔兽世界永恒版游戏数据接入 AI 聊天的远程 MCP 服务器**

thott.bot 提供一个远程 MCP 服务器（https://mcp.thott.bot/mcp），向用户的 AI 客户端暴露只读工具，用于查询魔兽世界：永恒版的游戏数据，包括任务、物品、天赋、职业技能、拍卖行实时价格、补丁与热修记录、地图与副本、Blue 帖新闻等。支持 ChatGPT（官方插件）、Claude、Claude Code、Codex、Cursor、Hermes 等任何支持 MCP 的应用，通过 OAuth 登录创建免费账户。每月约 20 次免费提问，无限次为付费档。仓库内仅含 Cursor 与 Hermes 插件配置，不含服务器代码。

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

- 远程 MCP 服务器，OAuth 登录后提供只读游戏数据查询工具
- 数据来自 Blizzard 官方游戏文件与论坛帖，更新在变更落地数分钟内
- 拍卖行全服实时价格，每小时更新
- 内置聊天插件版本可把 AI 带入游戏内

## 适用场景

- 问当前版本最受欢迎的天赋构建与配装
- 查询拍卖行实时价格与物品掉落来源
- 让 AI 帮忙写基于游戏 API 的插件（addon）
- 跟进每周职业改动与补丁说明

## 场景标签

 · 领域:游戏/AI 数据服务

## 证据(README 行号)

> L109: Yes, a remote MCP server at `https://mcp.thott.bot/mcp`. Your AI signs in with OAuth and gets read-only tools to
> L136: There's no server code here: the plugins point your app at `https://mcp.thott.bot/mcp`.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4da2e91eb90c` · [字段定义](../../DATASET.md)*
