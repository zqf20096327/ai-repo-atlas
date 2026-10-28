# TradingGoose/TradingGoose.github.io

⭐ 81 · TypeScript · AGPL-3.0 · 推送 2026-04-22 · [GitHub](https://github.com/TradingGoose/TradingGoose.github.io) · [官网](https://tradinggoose.github.io/) · 组织维护

**面向个人股票分析与组合管理的多 AI Agent 交易平台**

TradingGoose 是开源的 AI 交易工作流平台：多个专业 Agent（宏观/市场/新闻/社媒/基本面/风险分析）协同分析事件并生成交易建议，Portfolio Manager Agent 结合用户 Alpaca 账户与风险约束生成最终订单，通过 Alpaca API 执行（支持模拟与实盘）。支持定时再平衡、多股并发分析、RBAC 权限与 Supabase 认证。自部署需 Supabase CLI、Node.js 18+、Alpaca 账户及外部 Perplefina 研究层实例。多 Agent 架构改编自 TauricResearch/TradingAgents，AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Agent 协同分析（宏观/市场/新闻/社媒/基本面/三档风险）
- Portfolio Manager Agent 按仓位与风险约束生成订单并经 Alpaca 执行
- 定时自动再平衡（日/周/月）与模拟交易模式
- 可配置多 AI 提供商（OpenAI/Anthropic/Google/DeepSeek）含故障转移

## 适用场景

- 让 AI Agent 分析个股新闻与技术面并生成交易建议
- 自动化管理投资组合并按计划再平衡
- 通过模拟交易测试多 Agent 交易策略

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L25: TradingGoose focuses on **event-driven trading strategy and analysis** that harnesses the power of AI agents and Al
> L33: Once analysis agents provide their recommendations, the **Portfolio Manager AI agent** takes over to:
> L63: - **Live Trade Execution**: Real order execution through Alpaca Markets (paper and live trading)

## 星数曲线

```mermaid
xychart-beta
    title "TradingGoose/TradingGoose.github.io 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 79 --> 82
    line [80, 81, 81]
```

2026-10-18 80 → 2026-10-28 81（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `82ea52d89bec` · [字段定义](../../DATASET.md)*
