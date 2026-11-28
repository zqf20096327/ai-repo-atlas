# starlitxiling/starfane

⭐ 5 · Rust · MIT · 推送 2026-11-27 · [GitHub](https://github.com/starlitxiling/starfane) · [官网](https://github.com/starlitxiling/starfane/releases) · 个人维护 · 中文 README

**单二进制 Rust 控制平面，统一管理多个编码 Agent 会话**

以单二进制 Rust 守护进程形式协调 Claude Code、Codex CLI 与 Antigravity（agy）等交互式编码 CLI，通过统一 TerminalMux 抽象接入 tmux/zellij 长驻会话，并注册官方 hooks 与 stdio MCP 获取事件。提供嵌入式 Web 控制台（中英双语、全量会话回放、上下文占用与吞吐显示）、SSH/Peer 多主机联邦、tmux 备份恢复、证据门控的 Feature Pipeline 与 Two-Speed Debug 流程，以及可插拔通知路由（飞书/Telegram/Discord/Slack/企业微信/QQ）。本地优先、默认零外联流量，通过 Homebrew、预编译二进制或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过官方 hooks 与 stdio MCP 挂接已有 claude/codex/agy 会话，支持生成新交互窗格
- 嵌入式 Web 控制台：中英文部署时选择、全量对话回放、终端滚动缓冲捕获
- SSH ControlMaster 与 Peer starfaned 两类多主机联邦，主机分组侧边栏
- 10 个 MCP 工具与 pipeline/debug 等 CLI 命令，tmux 会话快照备份与恢复

## 适用场景

- 在同一控制台集中查看和管理多个编码 Agent 的会话与上下文占用
- 远程服务器/GPU 容器上的 Agent 会话通过 SSH 或 Peer 节点纳入统一管理
- 对 tmux 会话布局做定期备份并在重启后自动恢复
- 按团队项目配置飞书/企业微信等通知路由并隔离凭据

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Lightweight, single-binary Rust control plane for coordinating Claude Code, Codex CLI, Antigravity (<code>agy</code
> L24: - **Zero Headless, BYO-`tmux` & `zellij` (0.44+)**: Keep your real, long-lived interactive `claude`, `codex`, and `
> L30: - **Swarm, Subagents & Evidence-Gated Playbooks**: Automatically folds native subagents and Swarm workers under par


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `48344c298a9c` · [字段定义](../../DATASET.md)*
