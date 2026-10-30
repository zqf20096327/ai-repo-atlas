# ActiveCampaign/postmark-skills

⭐ 46 · MIT · 推送 2026-09-24 · [GitHub](https://github.com/ActiveCampaign/postmark-skills) · [官网](https://postmark.com) · 组织维护

**Postmark 邮件平台的 AI agent 技能集（5 个技能）**

ActiveCampaign 官方维护的 Postmark 邮件平台 Agent Skills 集合，包含 5 个技能：通过 Postmark API 发送事务性邮件（单个/批量/模板）、处理入站邮件 webhook、管理 Handlebars 服务端模板、配置投递/退信等 webhook 事件，以及邮件送达率与合规最佳实践。安装后 AI 编程 agent 在相关任务中自动调用。需 Postmark 账户与 Server API Token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个技能覆盖发信、入站处理、模板、webhook 与送达率合规
- 支持单个、批量（500 封/批）、bulk 与模板发送
- 覆盖 CAN-SPAM/GDPR/CASL 合规与 SPF/DKIM/DMARC 指引
- npx skills add 一条命令安装，或按技能单独安装

## 适用场景

- 让 AI 编程 agent 直接通过 Postmark 发送事务性邮件
- 搭建回复即工单、邮件转文档的入站处理流程
- 为项目配置退信与投递状态追踪 webhook
- 了解邮件送达率与合规要求

## 场景标签

 · 领域:开发者工具/邮件服务

## 证据(README 行号)

> L11: Agent Skills for the Postmark email platform. Teach AI coding agents how to send transactional email, process inbou
> L37: Once installed, your AI coding agent will automatically use these skills when relevant. Example prompts:

## 星数曲线

```mermaid
xychart-beta
    title "ActiveCampaign/postmark-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-30 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `23fd6cbdc341` · [字段定义](../../DATASET.md)*
