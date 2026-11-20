# xCodeWraith/CryptomarketAI

⭐ 12 · 推送 2026-11-19 · [GitHub](https://github.com/xCodeWraith/CryptomarketAI) · 个人维护

**给交易者：Telegram 上的 GPT-4o 图表技术分析 Agent**

基于 n8n 工作流的对话式加密货币技术分析 Agent：用户在 Telegram 发送如 "Analyze BTCUSD" 的消息，工作流经 Chart-img API 从 TradingView 抓取含 RSI/MACD 指标的 K 线图，由 GPT-4o Vision 解析图表，LangChain 保留最近 10 条对话上下文并驱动 Tool-Calling Agent 完成编排，输出趋势方向、支撑阻力位、动量状态与短期情景。部署依赖 Docker 运行 n8n 及 Telegram、OpenAI、Chart-img 三个 API Key；README 声明仅供信息与研究用途，不构成投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GPT-4o Vision 解析 TradingView K 线图（含 14 周期 RSI/MACD）
- LangChain Tool-Calling Agent 在 n8n 中编排自动分析流程
- LangChain 记忆保留最近 10 轮对话上下文支持追问
- 提供 n8n 工作流 JSON 导入与模块化子工作流配置步骤

## 适用场景

- 在 Telegram 里直接对话请求 BTCUSD 等品种的图表技术分析
- 基于已有对话上下文追问短期交易情景
- 用 n8n 搭建 24/7 运行的自动化行情分析流水线

## 场景标签

`工作流自动化` `金融量化` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L9: > **Conversational AI trading agent delivering Wall Street-grade technical analysis directly on Telegram.**
> L19: * **Autonomous Decision-Making:** Orchestrated via a dynamic LangChain Tool-Calling Agent inside n8n.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `ffb60075c311` · [字段定义](../../DATASET.md)*
