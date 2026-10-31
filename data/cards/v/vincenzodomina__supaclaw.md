# vincenzodomina/supaclaw

⭐ 61 · TypeScript · MIT · 推送 2026-03-15 · [GitHub](https://github.com/vincenzodomina/supaclaw) · [官网](https://github.com/vincenzodomina/supaclaw) · 个人维护

**基于 Supabase 内置能力的 OpenClaw 简化版 agent 运行环境**

完全构建于 Supabase 内置原语之上的个人 agent 平台：数据库、存储、认证、日志、cron 与边缘运行时均由 Supabase 提供，入站事件先持久化排队再由 worker 处理，支持重试与幂等。安全设计上不接触凭证、Bash 在模拟或白名单环境运行、破坏性操作需审计可回滚。提供安装脚本与 5 分钟快速启动（需 Supabase CLI、Deno、Docker 与 AI API key），功能含多渠道接入、记忆混合检索、文件/网络/Cron/Bash 工具与 Skills。v0.2.0 的 CLI Bash、连接器与 Web UI 尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 数据库/存储/认证/cron/边缘运行时全部使用 Supabase 原生原语
- 事件先持久化排队，worker 处理带重试与幂等语义
- 多渠道支持（Telegram/Slack/Teams/Discord 等）
- 记忆表 + 混合检索（FTS + pgvector）

## 适用场景

- 在已有 Supabase 账号上运行或自托管个人 agent
- 通过 Telegram/Slack 等渠道与 agent 交互
- 用 SQL 与 Supabase 面板直接检查 agent 的消息与任务数据

## 场景标签

`Agent 框架` `AI 助手` · 领域:Agent 开发

## 证据(README 行号)

> L5: Built entirely on Supabase built-in features. Use within your Supabase account or fully self-host.
> L29: - **One control plane:** Database, storage, auth, logs, cron, and edge runtime are all native Supabase primitives t
> L32: - **Serverless worker loop:** Webhook ingest and agent execution run as edge functions, with cron as a durable back

## 星数曲线

```mermaid
xychart-beta
    title "vincenzodomina/supaclaw 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-31 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `684feed2da37` · [字段定义](../../DATASET.md)*
