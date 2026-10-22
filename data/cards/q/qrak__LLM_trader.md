# qrak/LLM_trader

⭐ 135 · Python · MIT · 推送 2026-10-21 · [GitHub](https://github.com/qrak/LLM_trader) · 个人维护

**LLM 驱动的加密货币纸面交易 agent：读图、记忆、反思**

面向加密货币交易者的自主纸面交易代理（默认不涉及真实资金）：生成 1920×1080 K 线图交给多模态模型做视觉形态识别，结合技术指标与 RSS 新闻 RAG 产出交易决策；ChromaDB 向量记忆存储已平仓交易、语义规则与复盘教训，按最近邻检索注入提示词；每 N 笔平仓后运行反思引擎合成规则，并有声明校验（模型自报趋势强度对照实际 ADX）、风险管道（仓位上限、动态 SL/TP、R/R 门槛）。多供应商回退链：DeepSeek 为主，可配置 Gemini、OpenRouter、本地 LM Studio、BlockRun。提供 FastAPI+WebSocket 十标签页监控面板。Python 3.13，git clone + pip 安装，2,419 项回归测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChromaDB 记忆增强：检索最近 3 笔相似交易、学习规则与复盘教训注入提示词
- 视觉 AI 图表分析：1920×1080 K 线图交多模态模型识别形态
- 反思引擎按 surprise ratio 合成最佳实践/反模式规则并持久化
- 多供应商回退链：DeepSeek 主，Gemini/OpenRouter/LM Studio/BlockRun 可配置

## 适用场景

- 在纸面交易中观察 LLM 交易决策过程并通过面板监控
- 用已平仓交易经验驱动的记忆机制迭代交易策略
- 本地或 API 多模型路由下运行自动化行情分析

## 场景标签

 · 领域:金融/加密货币交易

## 证据(README 行号)

> L3: *An autonomous paper-trading agent that reads charts, remembers outcomes and sharpens its strategy from its own clos
> L72: - **📈 Vision AI Chart Analysis** — Generates a **1920×1080 PNG** candlestick chart with indicators and sends it to 
> L84: - **🔀 Multi-Provider AI Routing** — Primary: DeepSeek official API (`deepseek-flash`, accepts charts natively). Con

## 星数曲线

```mermaid
xychart-beta
    title "qrak/LLM_trader 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 132 --> 136
    line [133, 134, 135]
```

2026-10-18 133 → 2026-10-22 135（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `abfcd924679a` · [字段定义](../../DATASET.md)*
