# ch4p-labs/ch4p

⭐ 22 · TypeScript · Apache-2.0 · 推送 2026-06-22 · [GitHub](https://github.com/ch4p-labs/ch4p) · [官网](https://ch4p.ai) · 组织维护

**多渠道可编程的个人 AI 助手平台，安全默认、跨平台运行**

TypeScript 实现的个人 AI 助手平台，以 npm CLI 形式分发，支持 REPL、多渠道网关、桌面 GUI 与 tldraw 画布四种运行模式。接入 Telegram、Discord、Slack、iMessage 等 16 种消息渠道，通过 10 个 trait 接口可替换 LLM 提供方、记忆后端、工具等组件。安全方面默认启用九层防护（文件系统范围限制、命令白名单、AES-256-GCM 加密、输出脱敏等）。支持混合记忆检索、崩溃恢复、定时任务、MCP 客户端与浏览器工具，备选 LLM 路径含 Ollama 与 LiteLLM 代理。

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

## 能力要点

- 16 种消息渠道适配器与 4 种运行模式（REPL/Gateway/GUI/Canvas）
- 10 个 trait 接口实现组件级可替换（provider/记忆/工具/安全策略等）
- 九层默认启用的安全防护与双阶段任务结果校验
- 混合记忆检索（SQLite FTS5 BM25 + 向量相似度，OpenAI→Ollama→noop 自动回退）

## 适用场景

- 在 Telegram/Discord/Slack 等渠道统一运行自己的 AI 助手
- 通过配置文件定制命名 agent 的模型、工具与分发规则
- 以安全默认策略自托管可长期运行的助手网关

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L1: ch4p — personal AI assistant platform
> L21: - **Broad connectivity** — 16 messaging channels, tunnel exposure, and a skills system with OpenClaw-compatible ski
> L48: Channels (CLI, Telegram, Discord, Slack, Teams, iMessage, ...)     Canvas (tldraw, A2UI)

## 星数曲线

```mermaid
xychart-beta
    title "ch4p-labs/ch4p 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fde776608ff6` · [字段定义](../../DATASET.md)*
