# Boom-Vitt/boombignose-erp

⭐ 53 · TypeScript · AGPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/Boom-Vitt/boombignose-erp) · 组织维护 · 中文 README

**面向泰国中小企业的开源 ERP（CRM/销售/采购/库存/财务）**

基于 Next.js 16 + Supabase（Postgres、行级安全）的开源单组织 ERP，覆盖仪表盘、CRM、报价开票、采购、库存、报销、项目与工时、报表与自动化。内置泰国税务特性：单据上的 VAT 与预扣税（1–5%）、THB 金额、Asia/Bangkok 时区；明确定位非总账系统，法定记账对接 FlowAccount/PEAK/Xero。AI 部分为通过 OpenRouter 的交易摘要、跟进草稿与会议纪要导入（需配置 API key），以及 n8n 自动化集成。社区版 AGPL/商业双许可，Pro 版商业授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 报价→发票→交付→回款在单一数据库上流转
- VAT、1–5% 预扣税、THB 与曼谷时区内置
- Supabase 行级安全按 org_id 隔离，金额以整数 satang 存储
- 通过 OpenRouter 提供 AI 交易摘要与跟进草稿，n8n 出入站自动化

## 适用场景

- 两人小店到多团队公司统一管理销售、采购、库存与开票
- 在仪表盘查看现金、消耗率、跑道、MRR 与加权销售管线
- 员工提交报销、经理审批，可计费工时一键转草稿发票

## 场景标签

 · 领域:企业管理软件/ERP

## 证据(README 行号)

> L21: BoomBigNose ERP runs sales, purchasing, inventory, projects and billing for a business on one database. It is built
> L39: - **Automation and AI**: Reusable automation templates, scheduled follow-up reminders, an outbox that delivers even
> L169: Community Edition is dual-licensed under AGPL-3.0-only or a separately agreed Commercial license. Pro code in `ee/

## 星数曲线

```mermaid
xychart-beta
    title "Boom-Vitt/boombignose-erp 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25"]
    y-axis "stars" 51 --> 54
    line [52, 53, 53]
```

2026-10-23 52 → 2026-10-25 53（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `a516dea442c7` · [字段定义](../../DATASET.md)*
