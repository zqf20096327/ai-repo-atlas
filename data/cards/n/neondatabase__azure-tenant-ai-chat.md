# neondatabase/azure-tenant-ai-chat

⭐ 14 · TypeScript · MIT · 推送 2026-03-05 · [GitHub](https://github.com/neondatabase/azure-tenant-ai-chat) · [官网](https://multiuser-rag-g0e0g3h6ekhtf7cg.germanywestcentral-01.azurewebsites.net/) · 组织维护

**部署在 Azure 的多用户私有 RAG 聊天应用，Neon Postgres 存储**

基于 Azure Chat Solution Accelerator 修改的多用户 RAG 聊天解决方案：在用户 Azure 订阅内部署私有聊天租户，用 Neon Serverless Postgres 实现每用户独立数据库隔离，支持 OAuth 登录（Google/GitHub/Microsoft Entra ID）、PDF 文档对话、聊天历史、自定义 persona、语音交互（Azure Speech）与 Azure OpenAI 生成回复。本地运行需 Node.js 18 与 npm，部署提供 Azure Developer CLI 与 Azure Portal 两种途径，依赖 Azure 账户及多项 Azure 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每用户独立 Neon 数据库实现聊天数据隔离
- 支持 PDF 等文档的 RAG 对话与自定义 prompt 模板
- OAuth 多登录方式（Google/GitHub/Microsoft Entra ID）
- Azure Speech 支持多语言语音交互

## 适用场景

- 组织在自有 Azure 订阅内部署私有 AI 聊天租户
- 让成员基于内部 PDF 文档进行问答
- 需要应用与数据库双层数据隔离的多用户聊天场景

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L13: - 🧠 **AI-Powered Conversations**: Chat with documents such as PDF. You can also build your own prompt templates.
> L35: |**Azure OpenAI**|Provides models like GPT-4o for generating AI-powered conversational responses and vector embeddi

## 星数曲线

```mermaid
xychart-beta
    title "neondatabase/azure-tenant-ai-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `860056c42cc4` · [字段定义](../../DATASET.md)*
