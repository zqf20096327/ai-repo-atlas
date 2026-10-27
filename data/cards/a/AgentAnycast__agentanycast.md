# AgentAnycast/agentanycast

⭐ 79 · Shell · Apache-2.0 · 推送 2026-03-28 · [GitHub](https://github.com/AgentAnycast/agentanycast) · 组织维护

**让 AI agent 跨任意网络互通的 P2P 运行时，免公网 IP**

面向 A2A 协议场景的 P2P 运行时：为运行在笔记本、NAT 后或企业防火墙内的 agent 提供可寻址身份与互通通道。采用 sidecar 架构，薄 SDK 通过 gRPC 与本地 Go daemon 通信；daemon 负责 NAT 穿越（DCUtR 打洞+Circuit Relay 回退）、Noise_XX 端到端加密、W3C DID 身份与基于技能的 anycast 路由。提供 Python/TypeScript SDK、MCP Server 与 CrewAI/LangGraph 等框架适配器，LAN 内 mDNS 零配置发现，跨网需自部署零知识中继。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无需公网 IP：pip install 后 agent 即可被寻址，Go daemon 自动管理
- Noise_XX 端到端加密，中继仅见密文；DCUtR 打洞+中继回退的 NAT 穿越
- 按技能（能力）而非地址的 anycast 路由与技能注册表
- 原生实现 A2A 协议，含 P2P↔HTTP A2A 双向桥接与 MCP 互操作

## 适用场景

- 让运行在 NAT/防火墙后的多个 AI agent 互相发现并派发任务
- 把现有 CrewAI/LangGraph 等 agent 框架接入 P2P 网络
- 在 Claude/Cursor 等 MCP 工具中调用远端 P2P agent 技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: The A2A protocol assumes every agent has a public URL -- but real agents run on laptops, behind NATs, inside corpor
> L103: AgentAnycast uses a **sidecar architecture**: a thin SDK talks to a local Go daemon over gRPC. The daemon handles 
> L129: Turn existing agent frameworks into P2P agents with one function call:

## 星数曲线

```mermaid
xychart-beta
    title "AgentAnycast/agentanycast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-27 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `d9e68854ef09` · [字段定义](../../DATASET.md)*
