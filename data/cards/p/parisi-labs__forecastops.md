# parisi-labs/forecastops

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/parisi-labs/forecastops) · [官网](https://pypi.org/project/forecastops/) · 组织维护

**本地优先的预测（forecast）评测与可观测层：捕获、验证、比对预测**

面向已有预测代码的本地优先评测与可观测工具：在 `.predict()` 后加一行捕获预测产物，本地以 Parquet 存储原始数据点、DuckDB 写入运行元数据，计算 horizon 感知的多类指标（MAE/WAPE/bias/coverage/pinball 等），支持按任意分类列切片、滚动起点回测分组、运行间 diff 与机器可读诊断输出，并提供只读本地 UI 浏览器。不训练模型、无需云账号、默认无外呼网络（UI 绑定 127.0.0.1）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一行代码捕获预测，Parquet+DuckDB 本地存储
- horizon 感知指标与按任意分类列切片（MAE/RMSE/WAPE/sMAPE/bias/coverage/pinball）
- 滚动起点回测分组与任意两运行间 diff/skill 基准对比
- 只读本地 UI 与面向 agent/脚本的 fops diagnose 机器可读诊断

## 适用场景

- 生产预测流水线中持续捕获并验证预测质量
- 对比多个模型或回测实验组的误差与稳定性
- 按地区/事件类型等维度切片诊断预测误差来源

## 场景标签

`模型评测` `MLOps` · 领域:评测与运维

## 证据(README 行号)

> L8: ForecastOps is a local-first observability and evaluation layer for
> L26: serves a read-only local UI. It does not train forecasting models, require a

## 星数曲线

```mermaid
xychart-beta
    title "parisi-labs/forecastops 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-28 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `fb26043685ee` · [字段定义](../../DATASET.md)*
