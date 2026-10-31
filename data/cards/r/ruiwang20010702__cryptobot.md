# ruiwang20010702/cryptobot

⭐ 19 · Python · AGPL-3.0 · 推送 2026-02-25 · [GitHub](https://github.com/ruiwang20010702/cryptobot) · 个人维护 · 中文 README

**加密货币永续合约 AI 量化交易系统，AI 工作流生成信号**

面向加密货币永续合约交易的 AI 量化系统：基于 LangGraph 构建 8 节点多角色工作流（4 类分析师、多空研究员辩论、交易决策、ML 过滤、风控审核），整合 16 个数据源，覆盖 10 个 USDT 永续合约交易对，每 30 分钟运行一轮，信号经 Freqtrade 执行。包含 Regime 检测、多策略路由、量化回测与 Walk-forward 验证、全链路风控、LightGBM 信号评分、Telegram 交互与 Web Dashboard。需 Binance API Key 与 DeepSeek（或 OpenAI 兼容）API Key，依赖 Python 3.12、uv 与 TA-Lib C 库，提供 Docker Compose 与 systemd 部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 节点 LangGraph 多角色工作流，每轮约 40 次 LLM 调用
- 16 个数据源与 10 个 USDT 永续合约交易对
- 量化回测含成本模型、Walk-forward 验证与历史回放
- Telegram 11 个命令双向交互与 FastAPI Web Dashboard

## 适用场景

- 自动分析加密永续合约市场并生成交易信号
- 通过 Telegram 查看持仓、信号与风控状态
- 对多策略组合做带成本模型的量化回测

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: 加密货币永续合约 AI 量化交易系统。
> L16: **8 个节点的 LangGraph 状态图**：采集数据 → 筛选币种 → (volatile 时可跳过) 4 分析师分析 → 多空研究员辩论 → 交易决策 → ML 过滤 → 风控审核 → 写入信号。每轮约 40 次 LLM 
> L20: - **AI 多角色协作** — 技术分析师、链上分析师、情绪分析师、基本面分析师、看多/看空研究员、交易员、风控经理

## 星数曲线

```mermaid
xychart-beta
    title "ruiwang20010702/cryptobot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `15df030f6f0a` · [字段定义](../../DATASET.md)*
