# ing-bank/popmon

⭐ 512 · Python · MIT · 推送 2026-01-09 · [GitHub](https://github.com/ing-bank/popmon) · [官网](https://popmon.readthedocs.io/) · 组织维护

**监测 Pandas/Spark 数据集稳定性的 Python 库，检测数据漂移并告警**

popmon 按时间切片对特征生成分箱直方图，用统计检验比较各时间片之间以及相对参考数据集的分布稳定性，覆盖数值、有序、类别特征及二维直方图（可跟踪特征间相关性）。可按业务规则自动标记趋势、偏移、峰值、离群与异常并触发告警。结果默认输出为自包含 HTML 报告，直方图数据可存入数据库并接入 Grafana/Kibana 等工具。支持 pandas 与 Spark 数据框，Spark 使用需配置 histogrammar jar。由 ING 银行团队维护。

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

- 按时间切片分箱生成直方图并用统计检验比较分布稳定性
- 业务规则自动标记趋势/偏移/峰值/离群/异常并告警
- 输出自包含 HTML 报告，直方图数据可接入 Grafana/Kibana
- 同时支持 pandas 与 Spark 数据框，提供模块化可定制数据管线

## 适用场景

- 生产环境监测特征数据随时间的分布漂移
- 模型上线前对比当前数据与训练参考数据的稳定性
- 将漂移告警接入现有 Grafana 仪表盘与通知流程

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7: `popmon` is a package that allows one to check the stability of a dataset.
> L14: `popmon` can **automatically flag** and alert on **changes observed over time**, such
> L168: To give an example, one could store the histogram data in a PostgreSQL database and load that from Grafana and ben

## 星数曲线

```mermaid
xychart-beta
    title "ing-bank/popmon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 511 --> 513
    line [512, 512]
```

2026-10-18 512 → 2026-10-22 512（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3ba8c1a88c97` · [字段定义](../../DATASET.md)*
