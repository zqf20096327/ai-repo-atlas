# vadiminshakov/marti

⭐ 20 · Go · Apache-2.0 · 推送 2026-09-22 · [GitHub](https://github.com/vadiminshakov/marti) · 个人维护

**Go 加密货币交易机器人：DCA 与 AI 策略**

用 Go 编写的加密货币交易机器人，支持 Binance、Bybit 等多个交易所，提供 DCA（定投）与 AI 两种交易策略；AI 策略可对接任意 OpenAI 兼容 API。通过 go install 安装，默认以 Web UI 启动，无配置时提供交互式向导；也可用 --cli 以终端向导运行。支持用历史数据跑测试（go test historytest）。README 声明仅供教育与研究用途，交易有亏损风险。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持多交易所（Binance、Bybit）的 DCA 与 AI 交易策略
- AI 策略兼容任意 OpenAI 兼容 API
- 默认 Web UI，无配置时启动交互式向导；另有 --cli 终端模式
- 提供基于历史数据的回测测试（historytest）

## 适用场景

- 在 Binance/Bybit 上自动执行定投（DCA）策略
- 接入 OpenAI 兼容 API 运行 AI 驱动的交易策略
- 用历史数据测试策略表现

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L9: Marti is a cryptocurrency trading bot with *DCA* and *AI* strategies for multiple exchanges.
> L36: The AI strategy works with any OpenAI-compatible API.

## 星数曲线

```mermaid
xychart-beta
    title "vadiminshakov/marti 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5eb6e1a81443` · [字段定义](../../DATASET.md)*
