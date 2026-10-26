# crmkit/crmkit

⭐ 43 · Go · MIT · 推送 2026-08-13 · [GitHub](https://github.com/crmkit/crmkit) · [官网](https://crmkit.ai) · 组织维护

**面向 AI agent 的无界面 CRM 后端：纯 HTTP API 驱动**

用 Go 编写的 headless CRM 服务器（crmkitd），无 UI、无 SDK，通过纯文本/JSON 的 HTTP API 供 AI agent（ChatGPT、Claude、Cursor 等）读写联系人、公司、交易、工单、任务、活动等记录；提供稳定句柄、带提示的 4xx 错误、OTP 登录、追加式审计日志、多租户与套餐限额，以及 MCP 连接器（OAuth 2.1）与可安装的 agent skills。数据层为纯 Go SQLite，编译为单个静态二进制部署。项目处于 0.x 阶段，1.0 前 API 与存储结构可能发生不兼容变更；另有托管版 crmkit.ai。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 纯文本/JSON 双格式 HTTP API，无 UI 无 SDK，agent 直接驱动
- MCP 连接器（POST /mcp，OAuth 2.1 + PKCE），单工具暴露全部 API
- 纯 Go SQLite，CGO_ENABLED=0 编译为单个静态二进制
- 预置 digest/import/backup/inbox-sync 等 agent skills（npx skills 安装）

## 适用场景

- 让 AI agent 维护销售线索、客户与交易的共享记录系统
- 多个 agent 与团队成员并发读写同一份 CRM 数据并有审计轨迹
- 市场监测 agent 长期跟踪目标公司与竞争情报实体

## 场景标签

 · 领域:业务软件/CRM

## 证据(README 行号)

> L5: **An agent-first CRM, built for AI agents to drive over plain HTTP.** Headless
> L175: crmkit also speaks the **Model Context Protocol** at `POST /mcp`, so it plugs

## 星数曲线

```mermaid
xychart-beta
    title "crmkit/crmkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `109240125cd2` · [字段定义](../../DATASET.md)*
