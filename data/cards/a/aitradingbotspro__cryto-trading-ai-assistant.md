# aitradingbotspro/cryto-trading-ai-assistant

⭐ 108 · Python · 推送 2026-03-14 · [GitHub](https://github.com/aitradingbotspro/cryto-trading-ai-assistant) · 个人维护

**面向手动加密交易者的 AI 风控守卫：监测风险与情绪化交易**

监控型工具而非自动交易程序：通过交易所 API 或 webhook 接收交易事件，评估仓位大小、杠杆与当日盈亏，校验进出场是否符合自定义策略规则，检测报复性交易、过度交易等情绪化模式，并在入场前扫描波动率、清算簇与资金费率等市场风险。告警经 Telegram/Discord 推送并持久化到仪表盘。不执行或关闭任何交易。技术栈为 Python/FastAPI 后端、Scikit-learn（PyTorch 可选）、React/TypeScript 仪表盘，数据默认存 SQLite。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 风险规则监控：单笔风险、日亏损、杠杆、仓位大小告警
- 情绪化交易检测：报复性交易、过度交易、亏损后加仓、非时段交易
- 策略规则校验与入场前市场风险扫描（波动率、清算簇、资金费率）
- Telegram/Discord 告警推送与 React 仪表盘，不执行任何交易

## 适用场景

- 手动交易时获得风险规则违规与杠杆超限的实时告警
- 通过 TradingView webhook 接入交易事件并接收守卫分析
- 复盘交易质量并获得 AI 反馈评分与建议

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L5: Strategy Guardian AI monitors your trading in real time: it validates risk rules, detects emotional trading patterns
> L20: Strategy Guardian AI **does not execute trades**. It acts as a watchful layer around your activity:

## 星数曲线

```mermaid
xychart-beta
    title "aitradingbotspro/cryto-trading-ai-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-27 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ef5a97d87f99` · [字段定义](../../DATASET.md)*
