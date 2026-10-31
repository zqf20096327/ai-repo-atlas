# Flow-Research/workstream

⭐ 14 · Python · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/Flow-Research/workstream) · 组织维护

**管理并核验人类与 AI agent 工作成果的贡献治理基础设施**

由协议与实现软件两部分组成：项目上传指南生成版本化策略，贡献者认领任务并提交 ZIP 工作包，系统执行提交前/提交后确定性检查，经人工或自动审核后生成不可篡改的 ContributionRecord 记录，供支付等外部系统使用。后端为 Python/FastAPI 加 Celery/PostgreSQL/Redis/MinIO，通过 Docker Compose 运行，含 Go 编写 CLI 与 MCP 适配器。当前 v0.1 未发布，人工审核与支付交付尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提交前/提交后两级确定性检查与不可变提交存储
- 生成不可直接编辑的 ContributionRecord 永久记录
- 支持人类、AI agent 或两者混合的贡献流程
- 提供 MCP 适配器供 AI agent 读取权限与档案数据

## 适用场景

- 项目方定义策略并核验 AI agent 或人类提交的工作成果
- 为按贡献付费的系统提供可信的贡献记录
- 审计任务的提交、检查与审核全历史

## 场景标签

 · 领域:AI 治理/工作流基础设施

## 证据(README 行号)

> L3: Workstream is software that manages work done by people, AI agents, or both.
> L198: |`mcp_server/`|An MCP (Model Context Protocol) adapter. AI agents can use it to read profile and permission data.|

## 星数曲线

```mermaid
xychart-beta
    title "Flow-Research/workstream 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2bfacaa3706e` · [字段定义](../../DATASET.md)*
