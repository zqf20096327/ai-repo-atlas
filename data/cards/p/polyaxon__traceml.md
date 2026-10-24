# polyaxon/traceml

⭐ 533 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/polyaxon/traceml) · 组织维护

**面向 Polyaxon 的 ML 实验跟踪与数据摘要引擎**

Polyaxon 生态的跟踪与可视化引擎：在 Python 脚本或深度学习框架（Keras、PyTorch、TensorFlow、Fastai、PyTorch Lightning、HuggingFace）中通过 tracking 模块与 Callback 记录指标、输入输出、模型与工件（artifacts），支持离线模式（环境变量或 is_offline 参数）。另提供 DataFrameSummary 对象，扩展 pandas describe() 输出列级统计（计数、缺失、类型等）。部分功能（跨列摘要、可视化、目录与版本管理）标注为 WIP 未实现。以 pip 安装的 Python 库形式提供，跟踪功能需额外安装 polyaxon。

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

- Keras/PyTorch/TensorFlow/Fastai/PyTorch Lightning/HuggingFace 六类框架集成 Callback
- 离线模式跟踪实验运行（POLYAXON_OFFLINE 或 is_offline）
- DataFrameSummary 扩展 pandas describe() 的列级统计与类型汇总
- 跟踪 metrics、inputs/outputs、模型与可视化工件

## 适用场景

- 在深度学习实验中记录与跟踪训练指标和模型工件
- 对 pandas DataFrame 做列级统计摘要与数据探查
- 无 API 环境下离线记录 Polyaxon 实验运行

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L10: Engine for ML/Data tracking, visualization, explainability, drift detection, and dashboards for Polyaxon.
> L53: ## Integration with deep learning and machine learning libraries and frameworks

## 星数曲线

```mermaid
xychart-beta
    title "polyaxon/traceml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 532 --> 534
    line [533, 533]
```

2026-10-18 533 → 2026-10-24 533（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `c555fd99b8b3` · [字段定义](../../DATASET.md)*
