# guillempuche/batuda

⭐ 10 · TypeScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/guillempuche/batuda) · [官网](https://batuda.co) · 个人维护

**自托管 CRM：内置引用可溯源的研究代理，帮找联系人并发邮件跟进**

以研究引擎为核心的 CRM：代理检索公开网页，产出带页面引用与置信度的结构化发现，落入公司、联系人、任务、不可变互动日志等 CRM 记录中。每次发现必须解析到实际访问过的页面并存档快照，研究结果以提案队列形式等待人工应用；按用户设置每次与每月预算上限，search/scrape/enrich 等供应商为环境变量选择的角色端口，各带回退链与零成本本地 stub。通过 MCP（OAuth 2.1）供任意客户端访问，或经自带 Web 应用操作；邮件从用户自己的 IMAP/SMTP 收件箱收发。需 Node 24、pnpm、Postgres 与 S3 兼容桶，自行构建部署，无一键安装包。

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

- 每条发现必须携带来源页引用，页面快照存档可回查
- 供应商为可插拔端口（search/scrape/registry/enrich/verify/report），含零成本 stub
- 按用户的每次/每月预算上限与分层缓存控制开销
- 90+ 意图级类型化 MCP 工具，Postgres RLS 多租户隔离

## 适用场景

- 小型代理公司跟踪客户提案与后续跟进
- 独立创始人管理种子轮投资人名单
- 招聘者筛选候选人并记录沟通轨迹
- 不想按席位付费、主要经 AI 对话使用 CRM 的用户

## 场景标签

 · 领域:CRM/销售与客户管理

## 证据(README 行号)

> L3: **A research agent with a CRM around it.**
> L118: - **Research as the core capability.** Server-side agent loop with a mandatory citation ledger, a guard chain over


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `55c8a119301d` · [字段定义](../../DATASET.md)*
