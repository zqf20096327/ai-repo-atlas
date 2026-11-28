# khalilur14103026/crypto-accumulation-scanner

⭐ 18 · HTML · MIT · 推送 2026-11-27 · [GitHub](https://github.com/khalilur14103026/crypto-accumulation-scanner) · 个人维护

**给加密货币交易者的社区版囤积形态扫描机器人，Telegram 推送排名清单**

一个社区驱动的加密货币扫描机器人，周期性扫全市场寻找长时间横盘、波动收缩的 quiet accumulation 形态，经多因子评分（形态质量、OBV、200 EMA、波动挤压、对 BTC 相对强度、资金费率与持仓量）排出候选清单并通过 Telegram/Discord 每 4 小时推送。所有命令可在聊天内使用，配置集中在单一文件，警报自动记录并在 3/7/14 天后复核。目前数据源为 Bybit REST API（经 ccxt），README 明确说明排名仅供参考研究而非交易指令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多因子评分生成排名候选清单（形态/OBV/EMA/波动挤压/相对强度/资金费率）
- Telegram 每 4 小时定时推送，支持 Windows Task Scheduler 无人值守
- 每次警报自动记录并做 3/7/14 天 forward-test 复核
- 提供 listing sniper 模式每 5 分钟监控新上线公告

## 适用场景

- 定时收到全市场囤积形态候选清单而不用盯盘
- 在聊天里对单个币种拉取因子明细与信号读数
- 通过 forward-test 日志回看历史警报表现

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L7: Crypto Accumulation Scanner is a community-built bot that quietly watches the market for coins coiling in long, flat
> L18: 🔍 **Quiet-accumulation detection** — the scanner sweeps the market for coins coiling in long, flat bases with shrin
> L35: - **/crypto-accumulation-scanner** — the headline command. Kicks off a fresh market-wide sweep for coins coiling in


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `66a18814a7b1` · [字段定义](../../DATASET.md)*
