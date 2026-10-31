# mjason/long

⭐ 29 · Elixir · MIT · 推送 2026-07-03 · [GitHub](https://github.com/mjason/long) · [官网](https://github.com/mjason/long) · 个人维护 · 中文 README

**面向家庭/小团队的多用户 LLM agent 运行时，单二进制部署**

基于 Elixir/OTP 的单进程多用户 LLM agent 运行时：Phoenix LiveView 提供 Web 聊天与管理界面，Ash 做数据层，Oban 调度定时任务，ReqLLM 抽象 20+ LLM 提供商接入。核心机制是以 GraphQL 作为 agent 对整个数据层的读写工具面，配合 Anthropic 兼容 Skills、四层记忆、Deno 沙箱代码执行、微信/Telegram 多账号通道。单二进制 curl 安装到 ~/.long，SQLite 存储，无需外部服务；默认面向局域网可信环境，非互联网加固。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 graphql 工具让 agent 通过自省 schema 读写全部数据层
- 四层记忆：工作检查点、事实记忆、Anthropic 兼容 Skills、会话归档
- ReqLLM 原生支持 20+ 提供商（openai/anthropic/ollama/bedrock 等）
- 单二进制含 Erlang VM，curl|bash 一行安装，SQLite 无外部依赖

## 适用场景

- 在闲置 Mac mini 或 Linux 小机上部署家庭共享的 AI agent
- 通过微信/Telegram 多账号绑定让家庭成员各自使用 agent
- 让 agent 自行调度定时任务、执行沙箱代码与浏览网页

## 场景标签

`聊天机器人` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: > A single-process, multi-user LLM agent runtime on Elixir/OTP — for a household or a small team. Phoenix for the U
> L48: |`/chat`|the agent. Streaming replies, live tool-call display, a memory side-rail, AI-named sessions.|
> L63: - **Multi-provider LLM routing** — ReqLLM speaks 20+ providers natively (openai / anthropic / google / groq / deeps

## 星数曲线

```mermaid
xychart-beta
    title "mjason/long 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-31 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c872f3da771c` · [字段定义](../../DATASET.md)*
