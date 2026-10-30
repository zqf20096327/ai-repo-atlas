# YCSE/nanobanana-mcp

⭐ 32 · JavaScript · MIT · 推送 2026-03-03 · [GitHub](https://github.com/YCSE/nanobanana-mcp) · 个人维护

**把 Gemini 图像生成/编辑接入 Claude 系客户端的 MCP 服务器**

基于 Model Context Protocol 的服务器，将 Google Gemini 的图像生成与编辑能力（Nano Banana 2 Flash 与 Nano Banana Pro 两个模型）提供给 Claude Desktop、Claude Code 与 Cursor 使用。提供文本生图（2K）、自然语言改图、会话风格/角色一致性、运行时切换模型、多轮图像对话等工具，另有斜杠命令安装器。需 Node.js 18+ 与 Google AI API Key，生成图片保存到本地 Documents 目录，通过 npx 或源码安装运行。

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

- 文本生成 2K 图片与自然语言编辑图片
- Flash/Pro 模型运行时切换，无需重启
- 会话内风格/角色一致性与多轮图像对话
- 支持 Claude Desktop、Claude Code 与 Cursor 三类客户端

## 适用场景

- 在 Claude 或 Cursor 中直接调用 Gemini 生成和编辑图片
- 多轮对话中保持角色/风格一致的连续图像创作
- 快速迭代草稿后切到 Pro 模型出图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: MCP server that brings Gemini's image generation and editing capabilities to Claude Desktop, Claude Code, and Cursor
> L28: claude mcp add nanobanana-mcp -- npx -y @ycse/nanobanana-mcp \

## 星数曲线

```mermaid
xychart-beta
    title "YCSE/nanobanana-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 30 --> 33
    line [31, 32, 32]
```

2026-10-18 31 → 2026-10-30 32（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `df8da2e33078` · [字段定义](../../DATASET.md)*
