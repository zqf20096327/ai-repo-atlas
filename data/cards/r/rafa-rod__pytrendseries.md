# rafa-rod/pytrendseries

⭐ 167 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/rafa-rod/pytrendseries) · 个人维护

**时间序列趋势检测库：识别涨跌趋势并计算回撤指标**

pytrendseries 是一个 Python 库，读取 pandas.DataFrame 格式的时间序列（如股价、月度销售、温度），在指定窗口内检测上升趋势与下降趋势，输出每段趋势的峰谷日期、时间跨度与 drawdown。另提供最大回撤（可按非重叠窗口）、当前回撤、time underwater、回撤序列可视化等函数，并可生成 drawdown at risk 所需的回撤序列。get_trends_labels 函数将价格数据转为离散标签列（1/-1/0，支持自定义字符串标签），用于监督学习分类问题的目标变量构造。经 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- detecttrend 在指定窗口内检测上涨/下跌趋势，输出峰谷日期与 drawdown
- maxdrawdown 支持整体序列或非重叠窗口的最大回撤计算
- calculate_current_drawdown 与 calculate_time_under_water 提供当前回撤与水下时间指标（含 Recovered/Ongoing 状态）
- get_trends_labels 生成离散标签列，支持数值/字符串/二分类自定义标签

## 适用场景

- 检测股价等时间序列的历史趋势段并计算各段回撤
- 构造监督学习分类任务的标签列（涨/跌/无趋势）
- 获取回撤序列以计算 drawdown at risk

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L49: Detection of trends could be used in machine learning algorithms such as classification problems like binary (1 = u
> L221: ## Why use this for Machine Learning?

## 星数曲线

```mermaid
xychart-beta
    title "rafa-rod/pytrendseries 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 166 --> 168
    line [167, 167]
```

2026-10-18 167 → 2026-10-31 167（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `eb1b773514bb` · [字段定义](../../DATASET.md)*
