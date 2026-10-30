# somratpro/HuggingMes

⭐ 153 · JavaScript · MIT · 推送 2026-06-24 · [GitHub](https://github.com/somratpro/HuggingMes) · [官网](https://huggingface.co/spaces/somratpro/HuggingMes) · 个人维护

**在 HuggingFace Spaces 上免费托管 Hermes AI agent 的自部署网关**

将 Nous Research Hermes Agent 部署到 HuggingFace Spaces 的 Docker 网关：提供 24/7 个人 AI 助手，附管理仪表盘、单 token 访问控制、HF Dataset 持久化备份（默认 600 秒同步）、Cloudflare Worker 出站代理与 KeepAlive、进程自愈重启、终端安装包重启回放、API key 池轮换。启动时直接映射 OpenRouter/Anthropic/OpenAI/DeepSeek 等 20 余家直连 provider，也支持 Hermes 原生 OAuth provider 与任意 OpenAI 兼容自定义端点，并可经 Telegram 使用。README 明确警告：使用本项目可能导致 HuggingFace 账号被封。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 启动时直接映射 20 余家 LLM provider，另支持 Hermes 原生 OAuth provider 与自定义 OpenAI 兼容端点
- HF Dataset 持久化备份与进程自愈、包安装重启回放
- Cloudflare Worker 自动代理被屏蔽的出站流量（Telegram 等）并支持 KeepAlive
- API key 池轮换与单 token 保护仪表盘和 API

## 适用场景

- 在 HF Space 上长期跑一个可经 Telegram 使用的个人 AI 助手
- 不改代码把 agent 工作区数据定期备份到 HF Dataset
- 在受限网络环境为 agent 配置出站代理

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L32: **Self-hosted Hermes AI agent gateway for Hugging Face Spaces.** HuggingMes runs Nous Research Hermes Agent on Hugg
> L38: - 🧠 **Hermes Core:** Runs Hermes Agent for multi-turn chat, tools, memory, and agent workflows.

## 星数曲线

```mermaid
xychart-beta
    title "somratpro/HuggingMes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 152 --> 154
    line [153, 153]
```

2026-10-18 153 → 2026-10-30 153（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `ca2e31f55245` · [字段定义](../../DATASET.md)*
