# Blackman99/agent-feishu-channel

⭐ 48 · TypeScript · MIT · 推送 2026-09-13 · [GitHub](https://github.com/Blackman99/agent-feishu-channel) · [官网](https://blackman99.github.io/agent-feishu-channel/) · 个人维护 · 中文 README

**把 Claude/Codex 编码代理会话接入飞书群聊的桥接服务**

Node.js/TypeScript 编写的桥接程序：通过 WebSocket 连接飞书机器人，将 Claude Code 与 Codex CLI 会话带入飞书群聊，支持按会话切换双提供方、文件编辑/Shell 命令/搜索等完整编码代理工作流。工具调用会以飞书交互卡片形式发起审批，会话状态持久化并在重启后自动恢复；提供 /new、/model、/config 等斜杠命令、MCP 服务器配置与分级上下文缓解（50MB 硬限回退）。需 Node.js>=20 及对应 CLI 二进制，npm 全局安装后以 afc 命令运行。

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

- Claude 与 Codex 双提供方，可按配置或按会话切换
- 工具调用通过飞书交互卡片做权限审批
- 会话持久化：重启后自动恢复对话
- MCP 服务器（stdio/sse）可在配置中挂载给当前提供方

## 适用场景

- 在飞书群聊中直接驱动 Claude Code / Codex 做编码任务
- 通过审批卡片控制代理的敏感工具调用
- 在移动端远程接管和恢复编码代理会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5:  Claude and Codex, natively in Feishu / Lark.
> L20: - **Dual providers** — switch between Claude and Codex per config or per session
> L88: - **Claude CLI** — `claude` binary in `$PATH` when using the Claude provider

## 星数曲线

```mermaid
xychart-beta
    title "Blackman99/agent-feishu-channel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-29 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `859902c35c63` · [字段定义](../../DATASET.md)*
