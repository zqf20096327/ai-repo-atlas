# seoes/proval

⭐ 117 · TypeScript · AGPL-3.0 · 推送 2026-10-24 · [GitHub](https://github.com/seoes/proval) · [官网](https://proval.app) · 个人维护

**自托管 LLM 代码审查 agent：接入 Git 平台自动审查 PR 与 issue**

部署在自有服务器上的 LLM 代码审查服务：通过 webhook 接收 GitLab、Forgejo、GitHub 事件，读取 diff 后按变更文件分组，派出子 agent 探索代码库并产出按严重度分组的审查意见，支持行内评论、issue 回复、线程回复与含 token 用量的活动看板。模型通过 OpenAI 兼容 Chat Completions API 接入，可用 Ollama、llama.cpp 等本地模型。以 Docker Compose/Docker/Kubernetes 方式部署，使用 Bun/Hono/SvelteKit/SQLite 构建，AGPL-3.0 许可。作者声明项目尚处早期，认证、SSO、速率限制等功能在计划中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持 GitLab、Forgejo、GitHub，含行内评论（单行/多行）
- 子 agent 分组审查变更文件，探索代码库捕捉跨文件问题
- OpenAI 兼容 API 接入，支持 Ollama、llama.cpp 等本地模型
- 活动看板记录审查/回复及 token 用量

## 适用场景

- 在内网或 homelab 中用本地模型自动审查 pull request
- 让 AI 回复 issue 并跟踪讨论上下文
- 私有化部署代码审查，不依赖外部 SaaS

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5: A Self-hosted LLM code review agent. Connect it to your Git host, bring your own model, and let it review pull reque
> L28:  When a pull request gets a meaningful push (or a draft becomes ready), Proval reads the diff, groups changed files

## 星数曲线

```mermaid
xychart-beta
    title "seoes/proval 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 115 --> 118
    line [116, 117]
```

2026-10-18 116 → 2026-10-25 117（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5ccdcc959855` · [字段定义](../../DATASET.md)*
