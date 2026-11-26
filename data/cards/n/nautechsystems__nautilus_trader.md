# nautechsystems/nautilus_trader

⭐ 31,820 · Rust · LGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/nautechsystems/nautilus_trader) · [官网](https://nautilustrader.io) · 组织维护

**Rust 原生事件驱动交易引擎，供量化交易开发者研究回测与实盘执行**

NautilusTrader 是开源的多资产、多场所交易系统引擎，Rust 核心 + Python 控制面（PyO3 绑定），同一策略与执行算法代码可在确定性模拟回测与实盘执行间复用。通过模块化 adapter 接入任何 REST API 或 WebSocket 数据源，内置加密货币 CEX/DEX、外汇、股票、期货、期权与博彩交易所适配器清单。支持高级订单类型、OCO/OUO/OTO 条件单、纳秒级历史数据回测，并称可训练强化学习交易 agent。v2 迁移期 v1 仅做安全回补。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 16,214 位贡献者
- 涨星:近 1 天 **+116**(自 20261016 起算)
- 安装:pypi 包 `nautilus_trader` 月下载 353,140
- 平台:WINDOWS / MACOS / LINUX · 协议:—

## 能力要点

- Rust 核心 + Python 控制面，PyO3 绑定，预编译 wheel 安装无需 Rust 工具链
- 模块化 adapter 接入 20+ 交易所与数据源（Binance、Interactive Brokers、Polymarket 等）
- 纳秒分辨率历史数据回测与实盘共用同一策略代码
- 支持 IOC/FOK/GTC 等多种 Time in force 与 OCO/OUO/OTO 条件单

## 适用场景

- 加密货币与多资产策略的回测与实盘部署
- 在统一架构下做做市与跨场所套利策略
- 训练强化学习交易 agent 并迁移到实盘

## 场景标签

`金融量化` `强化学习` · 领域:学习与行业

## 证据(README 行号)

> L30: NautilusTrader is an open-source, production-grade, Rust-native engine for multi-asset,
> L63: - **AI Training**: Engine fast enough to train AI trading agents (RL/ES).
> L56: - **Portable**: Runs on Linux, macOS, and Windows. Deploy using Docker.

## 星数曲线

```mermaid
xychart-beta
    title "nautechsystems/nautilus_trader 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 30543 --> 31936
    line [30659, 30711, 30816, 30894, 30944, 31000, 31038, 31074, 31102, 31135, 30711, 31369, 31438, 31462, 31485, 31508, 31529, 31558, 31597, 31636, 31667, 31686, 31710, 31726, 31745, 31765, 31820]
```

2026-10-24 30,659 → 2026-11-26 31,820（+1,161）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d30d3eee9dbe` · [字段定义](../../DATASET.md)*
