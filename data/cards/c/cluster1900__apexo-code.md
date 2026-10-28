# cluster1900/apexo-code

⭐ 42 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/cluster1900/apexo-code) · 个人维护 · 中文 README

**跨终端/网页/桌面的通用编程 Agent，多模型接入**

Apexo 是一个开源通用编程 Agent，由单一本地 Agent 运行时驱动 TUI、Web UI 和 Electron 桌面三种界面。提供自主目标迭代（/goal）、多会话工作流、后台任务与子 Agent 编排、跨会话持久记忆、命令沙箱（macOS seatbelt / Linux bubblewrap）与生命周期钩子等机制。模型接入覆盖 Google Gemini/Antigravity、xAI Grok（含 OAuth 登录）及任意 OpenAI 兼容端点（OpenAI、Claude、MiniMax、DeepSeek、vLLM、Ollama 等）。通过 npm 全局安装预编译 CLI，桌面安装器从 GitHub Releases 获取；桌面应用无自动更新，需重建或重装新版。

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

- 统一本地运行时驱动 TUI/Web/桌面三界面
- 自主目标（/goal）与多会话工作流、后台子 Agent 编排
- OS 级命令沙箱（seatbelt/bubblewrap）与持久项目记忆
- Gemini/Antigravity 与 xAI Grok 一等支持，兼容任意 OpenAI 兼容端点

## 适用场景

- 在终端里让 Agent 按目标自主迭代完成编码任务
- 用自定义端点（vLLM/Ollama/DeepSeek 等）驱动本地化编程助手
- 通过沙箱限制 Agent 执行的 shell 命令权限

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: Apexo is a **general-purpose coding agent** with a unified terminal UI (TUI), web UI, and Electron desktop app powe
> L12: Rather than being tied to a single model vendor or acting as a thin wrapper, Apexo provides its own deeply engineer


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `34b8eb42d1b8` · [字段定义](../../DATASET.md)*
