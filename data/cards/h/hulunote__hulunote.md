# hulunote/hulunote

⭐ 84 · Clojure · MIT · 推送 2026-06-15 · [GitHub](https://github.com/hulunote/hulunote) · [官网](https://www.hulunote.top/) · 个人维护

**带 AI 能力的大纲式双链笔记应用，AI 辅助记录组织知识**

开源大纲式（outliner）双链笔记应用，灵感来自 Roam Research，面向构建网状知识库的个人用户：层级大纲、[[wiki 链接]]与反向链接、每日笔记、多数据库工作区。AI 作为内置功能：应用内 MCP 客户端连接 AI 模型与 MCP 服务器，AI 整理摘要并生成笔记；配套生态含供 Claude Desktop 等客户端读写的 hulunote-mcp-server、OpenClaw agent 插件、Rust 后端、TUI、Electron 桌面端及 Android/iOS 仓库。前端为 ClojureScript，后端需 PostgreSQL 并执行 SQL 初始化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 层级无限嵌套大纲与 [[wiki 链接]]/反向链接
- 内置 MCP 客户端，应用内直连 AI 模型与 MCP 服务器
- hulunote-mcp-server 让 Claude Desktop 等 MCP 客户端用自然语言读写笔记
- AI 自动整理研究资料、摘要、生成层级笔记与跨库检索

## 适用场景

- 用大纲和双链搭建个人第二大脑知识库
- 让 AI 帮我把资料整理成带链接的结构化笔记
- 在 Claude Desktop 或 OpenClaw agent 中用对话管理我的笔记

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: Hulunote is an open-source outliner note-taking application with bidirectional linking. Inspired by Roam Research, d
> L13: - **Built-in MCP Client** — Connect to AI models and MCP servers directly from the app

## 星数曲线

```mermaid
xychart-beta
    title "hulunote/hulunote 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 83 --> 86
    line [84, 85, 84]
```

2026-10-18 84 → 2026-10-24 84（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f4f51e2ea6ae` · [字段定义](../../DATASET.md)*
