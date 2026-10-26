# inngest/utah

⭐ 137 · TypeScript · Apache-2.0 · 推送 2026-07-22 · [GitHub](https://github.com/inngest/utah) · 组织维护

**基于 Inngest 的持久化个人 AI agent，多渠道触发自扩展技能**

TypeScript 实现的个人 AI agent：think/act/observe 循环中每次 LLM 调用与工具执行都是 Inngest step，获得重试、单聊并发锁与可观测性。支持 Telegram/Slack 等渠道经 Inngest Cloud WebSocket 触发本地 worker。特色是 sidecar 进程：agent 可自行编写 .ts 函数文件并热加载部署为持久化定时技能。具备两层记忆（日志+MEMORY.md）、对话压缩与上下文裁剪。需 Node.js 23+、Inngest 账号与 LLM API key，本地运行无需公网端点。

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

- 每次 LLM 调用与工具执行均为 Inngest step，具备重试与检查点
- sidecar 热加载 agent 自编写的函数，形成可自扩展的持久化技能
- 两层记忆系统：每日日志由心跳函数蒸馏为长期记忆
- 多渠道（Telegram/Slack）经 ChannelHandler 接口接入，渠道无关的 agent 循环

## 适用场景

- 通过 Telegram/Slack 与个人 AI 助手对话并让其操作本地文件系统
- 让 agent 自行编写定时任务（如晨间分诊、每周回顾）并自动部署
- 需要对话状态跨重启持久保留的个人助理场景

## 场景标签

`AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A durable AI agent built with Inngest and pi-ai. No framework. Just a think/act/observe loop — Inngest provides dura
> L19: Channel (e.g. Telegram) → Inngest Cloud (webhook + transform) → WebSocket → Local Worker → LLM (Anthropic/OpenAI/Go

## 星数曲线

```mermaid
xychart-beta
    title "inngest/utah 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 136 --> 138
    line [137, 137]
```

2026-10-18 137 → 2026-10-26 137（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `96fc823381e6` · [字段定义](../../DATASET.md)*
