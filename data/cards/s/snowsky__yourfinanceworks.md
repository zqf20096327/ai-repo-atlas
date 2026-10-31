# snowsky/yourfinanceworks

⭐ 15 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/snowsky/yourfinanceworks) · [官网](https://www.yourfinanceworks.com) · 个人维护

**面向开发者与小微企业的自托管 AI 财务管理平台**

自托管的多租户财务记账 SaaS：覆盖发票开具、支出管理、银行对账与经营分析。AI 功能包括 OCR 票据/银行流水提取与分类、AI 发票模板、欺诈检测与风险评分、以及基于 MCP 的自然语言商业数据查询助手。技术上采用 FastAPI + PostgreSQL（租户独立数据库）+ Redis + Kafka 后端与 React + TypeScript 前端，Docker Compose 本地编排。采用 AGPL-3.0 与商业许可的双许可拆分模式，商业目录需付费授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OCR 票据与银行流水自动提取、智能分类与一键对账
- MCP 支持的 AI 助手，自然语言查询商业数据
- 多租户架构，租户级数据库隔离与角色权限控制
- 插件系统与投资组合管理插件

## 适用场景

- 小企业自助开票、收账提醒与报销审批
- 自动处理票据和银行对账，减少手工记账
- 通过 AI 助手用自然语言查询财务与经营数据

## 场景标签

`OCR` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L9: YourFinanceWORKS transforms financial futures for businesses and individuals through AI-powered automation of invoic
> L50: - OCR-powered receipt processing with high-accuracy data extraction
> L64: - MCP-backed AI assistant for natural language business queries

## 星数曲线

```mermaid
xychart-beta
    title "snowsky/yourfinanceworks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2ddc90052d73` · [字段定义](../../DATASET.md)*
