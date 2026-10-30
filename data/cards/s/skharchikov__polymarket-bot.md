# skharchikov/polymarket-bot

⭐ 38 · Rust · 推送 2026-10-25 · [GitHub](https://github.com/skharchikov/polymarket-bot) · [官网](https://t.me/Polymarket_rs_bot) · 个人维护

**Polymarket 预测市场自动交易机器人：ML 集成模型 + LLM 信号**

Rust Cargo workspace 中的两个独立交易机器人：trading-bot 通过 XGBoost/LightGBM 等集成模型（Python FastAPI sidecar，每 24 小时在约 3000 个已结算市场上重训）对预测市场打分，结合贝叶斯锚定、LLM 相关性检查与 Kelly 仓位管理自动下注；copy-trading-bot 每分钟轮询 Polymarket 排行榜镜像头部交易者。两者均有 Telegram 接口，实时 WebSocket 价格监控触发重评估。README 明确声明为研究学习项目、不适用于生产。部署方式为 Docker Compose（6 个服务：Postgres、模型服务、两个 bot、Prometheus、Grafana）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 29 特征工程 + XGBoost/LightGBM/HistGBM 等集成模型与元学习器
- 三个并行策略（激进/平衡/保守）各 €300 独立资金池与 Kelly 仓位
- Brier 分数追踪模型相对市场的表现（skill 指标）
- Telegram 命令与通知体系（下注/结算/价格波动/日报）

## 适用场景

- 学习研究预测市场量化交易与 ML 信号管线
- 通过 Telegram 查看仓位、模型精度与组合统计
- 镜像 Polymarket 排行榜头部交易者的仓位

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: A Cargo workspace containing two independent Rust trading bots for Polymarket prediction markets, backed by a shared
> L7: - **trading-bot** — ML-driven signals (XGBoost ensemble + LLM consensus + Bayesian updating)
> L43: 3. **XGBoost ensemble** — scores markets via local pure-Rust XGBoost or Python sidecar (XGBoost + LightGBM + HistGB

## 星数曲线

```mermaid
xychart-beta
    title "skharchikov/polymarket-bot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-30 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `41e4e194311d` · [字段定义](../../DATASET.md)*
