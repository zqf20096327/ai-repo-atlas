# different-ai/agent-bank

⭐ 255 · TypeScript · MIT · 推送 2026-04-03 · [GitHub](https://github.com/different-ai/agent-bank) · [官网](https://zerofinance.ai) · 组织维护

**面向 AI agent 的 CLI 优先银行服务：开票、转账、对账**

为 AI agent 提供真实银行账户访问的 CLI-first 金融产品：通过 `zero` CLI（npm 包 agent-bank）脚本化完成发票创建与发送、ACH/IBAN 转账提案（带审批门）、收据匹配对账，闲置资金自动生息。支持使用官方托管版（0.finance）或自行 Fork 自托管（LITE_MODE.md，需 Privy 配置与 Safe 钱包）；自托管迁移涉及 Safe 资产转移与 gas 费。开发阶段：发票、IBAN/ACH 账户、储蓄账户已上线，借记/信用卡未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- zero CLI 将发票、转账、对账全流程脚本化
- 转账提案带审批门（approval gates）
- 可 Fork 自托管，含托管版迁移指南
- monorepo 含 CLI、Web 应用与储蓄自动化智能合约包

## 适用场景

- 让 agent 在终端创建并发送发票
- 通过 CLI 提议 ACH/IBAN 转账并走审批流程
- 将收据附加到交易并自动对账

## 场景标签

 · 领域:金融科技/Agent 基础设施

## 证据(README 行号)

> L7: > CLI-first banking for AI agents. Give your agents access to a bank account to create invoices, propose bank transf
> L13: 0 Finance gives agents a real bank account with a CLI-first workflow:
> L33: The CLI package is `agent-bank`, and the binary is `zero` (alias: `zero-bank`) for agent workflows.

## 星数曲线

```mermaid
xychart-beta
    title "different-ai/agent-bank 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 253 --> 256
    line [254, 255, 255]
```

2026-10-18 254 → 2026-10-26 255（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c8a742d63239` · [字段定义](../../DATASET.md)*
