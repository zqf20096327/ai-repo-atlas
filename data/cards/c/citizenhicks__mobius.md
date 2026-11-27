# citizenhicks/mobius

⭐ 632 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/citizenhicks/mobius) · [官网](https://mobius.thinkingsand.dev) · 个人维护

**给编码 agent 的前端中立 Rust 运行时框架与网关**

该仓库包含四个组成部分：mobius agent 框架（session 与 model/tool 循环，可插拔模型、沙箱、存储、能力）、无头网关服务器（pairing、Bots、聊天、定时例程）、终端客户端，以及原生 macOS 应用。用户在本机运行网关后，可从 Mac、终端、iPhone 或 iPad 接入同一会话。框架以 crate 形式发布，可通过 Model/Middleware/protocol trait 组合 AgentConfig 嵌入自有应用。命令在 macOS Seatbelt 或 Linux Bubblewrap 沙箱中执行，审批策略控制敏感操作确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust agent 框架：可插拔模型路由、沙箱、检查点存储与中间件能力
- 网关托管 agents，多客户端（macOS 应用/CLI/移动端）共享同一事件流
- 内置 OpenAI、Anthropic、DeepSeek、Kimi、Mistral、OpenRouter 等提供方，并支持任意 OpenAI Responses API 端点
- macOS Seatbelt 与 Linux Bubblewrap 沙箱执行，按 Bot 审批策略确认操作

## 适用场景

- 在 Rust 中构建自己的编码 agent 或前端
- 在本机托管 agents 并从 Mac、终端、iPhone 多端接入同一会话
- 以 Bot 配置复用不同用途、模型与工具集的 agent
- 用定时例程（Routine）让 Bot 周期性执行任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6:  An open-source runtime for coding agents.
> L24: |`mobius`|`src/`|The agent framework: one session and its model and tool loop, with pluggable models, sandboxes, st
> L25: |`mobius-gateway`|`crates/mobius-gateway/`|The headless server that runs the agents: pairing, Bots, chats, and sche

## 星数曲线

```mermaid
xychart-beta
    title "citizenhicks/mobius 星数(近 16 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 458 --> 657
    line [474, 508, 523, 534, 546, 563, 594, 614, 624, 580, 607, 641, 640, 638, 632, 632]
```

2026-11-10 474 → 2026-11-27 632（+158）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `3cdf35b631bf` · [字段定义](../../DATASET.md)*
