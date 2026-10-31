# eddiearc/larkin

⭐ 114 · TypeScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/eddiearc/larkin) · [官网](https://idanlin.cc/work/larkin/) · 个人维护 · 中文 README

**把本地 Coding Agent 运行时接入飞书的本地运行时宿主**

Larkin 是运行在用户本机的 Runtime Host，将外部安装的 Codex、Claude Code、Pi 三种 coding-agent 运行时连接到飞书（Lark），提供会话与提醒的持久化、消息与交互卡片、内嵌本地 Dashboard 与 OpenTelemetry 追踪。它自身不附带运行时、不存储提供商凭据，需用户自行安装并登录 agent 运行时；安装方式包括 npx/npm 全局安装与 GitHub Release 的独立二进制（macOS/Linux/Windows x64），Windows 11 x64 通过了原生端到端启动验证。另提供 Pi 的 tmux 后台 Bash 工具、默认关闭的 Inbox 巡检、遥测离线导出/导入等能力。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个本地进程同时接入 Pi/Codex/Claude Code 三种运行时
- 会话、提醒与本地 Dashboard 持久化，含 OpenTelemetry 追踪与本地 spool
- 提供 macOS/Linux/Windows x64 独立二进制，无需 Bun/npm
- Pi 可选 tmux 后台 Bash 工具与默认关闭的 Inbox 巡检

## 适用场景

- 在飞书里通过消息驱动本地安装的 coding agent 工作
- 让团队在飞书群/私聊中与 Codex、Claude Code 或 Pi 交互
- 本地观察 agent 消息处理链路的追踪与队列状态

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: Larkin is a local Runtime Host that connects Codex, Claude Code, and Pi agent runtimes to Feishu (Lark). It keeps se
> L69: During setup, choose one of the three externally installed runtimes: Pi (`pi`), Codex (`codex`), or Claude Code (`c


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `9885b2ad1b7c` · [字段定义](../../DATASET.md)*
