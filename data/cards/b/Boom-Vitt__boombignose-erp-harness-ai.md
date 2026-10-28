# Boom-Vitt/boombignose-erp-harness-ai

⭐ 54 · TypeScript · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/Boom-Vitt/boombignose-erp-harness-ai) · [官网](https://boom-vitt.github.io/boombignose-erp-harness-ai/) · 个人维护 · 中文 README

**面向泰国中小企业的开源 ERP：销售/采购/库存/项目/财务一体化**

基于 Next.js 16 + Supabase（Postgres 与 RLS）的开源 ERP，把 CRM、报价/发票（含 VAT 与预扣税）、采购、库存、项目工时、费用审批与现金流仪表盘放在同一数据库中；面向泰国企业优先（THB、Asia/Bangkok 时区），也适用于多人团队。AI 部分为交易摘要、跟进草稿与会议记录整理，通过本地 Ollama（默认 127.0.0.1:11434，拒绝远程主机）调用，未运行时不调用云模型。Community 版 AGPL-3.0 或商业许可，Pro 版为商业许可。非总账系统，法定记账、报税、薪资与制造不在范围内。提供 Windows/macOS/Linux 桌面安装包（未签名）或 pnpm 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 报价→发票→交付单据流转与冻结的已开发票
- VAT 与 1/2/3/5% 预扣税计算、THB 整数萨当存储
- 全表 org_id + 强制行级安全（RLS）多组织隔离
- AI 交易摘要/跟进草稿/会议记录走本地 Ollama，拒绝远程主机

## 适用场景

- 把 CRM、项目、库存和开票记录合并到一个系统避免数据不一致
- 泰国业务处理带 VAT 与预扣税的单据
- 费用审批、工时计费与项目利润核算
- 通过 n8n webhooks 连接自动化流程

## 场景标签

 · 领域:企业管理软件/ERP

## 证据(README 行号)

> L35: BoomBigNose ERP runs sales, purchasing, inventory, projects and billing for a business on one database. It is built
> L53: - **Automation and AI**: Reusable automation templates, scheduled follow-up reminders, an outbox that delivers even


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bd804d3266b6` · [字段定义](../../DATASET.md)*
