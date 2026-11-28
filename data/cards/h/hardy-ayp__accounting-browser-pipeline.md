# hardy-ayp/accounting-browser-pipeline

⭐ 3 · Python · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/hardy-ayp/accounting-browser-pipeline) · 个人维护

**企业 ERP 浏览器自动化流水线：抓取报表、入库 SQL 并做财务对账**

端到端 Python 流水线，通过 Lightpanda/Chrome CDP 驱动浏览器从 Web ERP 批量下载电子表格与 PDF 报告，用 MD5/SHA-256 校验与 Magic Bytes 验证文件真实性，随后动态推断 SQL 表结构入库，并执行金额与数量双维度对账（5 轮匹配引擎、余额证明公式）与企业主表更新。强调零数据伪造：不注入人工平衡数，每个报告数字引用来源文档、工作表与行号。提供 SKILL.md 供 AI agent 直接加载，仓库含单元测试与示例用法。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Lightpanda/Chrome CDP 浏览器自动化，支持会话持久化与 AJAX/模态框处理
- Magic Bytes 与加密校验和去重，拦截伪装成报表的错误页面
- 动态 SQL 模式推断，DECIMAL(18,4) 精度与批量参数化插入
- 金额/数量双维度 5 轮匹配对账与余额证明公式

## 适用场景

- 每日自动从 30 家门店的 ERP 门户批量下载销售、应付、库存报表
- 将下载的报表自动入库 SQL 并与总账/明细账对账找差异
- 在不破坏公式的前提下批量刷新企业多工作表主数据

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L9: An end-to-end autonomous pipeline connecting web ERP browser crawling (Lightpanda / Chrome CDP), automated spreadshe
> L132: ## 🤖 Using as an AI Agent Skill
> L134: This repository includes a compliant SKILL.md file. Any AI agent (such as Antigravity, Claude Code, or custom Open

## 星数曲线

```mermaid
xychart-beta
    title "hardy-ayp/accounting-browser-pipeline 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `c0ae9b265634` · [字段定义](../../DATASET.md)*
