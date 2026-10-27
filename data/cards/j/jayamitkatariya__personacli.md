# jayamitkatariya/personacli

⭐ 24 · TypeScript · MIT · 推送 2026-09-09 · [GitHub](https://github.com/jayamitkatariya/personacli) · [官网](https://jayamitkatariya.github.io/personacli/) · 个人维护

**本地优先的个人工作区：Markdown 笔记、任务与知文件的 AI 聊天**

运行于本地、通过浏览器访问的个人工作区：数据全部以纯 Markdown 文件存于本机文件夹，无账号、无云、无数据库。提供笔记编辑（CodeMirror）、自然语言任务解析与看板、语义搜索（本地嵌入）、语音输入（parakeet.cpp）。AI 部分支持自动检测 Ollama 或任意 OpenAI 兼容 API，聊天助手可创建/编辑笔记与管理任务，另有后台 Agents 与 MCP server 供外部 agent 读写工作区。macOS 快速上手，需 Node.js 20+，从源码 npm 安装，ffmpeg 与语音模型为可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 所有笔记与任务均为本机纯 Markdown 文件，无云无数据库
- 自动检测本地 Ollama（零配置）或任意 OpenAI 兼容 API，助手可读写笔记与任务
- 本地嵌入的语义搜索，嵌入存储于工作区内
- 可作为 MCP server 供 Claude Code、Cursor 等 agent 读写工作区

## 适用场景

- 在本机管理纯 Markdown 笔记和个人任务，不依赖云服务
- 让了解我工作区内容的 AI 聊天助手代为创建笔记、整理任务
- 通过导入功能从 Obsidian/Notion/Bear/Roam 迁移笔记到本地文件夹

## 场景标签

`AI 助手` `知识库管理` `语义搜索` · 领域:对话与助手

## 证据(README 行号)

> L8: Notes, tasks, and an AI chat that knows your files. Everything lives in one folder
> L43: - **AI chat** — connects to Ollama automatically if it's
> L216: - **Chat** — an AI that can see your workspace and act on it. Attach context

## 星数曲线

```mermaid
xychart-beta
    title "jayamitkatariya/personacli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `388b85aff944` · [字段定义](../../DATASET.md)*
