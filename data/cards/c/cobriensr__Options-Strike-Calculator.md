# cobriensr/Options-Strike-Calculator

⭐ 22 · TypeScript · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/cobriensr/Options-Strike-Calculator) · [官网](https://theta-options.com/) · 个人维护

**0DTE SPX 期权分析平台：定价、策略计算与 AI 图表分析**

面向单用户的 0DTE SPX 期权分析工具：给定 SPY/SPX 价格、VIX 与时间，生成 delta 目标行权价表、iron condor / BWB 盈亏（含偏度调整 PoP）、delta 上限建议与 regime 信号目录。接入 Schwab 与 Unusual Whales 实时行情，包含夜间 ML 流水线与多腿分类器等 Python 服务（部署于 Railway）。AI 部分为 Claude Opus 4.7 图表分析端点：读取至多 4 张图表截图，返回结构/入场/对冲建议并注入自改进的经验教训库。前端 React 19 + Vite，后端 Vercel Serverless，数据存 Neon Postgres。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Black-Scholes 行权价、iron condor/BWB 策略计算与偏度调整 PoP
- Claude Opus 4.7 图表分析：读取至多 4 张截图返回结构/入场/对冲方案
- Schwab + Unusual Whales 实时数据接入与 dealer-gamma/GEX 等信号
- 多阶段 ML 流水线与 6,897 个单元测试、Playwright e2e 测试

## 适用场景

- 我在做 0DTE SPX 交易时计算行权价与 iron condor/BWB 策略
- 我想让 AI 读取图表截图并给出结构与对冲建议
- 我需要实时 gamma 流与 regime 信号辅助盘中决策

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: Production-grade 0DTE SPX options analysis platform: Black-Scholes pricing, AI-powered chart analysis (Claude Opus 4
> L44: Given a SPY/SPX price, VIX, and time, the calculator produces delta-targeted strike tables, full iron condor / BWB 

## 星数曲线

```mermaid
xychart-beta
    title "cobriensr/Options-Strike-Calculator 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-29 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d8de071d127a` · [字段定义](../../DATASET.md)*
