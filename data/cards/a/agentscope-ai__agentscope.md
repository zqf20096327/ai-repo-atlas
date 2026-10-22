# agentscope-ai/agentscope

⭐ 33,658 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/agentscope-ai/agentscope) · [官网](https://docs.agentscope.io/) · 组织维护 · 中文 README

**给开发者的 agent 构建框架与服务运行时**

AgentScope 2.0 是一个 agent 框架，提供 SDK 层与服务层两部分：SDK 层以 ReAct 循环、工具集、模型接入、上下文压缩、记忆、权限/人工确认、沙箱执行等构件组合出 agent；服务层为 FastAPI 后端加预置 Web UI，提供多租户多会话、leader-worker 团队编排、IM 渠道接入（飞书/Discord）、RAG 服务、MCP 与技能中心、持久化与定时调度。需 Python 3.11+，从 PyPI 或源码安装，Web UI 依赖 pnpm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 2.9 天,年发版 31,169 位贡献者
- 涨星:近 1 天 **+64**(自 20261016 起算)
- 安装:pypi 包 `agentscope` 月下载 196,536
- 平台:— · 协议:MCP / OLLAMA

## 能力要点

- ReAct 循环 agent 构建块：结构化输出、实时中断恢复、批量工具执行
- 模型层接入 OpenAI、Anthropic、Gemini、DashScope、DeepSeek、Moonshot、Volcengine、xAI、Ollama 等
- 内置 agent 服务：多租户多会话、团队编排、飞书/Discord 渠道、RAG、持久化
- 支持 A2A 协议与 MCP 服务器、实时语音 agent（WebRTC）

## 适用场景

- 构建带工具调用与沙箱执行的开发 agent
- 用 FastAPI 服务层把 agent 发布为多会话 Web 应用
- 把 agent 接入飞书或 Discord 作为消息渠道
- 搭建 leader-worker 多 agent 协作与任务规划流程

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L56: AgentScope 2.0 is a production-ready, easy-to-use agent framework with essential abstractions that keep up with ris
> L110: |**Model**|LLM, embedding, and TTS across major providers (OpenAI, Anthropic, Gemini, DashScope, DeepSeek, Moonsho
> L129: AgentScope ships a batteries-included **agent service** — a FastAPI backend with a pre-built Web UI (`examples/web

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai/agentscope 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 33406 --> 33605
    line [33422, 33511, 33589]
```

2026-10-18 33,422 → 2026-10-22 33,589（+167）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `159a070752ea` · [字段定义](../../DATASET.md)*
