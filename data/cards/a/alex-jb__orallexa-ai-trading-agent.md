# alex-jb/orallexa-ai-trading-agent

⭐ 71 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/alex-jb/orallexa-ai-trading-agent) · [官网](https://orallexa-ui.vercel.app) · 个人维护 · 中文 README

**多智能体 AI 交易决策系统：8 源信号融合与辩论式分析，仅纸面交易**

Orallexa 是一个基于 Python + Next.js 的多智能体股票分析系统：9-10 个 ML 模型（RF/XGB/EMAformer/MOIRAI-2/Chronos-2/Kronos 等）与 Polymarket/Kalshi 预测市场等 8 类信号源加权融合，权重按各源历史准确率自适应；4 角色分析师面板加 Bull/Bear/Judge 辩论（Claude Sonnet/Haiku 双层路由），Kelly+ATR 风险定径由独立 agent 完成，输出决策卡、风险计划并通过 Alpaca 下纸面订单。真实资金被硬性门槛（Brier 改进）挡住，全程仅 paper trading。附 Next.js 双语仪表盘与带 Whisper 语音的桌面像素牛教练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 源信号融合，按各源滚动准确率自适应权重
- 4 角色面板 + Bull/Bear/Judge 辩论，双层 LLM 路由控制成本
- 9-10 个 ML 模型（含 Kronos、MOIRAI-2、Chronos-2），全 CPU 运行
- Alpaca 纸面交易 bracket 单，真实资金由 Brier 改进门槛拦截

## 适用场景

- 跑多智能体辩论式的股票分析与纸面交易回测
- 对比多个时序/分类模型在股票方向预测上的 OOS 表现
- 研究 LLM 辩论、信号融合与自适应权重在交易决策中的组合方式

## 场景标签

`多智能体` `金融量化` · 领域:Agent 开发

## 证据(README 行号)

> L29: Orallexa runs a **multi-agent intelligence pipeline**. 4 AI analysts with different risk profiles debate the trade.
> L81: |**8-Source Signal Fusion**|Technical + ML + News + Options + Institutional + Social (Reddit/X) + Earnings/PEAD + P

## 星数曲线

```mermaid
xychart-beta
    title "alex-jb/orallexa-ai-trading-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-30 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e80961971538` · [字段定义](../../DATASET.md)*
