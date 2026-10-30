# FlarePriceAlert/Flare

⭐ 22 · TypeScript · MIT · 推送 2026-09-04 · [GitHub](https://github.com/FlarePriceAlert/Flare) · [官网](https://flaremoves.com/) · 个人维护

**对 Robinhood 加密货币价格告警做上下文分类的告警看板**

运行于 Pons 的加密货币价格告警应用：监控 Robinhood 上跟踪的加密资产（如 LINK、XRP、ETH、BTC 等），在触发条件命中后调用模型层对走势分类（延续、 unwind、挤压、低质量噪音），输出分类标签、操作员注记与严重度，供操作员决定升级或忽略。提供告警数量上限、波动率防护等风控项。技术栈为 TypeScript，使用 Claude Agent SDK 构建，需配置 ANTHROPIC_API_KEY，以 git clone 加 Bun 运行源码方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 触发后分类：延续/unwind/挤压/噪音等走势标签与操作员注记
- 五级信号质量阶梯（early watch 到 noise）
- 5 种触发类型：price_above/price_below/pct_change/volatility_spike
- 告警上限、分类步骤、波动率防护等风控配置

## 适用场景

- 减少加密货币价格告警的注意力浪费，先分类再决定是否处理
- 区分突破延续与清算噪音类走势
- 通过 Pons 启动并查看带解释的告警看板

## 场景标签

 · 领域:加密货币/监控工具

## 证据(README 行号)

> L6: Flare does not just tell you that a level hit. It tells you whether the move looks like continuation, liquidation no
> L50: - a classification such as continuation, unwind, squeeze, or low-quality noise
> L12: Built with Claude Agent SDK

## 星数曲线

```mermaid
xychart-beta
    title "FlarePriceAlert/Flare 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8e4c0452d798` · [字段定义](../../DATASET.md)*
