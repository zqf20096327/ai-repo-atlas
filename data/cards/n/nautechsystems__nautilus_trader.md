# nautechsystems/nautilus_trader

⭐ 30,299 · Rust · LGPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/nautechsystems/nautilus_trader) · [官网](https://nautilustrader.io) · 组织维护

**给量化交易者的多资产多市场 Rust 原生交易引擎**

以 Rust 为核心、Python 作为策略控制面的开源交易引擎，覆盖研究、确定性回测模拟与实盘执行，采用事件驱动架构并通过 PyO3 提供 Python 绑定。通过模块化适配器接入带 REST API 或 WebSocket 的任意交易场所，当前集成覆盖 CEX/DEX 加密货币交易所、外汇/股票/期货/期权等传统市场及博彩交易所。预编译 wheel 安装无需 Rust 工具链；v2 迁移期 v1 仅接收关键安全回补，当前仍处活跃开发、版本间可能出现破坏性变更。

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

- 同一策略代码可在回测与实盘系统间复用
- Rust 核心（mimalloc/tokio）+ Python 控制面的双层架构
- 20+ 交易所与数据商的模块化适配器集成表
- 支持 128 位高精度与 64 位标准精度两种数值模式

## 适用场景

- 加密货币与传统市场的多场所量化策略回测与实盘执行
- 训练强化学习交易 agent（RL/ES）
- 通过适配器接入自有 REST/WebSocket 数据源构建交易系统

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L30: NautilusTrader is an open-source, production-grade, Rust-native engine for multi-asset,
> L63: - **AI Training**: Engine fast enough to train AI trading agents (RL/ES).
> L85: Python bindings are provided via PyO3 for the Rust-native v2 runtime.

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `0af742ba4dce` · [字段定义](../../DATASET.md)*
