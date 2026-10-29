# democra-ai/HuggingClaw

⭐ 56 · HTML · 推送 2026-05-26 · [GitHub](https://github.com/democra-ai/HuggingClaw) · 组织维护

**在 HuggingFace Spaces 免费部署 OpenClaw AI 助手的一键方案**

面向无自有服务器的用户，将开源 AI 助手 OpenClaw 以 Docker 方式部署到 HuggingFace Spaces 免费层（2 vCPU、16 GB RAM、50GB 存储）。通过 HF Dataset 同步解决 Spaces 重启数据丢失问题，通过 DNS-over-HTTPS 与端点探测解决 WhatsApp/Telegram 等域名被屏蔽的问题。支持 OpenAI、Anthropic、Google、OpenRouter、Ollama 等多种 LLM 后端，40+ 消息渠道，并提供 Control UI 网关。另含像素风多 agent 系统演示（Adam/Eve/Cain/God，经 A2A 协议通信）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键复制 Space + 设置两个 Secrets 即完成部署
- 数据每 60 秒同步至私有 HF Dataset，重启后保留会话与凭据
- 自动探测可用 Telegram API 端点与 DNS-over-HTTPS，绕过 HF Spaces 的 DNS 限制
- 透传全部 OpenClaw 环境变量，支持 OpenRouter/OpenAI/Anthropic/Google/Ollama 等后端

## 适用场景

- 不想买 Mac Mini 或租服务器，免费获得常驻在线的 AI 助手
- 把 AI 助手接入 WhatsApp、Telegram 等消息渠道
- 在隔离的云容器中运行 OpenClaw，限制其系统权限

## 场景标签

`AI 助手` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L67: > **Powered by OpenClaw** — an open-source AI assistant that normally requires your own machine (e.g. a Mac Mini). 
> L144: - All Spaces use `sdk: docker` with Dockerfile-based deployment
> L181: HuggingClaw syncs `~/.openclaw` (conversations, settings, credentials) to a private HuggingFace Dataset repo so yo

## 星数曲线

```mermaid
xychart-beta
    title "democra-ai/HuggingClaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 54 --> 57
    line [55, 56, 56]
```

2026-10-18 55 → 2026-10-29 56（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6133519c131a` · [字段定义](../../DATASET.md)*
