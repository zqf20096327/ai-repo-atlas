# m8524769/mermaid-code

⭐ 16 · Svelte · MIT · 推送 2026-10-30 · [GitHub](https://github.com/m8524769/mermaid-code) · [官网](https://mermaid-code.com) · 个人维护 · 中文 README

**本地优先的 Mermaid 图表编辑器，内置 AI Agent 面板与 MCP 服务器**

基于 Mermaid Live Editor 的 fork，用 Tauri 打包为 macOS/Windows 桌面应用。核心是本地 Mermaid 图表编辑：文件树/缩略图侧栏、多标签编辑、Tree-sitter 语法高亮、Vim 模式、自动保存、双击打开 .mmd 文件。AI 部分：内置 Agent 面板可直接与 Claude Code 或 Codex 对话，内置 MCP 服务器（localhost:37079）供 OpenCode、Cursor、Windsurf 等外部 agent 调用 list_diagrams/preview_diagram/search_icons 三个工具读写图表；文件监听实现生成与预览闭环。所有数据留在本地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Claude Code 与 Codex 的 Agent 对话面板（多轮会话、按文件夹恢复历史）
- 内置 MCP 服务器（3 个工具），外部 agent 可直接读写图表与预览
- Tree-sitter 语法高亮、颜色色板预览、关键词自动补全
- 本地文件系统访问与文件监听实时刷新预览

## 适用场景

- 在本地编辑和管理 .mmd 架构图、流程图，不让数据出机器
- 让 Claude Code/Codex 等 agent 根据代码库直接生成和修改图表
- 通过 MCP 让 Cursor 等编辑器内的 agent 预览与更新图表

## 场景标签

 · 领域:开发工具/图表编辑

## 证据(README 行号)

> L7: A local-first Mermaid diagram editor built on Mermaid Live Editor, enhanced with AI agent integration and desktop-na
> L15: **Built-in AI Agent panel** — chat with Claude Code or Codex directly inside the app. Ask it to create, modify, or 
> L17: Other AI agents (OpenCode, Cursor, etc.) can also connect via the built-in MCP server to interact with the app, rea

## 星数曲线

```mermaid
xychart-beta
    title "m8524769/mermaid-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ae6e47dc4de4` · [字段定义](../../DATASET.md)*
