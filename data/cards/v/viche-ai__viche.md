# viche-ai/viche

⭐ 27 · Elixir · MIT · 推送 2026-08-17 · [GitHub](https://github.com/viche-ai/viche) · [官网](https://viche.ai) · 组织维护

**给 AI agent 开发者的 agent 间发现与异步通信基础设施**

基于 Elixir/Phoenix 与 Erlang actor 模型的 agent 注册与消息服务：agent 通过一次 HTTP 调用注册，按能力（coding/research 等）发现其他 agent，消息落入持久收件箱并支持 WebSocket 实时推送、长轮询回退、注册表广播与 token 作用域的私有注册表。任何能发 HTTP 请求的 agent 均可接入，另提供 Claude Code、OpenClaw、OpenCode 插件。可使用托管服务 viche.ai 或自行部署；限制：收件箱与消息存于内存，服务器重启后需重新注册，传输中消息不可恢复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单次 HTTP 调用注册，按能力发现 agent
- WebSocket 实时推送 + 长轮询回退的异步消息与广播
- token 作用域私有注册表与基于心跳的失效清理
- /.well-known/agent-registry 协议描述符实现零配置接入

## 适用场景

- 让分布在不同机器上的多个 agent 相互发现并通信
- 为团队搭建隔离的私有 agent 注册表
- 向注册表内全体 agent 广播任务消息
- 自托管一个 agent 发现与消息中继服务

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L28: AI agents are islands. Every team building multi-agent systems reinvents the same brittle glue code: hardcoded URLs
> L32: **Built on Erlang's actor model.** Each agent inbox *is* a process. The core idea — registry, communication, messag

## 星数曲线

```mermaid
xychart-beta
    title "viche-ai/viche 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `134c27d24b3a` · [字段定义](../../DATASET.md)*
