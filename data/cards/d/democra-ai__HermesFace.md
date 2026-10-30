# democra-ai/HermesFace

⭐ 28 · Python · MIT · 推送 2026-05-26 · [GitHub](https://github.com/democra-ai/HermesFace) · 组织维护

**在 HuggingFace Spaces 免费部署 Hermes Agent 的方案**

基于 Docker 的 HuggingFace Spaces 部署方案：通过复制 Space 并设置 HF_TOKEN 与一个 API key，即可在免费额度（2 vCPU、16GB RAM）上持续运行 Nous Research 的 Hermes Agent——一个自带 47 个工具、持久记忆与自我改进技能的 AI 助手，并接入 Telegram、Discord、Slack、WhatsApp 等 16+ 消息渠道。核心机制是把 /opt/data 每 60 秒同步到私有 HF Dataset 实现持久化；支持 OpenRouter/OpenAI/Claude/Gemini 等多种 LLM API key。也支持本地 Docker 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 复制 Space + 设置 2 个 Secret 即完成一键部署
- 通过 HF Dataset 同步实现对话/技能/记忆的持久化（每 60 秒）
- 16+ 消息渠道接入：Telegram、Discord、Slack、WhatsApp、Signal、WeChat 等
- 支持 OpenRouter、OpenAI、Claude、Gemini、Nous Portal 等多种 LLM

## 适用场景

- 没有自有服务器时免费 24 小时运行个人 AI 助手
- 把 AI 助手接入 Telegram/WhatsApp 等聊天平台
- 在 HF Spaces 上运行 Hermes Agent 并保留记忆与技能数据

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L38:  Your always-on, self-improving AI agent — free, no server needed
> L61: |**Self-improving**|Hermes creates and refines skills from experience during use|

## 星数曲线

```mermaid
xychart-beta
    title "democra-ai/HermesFace 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-30 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3c30c1de7f56` · [字段定义](../../DATASET.md)*
