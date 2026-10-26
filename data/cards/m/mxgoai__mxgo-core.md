# mxgoai/mxgo-core

⭐ 67 · Python · Apache-2.0 · 推送 2026-03-29 · [GitHub](https://github.com/mxgoai/mxgo-core) · [官网](https://docs.mxgo.ai) · 组织维护

**自托管 AI 邮件处理系统：自动摘要、回复与研究邮件**

可自托管的邮件处理服务，通过 API 接收邮件并异步处理，支持 summary@/reply@/research@/ask@ 四种处理模式，可用 AI 分析 PDF、图片、文档等附件，并通过配置的邮件服务（如 AWS SES）回发结果。支持多 AI 提供商负载均衡（OpenAI、Azure OpenAI、AWS Bedrock、本地 Ollama、自定义端点），基于 Docker Compose 部署，含 RabbitMQ 队列与多 worker 扩展、定时任务与可选搜索/深度研究 API 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- summary/reply/research/ask 四种邮件处理模式
- 附件 AI 分析：PDF、DOCX、XLSX、图片描述等
- 多 AI 提供商负载均衡：OpenAI/Azure/Bedrock/Ollama/自定义端点
- Docker Compose 一键部署，多 worker 扩展与定时任务

## 适用场景

- 自托管部署一套自动摘要和回复邮件的服务
- 让 AI 分析邮件中的 PDF、表格和图片附件
- 定时生成每日邮件摘要报告

## 场景标签

`AI 写作` `文档问答` · 领域:内容生成

## 证据(README 行号)

> L15: - **🧠 Smart Email Processing**: Automatically summarize, reply to, and analyze emails
> L19:  - `summary@`: Generate email summaries
> L20:  - `reply@`: Create smart replies

## 星数曲线

```mermaid
xychart-beta
    title "mxgoai/mxgo-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-26 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d5d10d1d8712` · [字段定义](../../DATASET.md)*
