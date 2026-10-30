# QAInsights/Streamlit-JMeter

⭐ 22 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/QAInsights/Streamlit-JMeter) · [官网](https://github.com/QAInsights/Streamlit-JMeter) · 个人维护

**用 Streamlit 执行 JMeter 测试并交互式可视化结果**

基于 Streamlit 构建的 Apache JMeter 图形界面：通过浏览器选择 JMX 测试计划并执行（CLI 模式运行、生成日志），或加载 CSV 结果文件展示开始/结束时间、汇总报告与基于 vega-lite 的交互式图表。面向性能测试工程师。README 声明机器学习异常检测为进行中功能，当前版本仅执行与可视化。限制：仅支持 CSV 结果、图表数量有限、文件名含空格时不执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 浏览器界面选择并执行 JMeter 测试计划（JMX 文件）
- 分析 CSV 结果并展示汇总报告与交互式图表（vega-lite）
- 需设置 JMETER_HOME 环境变量指向本地 JMeter 目录

## 适用场景

- 在浏览器中执行 JMeter 测试计划而无需命令行操作
- 加载 JMeter CSV 结果并生成交互式图表分析性能
- 在 Streamlit 界面中查看测试执行进度与汇总指标

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L14: By integrating Streamlit with Apache JMeter, you can build machine learning models to train to detect anomalies fro
> L40: By leveraging Streamlit with JMeter which brings machine learning capabilities to detect the anomalies and to study
> L112: * This is just a inception version where I experimented the capabilities of `streamlit`. The next big thing is wri

## 星数曲线

```mermaid
xychart-beta
    title "QAInsights/Streamlit-JMeter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6b5513582161` · [字段定义](../../DATASET.md)*
