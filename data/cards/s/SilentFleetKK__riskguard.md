# SilentFleetKK/riskguard

⭐ 67 · Python · MIT · 推送 2026-07-10 · [GitHub](https://github.com/SilentFleetKK/riskguard) · 个人维护 · 中文 README

**量化交易的开源风控中间件：仓位上限、回撤熔断与审计**

面向个人量化交易者的 Python 风控层库，定位为数据→研究→回测→风控→执行五层中的风控标准件。提供单笔仓位闸、回撤熔断（减仓永远放行）、策略隔离期、组合敞口限制、Kelly/波动率/固定比例动态仓位、后台 RiskMonitor 实时哨兵、哈希链防篡改审计（可选 HMAC）、SQLite 状态持久化、每日体检摘要与压力测试。核心零依赖，带 CLI 与三档预设，可接 backtesting.py/vectorbt 及 Alpaca 或自研 Broker。明确不做异常检测与行情预测。尚未发布 PyPI，需 git 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单笔仓位闸、回撤熔断、组合敞口限制等规则由系统强制执行
- Kelly/VolatilityTarget/FixedFractional 动态仓位计算
- 哈希链审计日志（可选 HMAC）与 SQLite 状态持久化，熔断扛得住重启
- RiskOverlay 可接入 backtesting.py / vectorbt，一键跑套风控对比

## 适用场景

- 我在用 backtesting.py/vectorbt 回测，想加一层不绑定框架的风控
- 我让 AI agent 帮我交易，但需要一道它绕不过去的规则闸门
- 想让熔断、仓位纪律在进程重启后依然生效并留下可验证的审计记录

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L17: 量化交易的五层积木——**数据 → 研究 → 回测 → 风控 → 执行**——数据有 OpenBB、研究有 Qlib、回测有 backtesting.py/vectorbt、执行有 Alpaca,**唯独风控层没有一个成熟的开源标
> L240: - 想让 AI agent 帮你研究、下单,但**不敢让它直接碰真实资金**的——RiskGuard 就是那道 AI 绕不过去的闸门
> L251: 5. **AI 动脑,系统守纪律**:AI 可研究/写码/挑毛病,但每笔真实指令必须先过写死的风控规则。

## 星数曲线

```mermaid
xychart-beta
    title "SilentFleetKK/riskguard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-28 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `52634ba49e12` · [字段定义](../../DATASET.md)*
