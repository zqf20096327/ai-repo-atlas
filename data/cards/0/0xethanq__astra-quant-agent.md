# 0xethanq/astra-quant-agent

⭐ 393 · Python · NOASSERTION · 推送 2026-10-03 · [GitHub](https://github.com/0xethanq/astra-quant-agent) · [官网](https://www.astraquant.tech) · 个人维护 · 中文 README

**多 LLM 委员会决策 + Python 风控的自主加密交易系统**

AstraQuant 是运行 15 分钟交易周期的自主加密交易系统：宏观、趋势、微观结构、逆向四个 LLM 分析席位独立评估并合成下单意图，确定性 Python 代码对杠杆、仓位、止损持有绝对否决权，成交后经 OKX 原生 OCO 条件单全云端止损。执行引擎仅支持 OKX API，Binance/Gate.io 仅为推荐返佣链接。默认以 demo 纸面模式启动，提供 Docker Compose 与裸机两种部署，后端 Python、前端 Vue 3，含 Prompt Studio、自我演化、Prometheus/Grafana 可观测性等模块。AGPL-3.0 + Commons Clause 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四席位多模型议会合成下单意图，含 Paranoid Veto/加权多数等仲裁模式
- 确定性 Python 风控闸门（最大 6 仓位、同向上限、回撤熔断、杠杆钳制 2-5x）
- CVD/OBI/资金费率/IV 偏斜/VWAP 等微观结构因子持续计算
- Prompt 缓存架构：90% 以上静态上下文共享前缀，降低 token 成本

## 适用场景

- 在 OKX 上运行多模型分析的自动化合约交易
- 以纸面模式验证 LLM 交易策略后再接实盘
- 通过管理面板调整风险参数、提示词与模型席位配置

## 场景标签

`金融量化` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12: AstraQuant combines large language models (macro, technical, and microstructure analysis) with deterministic Python
> L59: 1. **Hypothesis vs. Enforcement**: LLMs analyze market structure and propose order intents; deterministic Python co
> L69: 2. Multi-Model Council (LLMs)   ──> Macro, Trend, and Microstructure seats analyze & synthesize order intent

## 星数曲线

```mermaid
xychart-beta
    title "0xethanq/astra-quant-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 380 --> 391
    line [381, 388, 390]
```

2026-10-18 381 → 2026-10-22 390（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `38baa42daecd` · [字段定义](../../DATASET.md)*
