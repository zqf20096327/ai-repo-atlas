# tezra-io/fermix

⭐ 19 · Elixir · MIT · 推送 2026-10-30 · [GitHub](https://github.com/tezra-io/fermix) · [官网](https://fermix.ai) · 组织维护

**自托管的个人多 agent AI 守护进程：通过你已在用的聊天渠道触达**

以 Elixir/OTP 单应用形式在本地机器后台运行的自我托管 AI agent 平台。所有对话渠道（Telegram、WhatsApp、Slack、Discord、Signal、iMessage、本地 CLI）汇入同一 agent 循环；自带 8 个模型 provider（OpenAI、Anthropic、OpenRouter、本地 Ollama 等）并支持自动回退链。子 agent 与定时任务可固定到不同模型，定时任务（摘要/提醒/监控）持久化并在重启后继续。配置、历史与日志保存在 ~/.fermix，无 Fermix 云端。以自解压二进制分发，安装后注册 OS 服务单元；语音笔记可通过可插拔 STT 后端转写，macOS 另有本地 Realtime 语音伴侣应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 Elixir/OTP 应用承载持久 agent、并发会话与进程内子 agent，无需 HTTP 桥或消息队列
- 8 个模型 provider 含免 key 的本地 Ollama，支持主备自动回退链
- 定时任务（摘要/监视/提醒/检查）隔离运行、持久存储、经渠道回投，重启后存活
- 入站语音笔记经可插拔 STT 后端（openai/xai/deepgram）转写后再进入 agent

## 适用场景

- 在自己机器上常驻一个通过 Telegram/Slack/Discord 等渠道随时联系的个人 AI agent
- 定时跑摘要、提醒与监控检查并把结果推送到聊天渠道
- 用本地 Ollama 免 key 运行、数据不出本机的 agent

## 场景标签

`多智能体` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L15: Fermix is a personal, self-hosted AI agent: it runs as a background service on your own machine and reaches you thr
> L19: - **Bring your own model.** Eight providers — OpenAI, OpenAI Codex, Anthropic, SpaceXAI, OpenRouter, Mistral, Venic

## 星数曲线

```mermaid
xychart-beta
    title "tezra-io/fermix 星数(近 3 点)"
    x-axis ["2026-10-28", "2026-10-29", "2026-10-31"]
    y-axis "stars" 10 --> 20
    line [11, 19, 19]
```

2026-10-28 11 → 2026-10-31 19（+8）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `01d3af68626a` · [字段定义](../../DATASET.md)*
