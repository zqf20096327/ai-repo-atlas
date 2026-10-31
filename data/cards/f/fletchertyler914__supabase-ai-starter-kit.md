# fletchertyler914/supabase-ai-starter-kit

⭐ 15 · Shell · NOASSERTION · 推送 2026-05-23 · [GitHub](https://github.com/fletchertyler914/supabase-ai-starter-kit) · [官网](https://github.com/fletchertyler914) · 个人维护

**本地优先的 Supabase+n8n+Ollama 自托管 AI 应用脚手架**

面向独立开发者、顾问与团队的自托管 AI 产品基础栈：以 Docker Compose 打包 Supabase 自托管版（Auth/Postgres/pgvector/Realtime/Storage/Edge Functions）、Kong 网关、n8n 工作流自动化与 Ollama 本地模型，一条 npm run setup 命令完成环境生成、启动、种子工作流（17 个 n8n 工作流）、模型拉取与验证。预置本地聊天、pgvector RAG 摄取/查询、对话式构建工作流等模板及 ai_calls 用量记录。README 声明本地默认配置非生产安全，需自行管理密钥与部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令 setup：生成 .env、启动 Docker、种子 17 个 n8n 工作流、拉取模型并验证
- pgvector + nomic-embed-text 的文档摄取与语义查询 RAG webhook
- NodeBot Builder：通过对话让本地 agent 构建 n8n 工作流（11 个辅助子工作流）
- 测试套件覆盖 health/auth/db/RAG/Ollama，并带备份恢复与 Cloudflare Tunnel 脚本

## 适用场景

- 在自有基础设施上搭建带认证与向量检索的私有 RAG 系统
- 为 AI 产品原型提供可复用的客户起步栈（auth+工作流+本地模型）
- 在接入托管服务前先在本地评估自托管 AI 基础设施

## 场景标签

`工作流自动化` `RAG` · 领域:效率与自动化

## 证据(README 行号)

> L7: This repo gives you a batteries-included Supabase + n8n + Ollama foundation that runs locally, ships as Docker Compo
> L23: - **Supabase self-hosted** for Auth, Postgres, pgvector, Realtime, Storage, and Edge Functions.
> L27: - **Docker Compose** for repeatable local development, demos, and single-server deployment.

## 星数曲线

```mermaid
xychart-beta
    title "fletchertyler914/supabase-ai-starter-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2ae7d987606f` · [字段定义](../../DATASET.md)*
