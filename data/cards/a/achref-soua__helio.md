# achref-soua/helio

⭐ 20 · TypeScript · AGPL-3.0 · 推送 2026-06-29 · [GitHub](https://github.com/achref-soua/helio) · 个人维护

**开源自托管营销自动化平台：CDP、旅程编排、邮件与 AI 副驾驶**

面向营销团队的自托管增长平台：统一客户数据（CDP）、事件管道（浏览器 SDK→Redpanda→ClickHouse）、可视化细分、跨渠道旅程编排（邮件/SMS/WhatsApp/Web 推送/应用内消息，基于 Temporal 持久化工作流）、活动与分析、轻量 CRM 与导入迁移工具。组织各自接入自有 SMTP/Twilio 及 AI 提供商（OpenAI/Anthropic/Groq/NVIDIA NIM/Ollama 或 OpenAI 兼容本地服务），AI 副驾驶可从一句话生成分段、旅程与邮件草稿，并支持上传自有 ONNX/XGBoost 流失模型。提供 helio CLI 驱动 Docker 的一命令安装，AGPL-3.0 许可，免费不限联系人数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多租户架构，Postgres 行级安全隔离与组织级 API key
- 基于 Temporal 的持久化旅程编排，发送节点防重复投递
- AI 副驾驶生成分段/旅程/邮件草稿，支持接入自有 AI 提供商与自有流失模型（ONNX/XGBoost）
- MCP server 将平台能力暴露为工具供外部 AI agent 调用

## 适用场景

- 替代按联系人收费的 SaaS，自托管管理客户数据与营销旅程
- 统一邮件、短信、WhatsApp、站内信等多渠道自动化触达
- 从 HubSpot/Mailchimp/Klaviyo 一键迁移联系人

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L52: - ✅ **AI copilot** — describe a segment, journey, or on-brand email in a sentence and get a working draft; predicti
> L53: - ✅ **Bring your own AI** — each organization picks its provider (OpenAI, Anthropic, Groq, NVIDIA NIM, Ollama, or a

## 星数曲线

```mermaid
xychart-beta
    title "achref-soua/helio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-31 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b636fb59659e` · [字段定义](../../DATASET.md)*
