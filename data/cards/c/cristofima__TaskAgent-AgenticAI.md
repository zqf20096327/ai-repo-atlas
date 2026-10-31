# cristofima/TaskAgent-AgenticAI

⭐ 14 · C# · MIT · 推送 2026-02-16 · [GitHub](https://github.com/cristofima/TaskAgent-AgenticAI) · [官网](https://cristopher-coronado-portfolio.vercel.app/projects/task-agent-agentic-ai) · 个人维护

**AI 任务管理助手：自然语言对话管理任务的全栈示例应用**

基于 .NET 10 + Next.js 16 的任务管理应用，通过自然语言对话完成任务的增删改查、分析摘要与下一步建议。AI 部分由 Microsoft Agent Framework 与 Azure OpenAI（GPT-4o-mini）驱动，采用 AG-UI 协议以 SSE 流式输出，配 Azure AI Content Safety 内容安全过滤与 OpenTelemetry/.NET Aspire 可观测性。数据层为 SQL Server + PostgreSQL 双库，共 225+ 测试。项目需自备 Azure 资源，作为系列技术文章的配套示例工程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言完成任务 CRUD、过滤分析与上下文建议
- AG-UI 协议 + SSE 的流式聊天界面与持久化会话
- Azure Content Safety 内容过滤，被拦截内容不入库
- SQL Server + PostgreSQL 双库持久化，225+ 测试（单元/集成/E2E）

## 适用场景

- 用对话方式管理个人任务与待办
- 学习 Clean Architecture 下的 AI Agent 全栈实现
- 参考 Azure OpenAI + 内容安全 + 可观测性的生产化模式

## 场景标签

 · 领域:任务管理/AI Agent 应用

## 证据(README 行号)

> L6: An intelligent task management assistant built with **Microsoft Agent Framework**, **Azure OpenAI**, and **.NET Aspi
> L60: - 💬 **Natural Language Interface**: Talk to your task manager like a person
> L65: - ✅ **Complete CRUD**: Create, read, update, and delete tasks

## 星数曲线

```mermaid
xychart-beta
    title "cristofima/TaskAgent-AgenticAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `6c5e178498e8` · [字段定义](../../DATASET.md)*
