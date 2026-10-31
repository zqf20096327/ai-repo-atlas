# wa91h/local-ai-toolkit

⭐ 15 · Go Template · MIT · 推送 2026-05-17 · [GitHub](https://github.com/wa91h/local-ai-toolkit) · 个人维护

**自托管本地 AI 技术栈：LiteLLM 网关 + n8n 工作流 + Open WebUI**

通过 Docker Compose 或 Kubernetes Helm 一键部署的自托管 AI 技术栈，打包三个服务：LiteLLM（OpenAI 兼容 LLM API 网关与管理 UI）、n8n（可视化工作流自动化）、Open WebUI（聊天界面），共享一个 PostgreSQL 16 实例（承载 n8n 与 litellm 两个数据库）。LiteLLM 初始不含任何模型，用户自行在 LiteLLM UI 注册 OpenAI/Anthropic/Vertex/Groq 或本地模型服务等提供商，Open WebUI 通过 scoped virtual key 接入网关。README 明确声明默认配置无 TLS、无认证代理、无密钥管理与备份策略，不适用于生产环境，并提供 Production Checklist。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Docker Compose 与 Kubernetes Helm 两种部署方式，支持按 profile 禁用单个服务
- LiteLLM 作为 OpenAI 兼容网关统一接入多提供商模型，Open WebUI 仅获 host 不获 master key
- 单一 PostgreSQL 16 实例共享托管 n8n 与 litellm 数据库，init 脚本幂等
- 支持外接数据库（RDS/Cloud SQL）、Ingress、模型运行时注册并持久化到 Postgres

## 适用场景

- 在本地或内网快速搭建带网关、工作流与聊天界面的完整 AI 技术栈
- 统一管理多个 LLM 提供商的密钥与调用，向内部应用提供 OpenAI 兼容 API
- 配合 n8n 构建 AI 工作流自动化

## 场景标签

`模型网关` `工作流自动化` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L3: A self-hosted AI stack bundling an LLM gateway, workflow automation, and a chat UI — all backed by a shared PostgreS
> L13: |**LiteLLM**|OpenAI-compatible LLM API gateway|http://localhost:4000|

## 星数曲线

```mermaid
xychart-beta
    title "wa91h/local-ai-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `463afdb6951b` · [字段定义](../../DATASET.md)*
