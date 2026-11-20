# badhope/moneyhelper

⭐ 104 · Python · MIT · 推送 2026-11-19 · [GitHub](https://github.com/badhope/moneyhelper) · [官网](https://badhope.github.io/moneyhelper/) · 个人维护 · 中文 README

**自托管记账软件：一句话自动生成凭证、对账并结账**

自托管财务软件，覆盖个人与企业两侧：一句话生成多笔分录，支持微信支付/支付宝/银行 CSV/PDF 对账单/发票二维码与 OCR 导入；企业侧提供多租户、复式总账（科目表、期间、过账/冲销、试算平衡、期间锁定）、报销与采购到付款流程、银行对账。关键机制是确定性计算引擎产出全部数字，模型只负责措辞；每个数字携带来源记录。周末自动结账与定时任务无人值守运行，能力经 MCP 暴露给外部 agent。数据存本地 SQLite，无遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性计算引擎产出全部数字，模型仅负责措辞，数字附带溯源记录
- 复式总账：科目表、期间锁定、过账/冲销、试算平衡
- 微信支付/支付宝/银行 CSV/PDF/发票二维码及 OCR 原生导入
- 通过 MCP 暴露全部能力，Claude/Codex 等 MCP 客户端可驱动记账

## 适用场景

- 一句话把日常消费自动记成多笔分录
- 家用与公司账共用一套安装而不混账
- 月底自动过账凭证并锁定期间
- 用 MCP 客户端以对话方式查询和操作账目

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: Self-hosted finance software that keeps the books for you. Write one sentence — it books the entry, reconciles the b
> L19: Here the split is the other way round: a deterministic calculation engine fills in every figure, and the model is o
> L31: **Personal.** One sentence becomes several entries — `lunch 45, taxi 28` is two transactions, not one. WeChat Pay, 
> L33: **Enterprise.** Multiple tenants, departments and memberships. A real double-entry general ledger: chart of account


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `6ab0d2c25011` · [字段定义](../../DATASET.md)*
