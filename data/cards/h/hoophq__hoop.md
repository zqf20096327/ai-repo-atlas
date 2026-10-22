# hoophq/hoop

⭐ — · [GitHub]() · 组织维护

**代理数据库流量的开源 sidecar：为 AI agent 做数据脱敏与拦截危险 SQL**

MIT 许可的单二进制 sidecar，部署在 agent 与数据库之间，agent 只需改连接端口。提供四项控制：内存中重写响应的敏感字段（不改请求）、有序 deny 规则的 Guardrails、本地规则先行加模型评分的 Session Analyzer、人工审批 Reviews。支持 PostgreSQL、SQL Server、HTTP 协议；另含控制平面与仍受支持的原有 gateway（RBAC、会话录制等）。控制平面部分功能（如 UI 配置、审批队列）标注未建成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 数据脱敏在内存中重写响应，请求本身不被改动
- Guardrails 以 pgwire 真实错误返回拒绝原因
- Session Analyzer 本地规则先执行，避免无谓模型调用
- 支持 PostgreSQL / SQL Server / HTTP 三种协议

## 适用场景

- 生产环境中约束 AI agent 对数据库的访问
- 防止 agent 执行 DELETE 等破坏性语句
- 对 agent 会话做风险评分并升级人工审批

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L13: **The query runs. The sensitive fields stay hidden.**
> L71: ## The Four Controls
> L89: Wire protocols outlive models, frameworks, and MCP. The sidecar works behind whatever interface your agent uses.

## 星数曲线

```mermaid
xychart-beta
    title "hoophq/hoop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 830 --> 832
    line [831, 831]
```

2026-10-18 831 → 2026-10-21 831（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `6cc18751fa91` · [字段定义](../../DATASET.md)*
