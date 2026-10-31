# mazamaka/polymarket-bot

⭐ 14 · Python · MIT · 推送 2026-03-28 · [GitHub](https://github.com/mazamaka/polymarket-bot) · 个人维护

**面向 Polymarket 预测市场的自主 AI 交易机器人**

基于 Python 3.12/asyncio 与 FastAPI 的 Polymarket 预测市场交易机器人，以 Claude（Opus/Sonnet/Haiku，经 Claude Code CLI）为分析引擎，运行三种策略：AI 错价检测（Haiku 批量筛选 + Opus 五框架深度分析，辅以实时搜索与行情数据）、天气套利（Open-Meteo 16 模型集合预报，基于 12,776 个历史市场回测的入场阈值）、新闻信息套利（SSE 流监听突发新闻，目标 10-30 秒反应）。内置多层风控（仓位上限、止损止盈、频率限制），默认纸面交易模式，支持 Docker Compose 部署。README 声明仅供教育研究用途。

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

- 三种策略：Claude 错价检测、天气套利、新闻信息套利
- 多层风控：仓位 5% 上限、总敞口 60% 上限、止损止盈、频率限制
- 默认纸面交易模式，Docker Compose 部署，FastAPI + WebSocket 仪表盘
- 需要 Claude Code CLI（Max 订阅）作为 AI 引擎

## 适用场景

- 在 Polymarket 预测市场上跑自动化量化/AI 交易
- 先用纸面交易模式回测验证策略
- 监听突发新闻快速响应市场报价

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: An autonomous AI-powered trading bot for Polymarket prediction markets. Uses Claude AI (Opus/Sonnet/Haiku) as the an
> L9: Claude Opus analyzes prediction markets as a Superforecaster using 5 analytical frameworks. The pipeline:
> L53: |AI Engine|Claude Code CLI (Max subscription) -- Opus, Sonnet, Haiku|

## 星数曲线

```mermaid
xychart-beta
    title "mazamaka/polymarket-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `df3208da3304` · [字段定义](../../DATASET.md)*
