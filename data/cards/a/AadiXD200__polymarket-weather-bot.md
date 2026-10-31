# AadiXD200/polymarket-weather-bot

⭐ 14 · Python · 推送 2026-04-05 · [GitHub](https://github.com/AadiXD200/polymarket-weather-bot) · 个人维护

**Polymarket 天气衍生品市场的自动量化交易机器人**

面向预测市场交易者的自主量化交易系统：从 Open-Meteo 拉取 GFS/ECMWF/ICON/GEM/Météo-France 五个 NWP 模式最新预报，计算集合均值与离散度，融合 ASOS 实时观测做临近订正，用 Student-t 分布对温度区间积分得出概率，与 CLOB 市场中间价之差超过自适应阈值时入场；仓位采用 25% 分数 Kelly 并设单笔 15 USDC 上限。提供 CLI 与 systemd 部署单元，含纸面与实盘模式。README 自称实验性研究项目，纸面业绩不保证实盘结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 五模式集合预报 + ASOS 观测临近订正生成温度区间概率
- 多重入场过滤（边缘阈值、NO 价格带、集合标准差门、盘口深度、组合上限）
- 25% 分数 Kelly 仓位 sizing，单笔硬上限 15 USDC
- 通过 Polymarket CLOB API 提交订单，附纸面交易与 systemd 部署单元

## 适用场景

- 在 Polymarket 天气市场上按模型-市场价差自动下注
- 用纸面模式在不投入真实资金的情况下测试策略
- 以 daemon 方式在云主机上持续运行扫描与结算

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L3: An autonomous quantitative trading system that identifies and exploits pricing inefficiencies in Polymarket weather 
> L67: 1. **Forecast ingestion** — Fetches the 5 latest NWP runs for the target ICAO station from Open-Meteo: GFS, ECMWF, 
> L73: 4. **Bucket probability** — Integrates a Student-t distribution (ν=4, fat tails) over the temperature bucket `[lo, 

## 星数曲线

```mermaid
xychart-beta
    title "AadiXD200/polymarket-weather-bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2ddd3db3b828` · [字段定义](../../DATASET.md)*
