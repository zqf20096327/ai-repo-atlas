# token-hunter/CrewVela

⭐ 13 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/token-hunter/CrewVela) · 个人维护 · 中文 README

**让多个编程 Agent 在同一桌面工作台沟通协作的 Tauri 应用**

基于 Tauri 2 + React + Rust 的本机桌面多 Agent 工作台，把 Agent 会话、会话间通信、项目协作与工作交接放进同一窗口。支持并排会话、网格分屏、Git worktree 工作目录分隔、交接资料预览、全自动托管交付以及可选的本地共享记忆接入；接入 8 个 Agent 系列的 CLI 与原生聊天入口，沿用各 Agent 本机的账号与模型配置，CrewVela 自身不做模型推理。当前为 v0.1.0 Beta，提供 Windows x64 安装包与 macOS Apple Silicon DMG，Linux/Intel Mac 无已验证安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 接入 8 个 Agent 系列（Claude Code、Codex、Kimi、DeepSeek 等）的 CLI 与原生聊天入口
- 会话通信：选择发送方与接收方传递消息，附通信诊断
- 工作交接机制：预览交接资料，保留来源会话可见历史
- 可选本地共享记忆与 Git worktree 工作区管理

## 适用场景

- 让一个 Agent 实现功能、另一个 Agent 审查代码
- 当前 Agent 卡住时交接给另一个 Agent 继续处理
- 把一个需求拆成多个角色，按任务依赖推进项目
- 同时推进多个任务，分屏查看各 Agent 会话

## 场景标签

`多智能体` `编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L20: CrewVela 是一个基于 **Tauri 2 + React + Rust** 的桌面多 Agent 工作台，把独立会话、会话通信、项目协作和工作交接放进同一个窗口。沿用各 Agent 的本机安装、账号与权限机制，让你围绕任务
> L71: 当前提供 8 个 Agent 系列的接入。实际可用性取决于 CLI、适配器、账号与模型配置。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `2737ac6ceeeb` · [字段定义](../../DATASET.md)*
