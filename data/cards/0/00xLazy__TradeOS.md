# 00xLazy/TradeOS

⭐ 23 · TypeScript · MIT · 推送 2026-03-11 · [GitHub](https://github.com/00xLazy/TradeOS) · 个人维护 · 中文 README

**让 AI agent 用自然语言操作 100+ 交易所的 OpenClaw 交易技能**

以 TypeScript 编写的 OpenClaw Skill：将自然语言指令转换为加密货币交易所操作，基于 CCXT 支持 100+ 中心化交易所，覆盖下单（市价/限价/止损/止盈）、多所组合追踪、PnL 报告、DCA 定投、条件单、跨所套利扫描与资金费率监控。内置密钥保险库（AES-256-GCM 加密、拒绝提币权限密钥）、风险限额与预览确认流程；数据全部本地存储，无云端依赖。通过 git clone 到技能目录并 npm 安装构建使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言下单，覆盖 100+ 交易所（CCXT）
- AES-256-GCM 密钥加密、强制预览确认、拒绝提币权限密钥
- DCA 定投、条件单、跨所套利扫描、资金费率监控
- 数据全部本地存储，零云端依赖

## 适用场景

- 通过对话让 AI agent 在多个交易所执行交易
- 设定自动化定投与价格触发条件单
- 聚合查看多交易所资产与盈亏报告
- 扫描跨交易所价差寻找套利机会

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L26: TradeOS is an OpenClaw Skill that transforms natural language into secure, auditable exchange operations across **1
> L73:     User["User (Natural Language)"] --> OpenClaw["OpenClaw Agent"]

## 星数曲线

```mermaid
xychart-beta
    title "00xLazy/TradeOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `adf58f837726` · [字段定义](../../DATASET.md)*
