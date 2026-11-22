# jagres0039/hermes-market-skills

⭐ 10 · Python · MIT · 推送 2026-05-30 · [GitHub](https://github.com/jagres0039/hermes-market-skills) · 个人维护

**为 Hermes AI agent 提供加密货币/印尼股票/外汇大宗商品市场分析技能**

三个独立技能包（crypto、saham_idn、forex_comm），各自带数据源、分析逻辑与 CLI；共享 TA 绘图与 LLM 摘要辅助模块。功能含行情读取、TA 分析、recommend 推荐引擎（多周期共振、风险档位门槛）、SMC 结构信号叠加（摆动/市场结构/订单块/FVG/流动性扫荡/溢价折价区）及无前视偏差的 walk-forward 回测。输出 JSON 到 stdout，图表落盘；由 Hermes agent 读取 JSON 组合自然语言回复（默认印尼语）。

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

- recommend 引擎：多时间框架共振、风险档位与 |score|/RR 门槛自动降级为 WAIT/HOLD
- SMC 结构信号规则引擎投票叠加，纯 pandas/numpy 无额外依赖
- walk-forward 回测，next_open 入场、确定性离线可复现输出
- 可选 Telegram 频道只读接入与 RSS 新闻情绪加权聚合

## 适用场景

- 让 Hermes agent 用印尼语或英语触发关键词获取 BTC、IDX 股票、黄金等行情分析
- 对加密与外汇规则引擎做历史回测并查看逐笔与聚合指标
- 聚合新闻 RSS 与 Telegram 频道消息做市场情绪评分

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L10: Market-analysis skills for the Hermes AI agent. Three independent skills covering the asset classes the agent (Gres
> L89: Output is always JSON to stdout. Charts are saved to `OUT_DIR` (default `/tmp/hermes-charts/`) and the path is incl

## 星数曲线

```mermaid
xychart-beta
    title "jagres0039/hermes-market-skills 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-08 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `cd7be51c33af` · [字段定义](../../DATASET.md)*
