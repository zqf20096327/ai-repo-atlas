# aman179102/trust-aware

⭐ 15 · Python · 推送 2026-02-02 · [GitHub](https://github.com/aman179102/trust-aware) · 个人维护

**信任感知情感分析 API：判断何时应转人工审核**

本地 FastAPI 服务，包装 Hugging Face 预训练 DistilBERT 情感分类模型（无需训练，CPU 运行，无云依赖）。在模型之上叠加风险引擎：综合置信度阈值（默认 0.7）、top-1/top-2 概率差、语言歧义模式等信号计算 risk_score，≥2 时输出 needs_human_review，否则 accepted；每次请求返回结构化风险信号与规则生成的可读解释。定位为信任感知、人在回路的参考实现，明确声明不含再训练、校准与生产级可观测性。通过 POST /analyze 与 GET /health 端点提供服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多信号风险引擎（置信度、margin、语言歧义）聚合为 risk_score
- risk_score ≥ 2 时决策为 needs_human_review，转人工审核
- 每请求返回结构化风险信号与规则生成的可读解释
- CPU 本地运行 DistilBERT，无付费 API 与云依赖

## 适用场景

- 在不发送数据到云端的前提下做风险敏感的情感分析
- 作为信任感知 AI 与人在回路决策的参考实现
- 在审核队列/升级工作流中集成低置信预测的人工复核触发

## 场景标签

 · 领域:AI 安全/NLP

## 证据(README 行号)

> L8: > A local FastAPI service that wraps a Hugging Face sentiment model with a risk-aware decision layer.
> L29: - Makes a **human-in-the-loop decision**: either `accepted` or `needs_human_review`.

## 星数曲线

```mermaid
xychart-beta
    title "aman179102/trust-aware 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `30a3076b50cf` · [字段定义](../../DATASET.md)*
