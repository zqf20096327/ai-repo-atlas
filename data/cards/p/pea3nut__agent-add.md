# pea3nut/agent-add

⭐ 27 · TypeScript · MPL-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/pea3nut/agent-add) · 个人维护 · 中文 README

**向 20+ 种 AI 编码工具统一安装 MCP/Skill/命令/子代理的 CLI**

一个 npm CLI 工具，用单条 npx 命令把 MCP 服务器、Skill、Prompt 规则、斜杠命令和子代理安装到 Cursor、Claude Code、Codex CLI、Gemini CLI 等 20 余种 AI 工具中，屏蔽各工具配置文件格式差异（JSON/TOML/全局路径等）。资产来源支持内联 JSON/Markdown、本地路径、Git SSH/HTTPS（稀疏检出）、HTTP URL，以及打包多资产的 Pack 清单；并面向资产开发者提供文件格式规范与主机特化语法（sub-agent 按主机覆盖 frontmatter 字段）。运行需 Node.js v18+，通过 npx 直接运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 20+ AI 工具宿主，统一安装 MCP/Skill/Prompt/Command/Sub-agent 五类资产
- Git 来源支持 @ref 与 #path 稀疏检出，不克隆整个仓库
- Pack 清单可一次分发多个资产，多来源自动展开
- sub-agent 支持 agent-add/<host>/<key> 按宿主特化 frontmatter 字段

## 适用场景

- 一条命令把同一套 MCP 配置装进 Cursor、Claude Code 等多个 AI 编码工具
- 团队用 Pack 清单批量分发内部 Skills、命令与子代理
- MCP/资产开发者按规范打包，让用户跨工具一键安装

## 场景标签

 · 领域:AI 开发工具/CLI

## 证据(README 行号)

> L3: **Install MCP, Skills, slash commands, sub-agents and more into any AI tool like Claude Code, Cursor, etc.**
> L41: Every AI tool has its own config format — Cursor uses `.cursor/mcp.json`, Claude Code uses `.mcp.json`, Windsurf us
> L43: agent-add smooths out all the differences. One command installs to any of the supported AI tools:

## 星数曲线

```mermaid
xychart-beta
    title "pea3nut/agent-add 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `303e086863c0` · [字段定义](../../DATASET.md)*
