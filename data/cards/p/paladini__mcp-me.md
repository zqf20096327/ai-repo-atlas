# paladini/mcp-me

⭐ 21 · TypeScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/paladini/mcp-me) · [官网](https://mcp-me.page/) · 个人维护

**让 AI 助手读取你个人档案的本地 MCP 服务器**

mcp-me 是一个本地运行的 Model Context Protocol (MCP) 服务器，为 Claude Desktop、Cursor、Windsurf、VS Code Copilot 等 AI 助手提供结构化的个人资料（身份、职业、技能、兴趣、性格、目标、项目、FAQ，以 YAML 文件存储于 ~/.mcp-me）。它提供 329 个注册生成器，可从 GitHub、DEV.to、Medium、Stack Overflow 等公开 API 自动填充档案，多数数据源无需 API key；另有 13 个实时插件（如 Spotify 正在播放、Last.fm）。所有数据留在本地，不发送云端。提供 ask_about_me、search_profile 工具与 5 个 prompt 模板。限制：需 Node.js 20+，通过 npm 安装或一键接入各助手。

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

- 329 个注册生成器从公开 API（GitHub/DEV.to/Medium 等）自动生成 YAML 档案，多数无需 API key
- 以 MCP 资源（me://identity 等 8 类）与工具形式向任意 MCP 兼容 AI 助手暴露个人资料
- 数据全部留在本地 YAML 文件，不上传云端
- 13 个实时插件（Spotify、GitHub、Last.fm 等）供 AI 按需查询

## 适用场景

- 让每次与 AI 助手的对话都自动带上我的技能、职业与项目背景
- 用一条命令从 GitHub、博客、Stack Overflow 等公开账号生成个人档案
- 通过 ask_about_me 工具让 AI 回答关于我的问题或生成自我介绍

## 场景标签

 · 领域:AI 助手个性化/MCP 工具

## 证据(README 行号)

> L8: **mcp-me fixes that.** It creates a structured personal profile that any AI assistant can read via the Model Context
> L24: - **Works everywhere** — Claude Desktop, Cursor, Windsurf, Copilot, and any MCP-compatible AI assistant
> L234: ## MCP Interface

## 星数曲线

```mermaid
xychart-beta
    title "paladini/mcp-me 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-31 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `ac227d986057` · [字段定义](../../DATASET.md)*
