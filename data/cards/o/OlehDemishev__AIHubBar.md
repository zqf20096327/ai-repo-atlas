# OlehDemishev/AIHubBar

⭐ 3 · Swift · MIT · 推送 2026-11-27 · [GitHub](https://github.com/OlehDemishev/AIHubBar) · [官网](https://olehdemishev.github.io/AIHubBar/) · 个人维护 · 中文 README

**macOS 菜单栏 AI 服务用量与会话管理面板**

原生 SwiftUI 菜单栏应用，集中显示各 AI 服务的用量限额（环形图、重置倒计时、按用量速率的预测）、本机运行的 agent 会话列表（状态、当前动作、权限请求的 Allow/Deny、后台运行的权限清单）以及项目级 AI 命令模板（结果输出为新文件）。通过 DMG 或 Homebrew 安装，要求 macOS 14+ 和至少一个 AI 服务；另有只读 MCP 服务器、Telegram 通知、13 种语言界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 AI 服务限额集中显示：会话/周限环形图、重置倒计时与用量速率预测
- agent 会话列表：状态、当前动作、通知/面板/Telegram 处理权限请求
- 项目 AI 命令模板（开发者/视频/写作/研究等），Compare 可并排跑多个服务
- 只读 MCP 服务器（AIHubBar --mcp），agent 可查询限额与会话

## 适用场景

- 集中查看 Claude/Codex 等服务的额度剩余与消耗预测
- 从一处批准或拒绝多个 agent 会话的权限请求
- 按项目模板批量运行 AI 命令并对比不同服务的结果

## 场景标签

 · 领域:开发者工具/AI 服务管理

## 证据(README 行号)

> L15: **AI Hub Bar** is a small, native Mac app that lives in the menu bar. One click on ✦ opens a panel with the limits 
> L24: - **Every AI service in one place:** Claude, Codex, GitHub Copilot, Gemini CLI, Cursor, OpenRouter credits, OpenAI 
> L78: **Requirements:** macOS 14 or later (Apple Silicon or Intel) and at least one AI service: an agent such as Claude C


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `651d59b2ee3c` · [字段定义](../../DATASET.md)*
