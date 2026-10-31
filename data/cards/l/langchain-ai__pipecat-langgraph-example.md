# langchain-ai/pipecat-langgraph-example

⭐ 14 · Python · 推送 2026-10-12 · [GitHub](https://github.com/langchain-ai/pipecat-langgraph-example) · 组织维护

**LangGraph 多智能体交接的示例语音客服（健身房）**

LangChain 官方示例项目：用 LangGraph 构建的虚构健身房客服智能体，采用“agents as graph nodes”模式，triage 分诊节点加 cancellation/credits/booking 三个专家节点，通过 Command(goto) 实现兄弟节点交接。同一张图既以文本聊天形式提供服务，也可作为 Pipecat 实时语音机器人运行（STT→LangGraph→TTS，支持打断）。数据全部为进程内 mock，无数据库与外部 API；默认模型 anthropic:claude-sonnet-4-6，可切换 OpenAI，追踪接入 LangSmith。需 Python 3.11+ 与 uv。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- triage + 3 个专家节点的多智能体 handoff 模式演示
- 同一 LangGraph 图同时驱动文本聊天与 Pipecat 实时语音（支持 barge-in 打断）
- LangSmith 追踪：handoff 决策与专家回复在 trace 树中并列展示
- 语音模式下状态由 Pipecat 上下文承载，每轮从转录恢复当前专家

## 适用场景

- 学习 LangGraph 多智能体交接（handoffs）模式
- 参考如何将同一 agent 图接入文本与语音双渠道
- 了解语音 agent 的 STT/LLM/TTS 流水线与追踪实现

## 场景标签

 · 领域:LLM 应用/语音智能体示例

## 证据(README 行号)

> L3: A tiny customer-support agent for a fictional gym, built with
> L5: served as both a **text chat** and a real-time **Pipecat voice bot** from the
> L92: The same graph also runs as a real-time **Pipecat** voice bot — the agent

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/pipecat-langgraph-example 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `edb58e56eb13` · [字段定义](../../DATASET.md)*
