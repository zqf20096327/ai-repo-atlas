# eobarretooo/ClawLite

⭐ 51 · Python · MIT · 推送 2026-06-20 · [GitHub](https://github.com/eobarretooo/ClawLite) · 个人维护

**本地优先的 Linux 自主 AI 助手，多渠道接入与自愈运行时**

Python 编写的本地优先自主 AI agent：通过 LiteLLM 接入 20+ LLM 提供商（OpenAI 兼容、Anthropic 兼容、Ollama/vLLM 本地、OAuth 免费档），经 FastAPI 网关（8787 端口）驱动 agent 引擎，带 BM25+向量混合持久记忆、心跳监督与供应商故障转移的自愈运行时、25+ 技能与工具集、Telegram/Discord/Email/WhatsApp/Slack/IRC 渠道适配器及操作仪表盘。代码由 AI 编写、单人监督维护。支持 git clone 安装、Docker 脚本与 Android/Termux 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LiteLLM 驱动的 20+ LLM 提供商接入（含 Ollama/vLLM 本地与 OAuth 免费档）
- BM25+向量混合持久记忆（FTS5、时间衰减、情节→知识整合，SQLite 或 pgvector）
- 自愈运行时：心跳监督、死信重放、供应商自动故障转移
- 6 种聊天渠道适配器与 25+ 技能、CLI、操作仪表盘

## 适用场景

- 在自己的 Linux 机器上 7x24 运行一个 AI 助手并接入 Telegram/Discord 等聊天渠道
- 在 Termux/Android 设备上部署本地 AI agent
- 通过仪表盘管理会话、定时任务、记忆健康与工具审批

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: *A local-first autonomous AI agent — persistent memory, 20+ LLM providers, real chat channels, and a 24/7 self-heali
> L20: - **Self-healing runtime** — heartbeat supervisor, dead-letter replay, automatic provider failover

## 星数曲线

```mermaid
xychart-beta
    title "eobarretooo/ClawLite 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 49 --> 52
    line [50, 51, 51]
```

2026-10-18 50 → 2026-10-28 51（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `31cedf4ec062` · [字段定义](../../DATASET.md)*
