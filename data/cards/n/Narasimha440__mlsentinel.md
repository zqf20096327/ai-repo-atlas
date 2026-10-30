# Narasimha440/mlsentinel

⭐ 18 · Python · MIT · 推送 2026-08-24 · [GitHub](https://github.com/Narasimha440/mlsentinel) · 个人维护

**向 MLSentinel 平台上报 ML 模型评估指标与数据质量报告的 Python SDK**

面向 MLSentinel 监控平台的 Python SDK（要求 Python 3.9+），负责本地校验、API key 认证、报告提交与错误转换。提供 auto_report()（按 API key 关联的默认模型自动上报）与 doc_report()（手动指定项目与模型）两种上报方式，支持 accuracy/precision/recall/f1_score/roc_auc/val_loss 指标，并能从 pandas DataFrame 本地生成数据质量摘要后上传。需先在 Web 控制台创建工作区、项目、模型与 API key 才能使用，仪表盘用于查看模型健康、评估历史与问题建议。

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

- auto_report() 按 API key 默认模型自动关联上报，无需传项目/模型名
- 本地先校验指标与输入，非法数据在发请求前被拦截
- 支持 6 种模型评估指标（accuracy/precision/recall/f1_score/roc_auc/val_loss）
- 可从 pandas DataFrame 本地生成数据质量摘要并上传

## 适用场景

- 训练评估后把指标上报到 MLSentinel 查看模型健康与历史
- 用同一 API key 向不同项目/模型手动上报指标
- 上传训练数据的质量摘要以检查模型数据质量

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L15: MLSentinel is a Python SDK for sending machine learning model evaluation metrics and data-quality reports to the ML
> L24: - monitor model health through the MLSentinel Dashboard

## 星数曲线

```mermaid
xychart-beta
    title "Narasimha440/mlsentinel 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `ee3493e00983` · [字段定义](../../DATASET.md)*
