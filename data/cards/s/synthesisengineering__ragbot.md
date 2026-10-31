# synthesisengineering/ragbot

⭐ 34 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/synthesisengineering/ragbot) · [官网](https://rajiv.com/blog/2023/05/08/introducing-rbot-a-personalized-ai-assistant-written-by-rbot/) · 个人维护

**给个人用户的对话式 AI 助手运行时：本地优先、工作区感知的合成工程工作台**

Ragbot 是合成工程方法论的对话式参考运行时，由 Rajiv Pant 开发，MIT 许可。以聊天为核心，在用户本机工作区上运行：包含自研 FSM agent 循环（多步规划、子 agent 派发、沙箱代码执行）、双向 MCP（客户端与服务端）、SKILL.md 技能运行时、三层记忆（向量 RAG+实体图+会话记忆）与 OpenTelemetry 可观测性。本地优先并支持 Ollama 本地模型，同时接入 Anthropic/OpenAI/Google；v3.5 起 pgvector 为唯一向量后端（Qdrant 路径已移除）。安装细节在 INSTALL.md，README 未直接给出命令。

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

- 自研 FSM agent 循环：多步规划、子 agent 派发、沙箱执行与确定性重放
- 双向 MCP：作为客户端与服务端，向 Claude Code/Cursor 等 MCP 对端暴露工作区
- SKILL.md 格式技能运行时，兼容 Claude Code 与 Codex CLI 的技能格式
- 三层记忆：向量 RAG + 实体图 + 会话记忆，会话间固化持久事实
- 跨工作区合成：四级保密分级与检索前保密门控

## 适用场景

- 在本机工作区上与 AI 协作完成复杂工作并保留持久记忆
- 用本地模型（Ollama Gemma 4）无 API key 地运行对话与 RAG 检索
- 把工作区能力通过 MCP 暴露给 Claude Code、Cursor 等工具复用

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Ragbot is the chat-led runtime of synthesis engineering — the open methodology for systematic human-AI collaboration
> L13: Ragbot v3.4.0 (May 14, 2026) is the next-major-features release. It moves the project from a polished 2024-paradigm

## 星数曲线

```mermaid
xychart-beta
    title "synthesisengineering/ragbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `347acb71b2ea` · [字段定义](../../DATASET.md)*
