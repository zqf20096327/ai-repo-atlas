# pushkarkumarvats/OmniQuant

⭐ 18 · Python · NOASSERTION · 推送 2026-02-20 · [GitHub](https://github.com/pushkarkumarvats/OmniQuant) · 个人维护

**Python/Rust/TS 混合的量化研究与交易仿真平台**

面向量化研究者的策略研究与仿真系统：原生 Rust 订单管理系统（BTreeMap 限价订单簿、ITCH 5.0 解析、事件日志）、FIX 4.2/4.4/5.0SP2 会话引擎、TWAP/VWAP/POV/IS 执行算法、11 项盘前风控检查。Python 层提供动量、做市（Avellaneda-Stoikov）、统计套利策略与 LSTM/Transformer/XGBoost 等 ML alpha 模型，另含 Next.js 监控面板。README 以表格区分已实现与仅规划的功能（如 DPDK、kdb+ 为 planned），并声明仅限研究与仿真、禁止未经验证直接用于实盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust OMS：BTreeMap 订单簿、10+ 订单类型、ITCH 5.0/OUCH 4.2 协议解析
- FIX 4.2/4.4/5.0SP2 会话生命周期与 TWAP/VWAP/POV/IS 执行算法
- LSTM/Transformer/XGBoost/ARIMA-GARCH 等 ML alpha 训练与预测流水线
- MVO/HRP/风险平价/Black-Litterman 组合优化与 11 项盘前风控检查

## 适用场景

- 在历史数据上回测动量、做市、统计套利等策略
- 研究与仿真高频订单簿撮合和执行算法
- 用 ML 模型生成 alpha 信号并做组合优化

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L8: **Quantitative trading research & simulation platform** — a hybrid Python / Rust / TypeScript system for strategy re
> L38: |ML — LSTM, Transformer, XGBoost, Ensemble, ARIMA-GARCH|✅ Working|Training + prediction pipelines|
> L97: ### ML Alpha Models

## 星数曲线

```mermaid
xychart-beta
    title "pushkarkumarvats/OmniQuant 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7c09e4692f59` · [字段定义](../../DATASET.md)*
