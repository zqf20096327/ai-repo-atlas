# claw-sharp/ClawSharp

⭐ 15 · C# · MIT · 推送 2026-04-18 · [GitHub](https://github.com/claw-sharp/ClawSharp) · 个人维护

**Claude Code 的 C#/.NET 移植：跨平台终端 AI 编码代理**

将 Claude Code 的终端 AI 编码助手工作流以 C# 实现，发布为单一自包含 .NET 二进制，支持 Windows/Linux/macOS（x64/ARM64），运行时无需 Node.js。覆盖会话循环、工具执行、会话持久化（可恢复会话、保留转录与文件历史）、多提供商接入（Anthropic、Gemini、OpenAI、Codex、GitHub Models、Bedrock、Vertex、Ollama 等）与终端 UX；另附带 Tauri 构建的桌面应用。支持插件、hooks、skills 与 MCP 服务器扩展。作者声明部分 Claude Code 功能仍在对齐中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单一自包含 .NET 二进制，运行时无需 Node.js
- 多提供商支持：Anthropic/Gemini/OpenAI/Codex/GitHub Models/Bedrock/Vertex/Foundry/Ollama
- Tauri 桌面应用与 CLI 双形态
- 支持插件、hooks、agents、skills 与 MCP 服务器

## 适用场景

- 在 .NET 环境中使用终端 AI 编码代理而无需 Node.js
- 在同一工具内切换多家模型提供商
- 通过桌面 GUI 进行长程编码会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **ClawSharp** is a C# port of Claude Code, Anthropic’s terminal-based AI assistant.
> L15: - **Multi-provider** — Anthropic, Gemini, OpenAI, Codex, GitHub Models, Bedrock, Vertex, Foundry, and Ollama
> L102: clawsharp --provider anthropic --model claude-sonnet-4-5

## 星数曲线

```mermaid
xychart-beta
    title "claw-sharp/ClawSharp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4895a035e522` · [字段定义](../../DATASET.md)*
