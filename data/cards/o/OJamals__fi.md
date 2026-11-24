# OJamals/fi

⭐ 5 · TypeScript · MIT · 推送 2026-11-17 · [GitHub](https://github.com/OJamals/fi) · [官网](https://github.com/OJamals/fi) · 组织维护

**将现有 AI 订阅账号接入一个开源编码工作区**

开源编码应用：将用户已有的 AI 订阅账号（Claude、ChatGPT/Codex、Grok、GitHub Copilot、Cursor 等）统一登录接入，在对话中逐条选择模型。内置编码 agent（文件工具、终端、规划、子 agent、持久会话），每个变更可审查与回滚，任务在受管 Git worktree 中隔离运行。支持 MCP 服务器与插件导入、内置网页搜索与图像生成。提供 macOS/Windows/Linux 桌面安装包，浏览器应用与 headless CLI 从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多个订阅账号统一登录，按对话选择模型，另支持 API key 与自定义端点
- 完整编码 agent：文件工具、终端、规划、子 agent、持久会话
- 变更审查与回滚，任务在受管 Git worktree 隔离运行
- MCP/插件扩展，可导入 Claude Code 与 Codex 配置

## 适用场景

- 在一个应用里切换使用已订阅的多家 AI 编码服务
- 让编码 agent 在隔离 worktree 中执行任务并逐条审查文件变更
- 通过 MCP 服务器和插件扩展工作区能力

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Sign in with the AI plans you already have (Claude, ChatGPT/Codex, Grok, GitHub Copilot, Cursor, and more) and choos
> L18: - **A full coding agent.** File tools, terminals, planning, subagents, and persistent conversations in your own pro
> L24: - **Desktop, web, or CLI.** Desktop apps for macOS, Windows, and Linux with automatic updates; the browser app and 

## 星数曲线

```mermaid
xychart-beta
    title "OJamals/fi 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-24"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-11-15 5 → 2026-11-24 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `d3efb6234b9a` · [字段定义](../../DATASET.md)*
