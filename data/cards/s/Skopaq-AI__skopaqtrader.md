# Skopaq-AI/skopaqtrader

⭐ 23 · Python · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/Skopaq-AI/skopaqtrader) · [官网](https://skopaq-ai.github.io/skopaqtrader/) · 组织维护

**面向印度股市的开源多智能体 LLM 量化交易平台**

基于 TradingAgents（Apache 2.0）并扩展的交易平台：用 LangGraph 编排 15 个 agent（分析师团队、多空研究员、风控、交易员），支持 NSE/BSE 印度股票，通过 INDstocks 券商 API 执行，含模拟盘到实盘路径、自主交易守护进程、三层持仓监控与日亏损熔断等安全机制。多模型分层可按角色指定 Gemini/Claude/Grok，Ollama 可作本地回退；另提供 Claude Code MCP 服务器（18 个工具）与交互式 REPL。需 Python 3.11+ 与至少一家 LLM 的 API key，README 声明仅供教育研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 编排的 15-agent 分析与交易流水线，含多空辩论与风控
- INDstocks 券商集成，支持模拟盘与实盘（NSE/BSE）
- Claude Code MCP 服务器：18 个交易工具与 /analyze、/trade 等斜杠命令
- 多模型分层 + Ollama 本地回退，含 Redis 语义缓存与 Supabase 记忆

## 适用场景

- 在印度股市（NSE/BSE）上运行 AI 多智能体分析并执行模拟/实盘交易
- 通过 Claude Code 或 CLI 对话式下达分析与交易指令
- 研究多 agent LLM 在量化交易中的信号生成与风险管理

## 场景标签

`金融量化` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: **An open-source AI algorithmic trading platform for Indian equities**
> L27: SkopaqTrader extends the TradingAgents multi-agent LLM framework with Indian equity market support, multi-model tie
> L36: - **Multi-agent analysis** — Analyst team (market, news, social, fundamentals), bull/bear researchers, risk manager

## 星数曲线

```mermaid
xychart-beta
    title "Skopaq-AI/skopaqtrader 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-27 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d677f8d39515` · [字段定义](../../DATASET.md)*
