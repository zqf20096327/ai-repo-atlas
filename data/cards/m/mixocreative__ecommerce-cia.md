# mixocreative/ecommerce-cia

⭐ 14 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/mixocreative/ecommerce-cia) · [官网](https://github.com/mixocreative/ecommerce-cia#readme) · 组织维护 · 中文 README

**台湾电商金流串接与完整性稽核的 AI Agent Skill**

运行在 Claude Code 与 OpenAI Codex 中的 agent 技能，对交易型电商系统做『串接稽核』：沿结账→金流→Callback→订单→库存→出货→退款→后台整条链路在测试环境实际下单验证，检查跨边界不变量违反，输出附证据的追溯矩阵与缺口清单。另提供新手引导模式，以逐题问答带无经验者从零串接蓝新/绿界/LINE Pay。深度分 Screen/Walk/Full 三档，探针默认仅连测试环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在测试环境实际下单，验证金流 Callback、库存、退款、后台开关联动
- 三层级检查（函数逻辑/串接关系/生命周期规则）与七种刻意故障演练
- 新手引导模式逐题带新手从零串接蓝新、绿界、LINE Pay
- 覆盖台湾金流（NewebPay/ECPay/PAYUNi/TapPay/超商取货付款/统一发票）及 Stripe/Adyen webhook 签章

## 适用场景

- 电商上线前请 AI agent 稽核金流与库存串接，拦截掉单、重复释库存等缺陷
- 没写过金流的初次建站者，从零串接蓝新或绿界
- 核对后台付款方式开关、Callback 重送幂等性等行为是否与预期一致

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: ### 電商金流與系統完整性稽核 · a skill for Claude Code and OpenAI Codex
> L162: A skill for Claude Code and OpenAI Codex that audits a transactional e-commerce system as a **viable system** in S

## 星数曲线

```mermaid
xychart-beta
    title "mixocreative/ecommerce-cia 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `be0f14fb6168` · [字段定义](../../DATASET.md)*
