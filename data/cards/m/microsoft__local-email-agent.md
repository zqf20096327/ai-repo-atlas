# microsoft/local-email-agent

⭐ 21 · Python · MIT · 推送 2026-01-31 · [GitHub](https://github.com/microsoft/local-email-agent) · 组织维护

**微软本地邮件助手：Phi-4 本地模型代发邮件与管日程**

基于 Foundry Local 运行 Phi-4 本地模型的邮件/日历 agent 示例项目：通过 Microsoft 365 MCP Server 收发邮件与管理日历，Outlook 邮件经 Azure OpenAI 生成嵌入后存入 PostgreSQL+pgvector 支持语义搜索；LangGraph 编排 supervisor 与子 agent，敏感操作（发邮件、改日程）需人工审批。前端为 Next.js Agent Inbox，后端 FastAPI + SSE 流式。限制：Foundry Local 不支持 Linux；嵌入依赖 Azure OpenAI 凭证。

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

- Foundry Local 本地运行 Phi-4，可换任意模型
- 发邮件/改日程等敏感操作需 human-in-the-loop 审批
- PostgreSQL+pgvector 语义邮件搜索
- Phi-4 无原生工具调用，用 LangChain 结构化输出强制 JSON

## 适用场景

- 本地模型代为收发邮件、管理 Outlook 日程
- 语义搜索历史邮件内容
- 学习 supervisor+子 agent 与 HITL 审批的 agent 架构

## 场景标签

`AI 助手` `语义搜索` · 领域:对话与助手

## 证据(README 行号)

> L3: An intelligent email assistant powered by Microsoft's Phi-4 local model, featuring a modern web UI, human-in-the-loo
> L11: - **Foundry Local** (runs entirely on your machine), this project shows phi-4 but you can use any model you like

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/local-email-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `fd6d8aefd7e2` · [字段定义](../../DATASET.md)*
