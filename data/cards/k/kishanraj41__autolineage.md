# kishanraj41/autolineage

⭐ 92 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/kishanraj41/autolineage) · 个人维护

**Python ML 管线的数据血缘自动追踪库：一行 import 记录全链路操作**

通过 import 时 monkey-patch 挂钩 pandas（65 个钩子）、scikit-learn（175 个）与 PySpark（49 个）操作，零代码改动记录从 read_csv 到 f1_score 的完整操作级血缘图；提供异常检测、指标退化根因定位、基线指纹比对，可导出 JSON/DOT/Mermaid/HTML 及 OpenTelemetry spans。面向需要可复现性与调试能力的 ML 开发者。限制：单进程追踪、monkey-patch 对框架版本敏感、C 扩展内部操作不可见、仅支持 Python。以 pip 包形式发布，附 Colab 快速体验。

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

- import autolineage.auto 一行接入，自动挂钩 pandas/sklearn/PySpark 共 289 个操作
- 异常检测与根因定位：识别导致指标退化的具体操作行
- 导出交互式 HTML、Graphviz DOT、Mermaid 及 OpenTelemetry spans
- 插件式架构：新增库支持约 200 行代码，不改核心

## 适用场景

- 模型指标突然崩坏时定位管线中的具体出错操作
- 为 ML 管线建立可审计的操作级数据血缘记录
- 跨运行对比基线指纹，发现行数或指标异常

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3:  Zero-code data lineage for Python ML pipelines.
> L4: One import. Every pandas, scikit-learn and PySpark operation tracked, anomalies caught, root cause localized.
> L40: ML pipelines fail silently. A model whose F1 drops from 0.97 to 0.00 invites hours of `print(df.shape)` debugging. 

## 星数曲线

```mermaid
xychart-beta
    title "kishanraj41/autolineage 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-27 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `d872ab03f7d6` · [字段定义](../../DATASET.md)*
