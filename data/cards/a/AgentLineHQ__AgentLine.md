# AgentLineHQ/AgentLine

⭐ 57 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/AgentLineHQ/AgentLine) · [官网](https://agentline.cloud) · 组织维护

**给 AI agent 提供真实电话号码的开源电话 API 平台**

基于 FastAPI 的自托管 AI 电话 agent 平台：为 Claude Code、Cursor、OpenClaw 等 coding agent 或任意 MCP/HTTP 客户端提供真实电话号码，支持 PSTN 呼出/呼入、SMS 收取、DTMF/IVR 菜单导航与通话转录。内置 STT(Deepgram)+LLM(OpenAI 兼容)+TTS(Cartesia) 语音管线，可切换 LiveKit/Pipecat 运行时，电话线路支持 SignalWire/Twilio/Plivo/Telnyx 多运营商路由与故障转移。依赖 PostgreSQL 与 Redis，提供 Docker Compose 一键部署，README 中另提供 agentline.cloud 托管版。

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

- 内置 MCP 服务器与 skill file，Agent 一行指令发起电话
- STT+LLM+TTS 语音管线可插拔（LiveKit/Pipecat/自定义类）
- SignalWire/Twilio/Plivo/Telnyx 多运营商按国家路由与故障转移
- DTMF/IVR 导航、通话转录、语义轮次检测与 barge-in

## 适用场景

- 让 Claude Code 或 Cursor 通过 MCP 直接拨打电话并读取转录
- 搭建 AI 前台接听呼入电话
- 外呼提醒、回访等语音 agent 任务
- 在电话菜单中自动按 DTMF 键并留言

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L17: AgentLine is an **open-source AI phone agent** / **voice agent telephony API**. It gives coding agents and LLM apps
> L55: - 🔌 **MCP Server** — Native Model Context Protocol tools for Claude Desktop, Claude Code, Cursor, OpenClaw, and Cod

## 星数曲线

```mermaid
xychart-beta
    title "AgentLineHQ/AgentLine 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 55 --> 58
    line [56, 57, 57]
```

2026-10-18 56 → 2026-10-29 57（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f4340897c785` · [字段定义](../../DATASET.md)*
