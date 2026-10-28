# hybroai/hybro-hub

⭐ 30 · Python · Apache-2.0 · 推送 2026-07-02 · [GitHub](https://github.com/hybroai/hybro-hub) · [官网](https://hybro.ai) · 组织维护

**把本地 AI agent 接入 hybro.ai 门户、与云端 agent 统一使用的守护进程**

Hybro Hub 是一个 pip 安装的轻量后台守护进程，将用户机器上的本地 agent（如 Ollama 模型、OpenClaw、n8n 工作流、Hermes 助手）通过 A2A 协议同步到 hybro.ai 门户，与云端 agent 并列对话。连接为仅出站方向，无需开入站端口；本地 agent 的处理在本机完成，消息内容不离开本机，云端中继只见路由元数据。内置 PII/自定义关键词/正则的敏感内容检测（当前仅记日志），支持自动发现 localhost 上的 A2A agent，另附带调用云端 agent 的 Python SDK。需 hybro.ai API key 才能启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地与云端 agent 在同一门户并列使用，消息标注 Local/Cloud 处理位置
- 仅出站连接，无需防火墙变更，可在 NAT 后工作
- 捆绑 ollama/openclaw/n8n/hermes 四种 A2A agent 适配器
- 自动探测 localhost 端口上的 A2A agent（agent.json/agent-card.json）

## 适用场景

- 把本地 Ollama 模型接入 hybro.ai 与云端专业 agent 并列对话
- 敏感数据留在本机处理，其余任务按需选用云端 agent
- 以 SDK 在自己的代码中调用 hybro.ai 云端 agent

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L9: Hybro Hub is a lightweight daemon that connects your local AI agents to hybro.ai — so you can use local and cloud ag
> L26: Hybro Hub bridges local and cloud. Open hybro.ai, see your local Ollama model next to cloud agents like a legal rev
> L97: - **A2A protocol** — local and cloud agents speak the same Agent-to-Agent protocol. Any A2A-compatible agent works.

## 星数曲线

```mermaid
xychart-beta
    title "hybroai/hybro-hub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f6013cd17777` · [字段定义](../../DATASET.md)*
