# himanshu-jadhav108/fairlens-ai-

⭐ 15 · TypeScript · 推送 2026-09-23 · [GitHub](https://github.com/himanshu-jadhav108/fairlens-ai-) · [官网](https://fairlens-ai-nine.vercel.app) · 个人维护

**面向开发者的 ML 公平性审计、解释与偏见缓解平台**

Web 端到端平台：上传 CSV 或选择内置数据集（Adult Census、COMPAS），自动训练基线模型并计算 Demographic Parity、Equalized Odds、Disparate Impact 等公平性指标；用 SHAP 解释偏见来源的特征贡献；调用 Gemini 2.5 Flash 生成自然语言摘要与建议；以 CorrelationRemover、ExponentiatedGradient、ThresholdOptimizer 三种策略自动做偏见缓解并对比前后指标。后端 FastAPI + Fairlearn/SHAP，前端 React/TypeScript，含 Firebase 认证与会话存储，支持 PDF/CSV 报告导出，提供 Vercel/Render 在线部署，自述为 72 小时黑客松作品（第三名）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 计算 Demographic Parity / Equalized Odds / Disparate Impact 等公平性指标
- SHAP 特征贡献解释偏见来源，Gemini 2.5 Flash 生成自然语言摘要
- 预处理/过程中/后处理三种策略自动缓解偏见并前后对比
- 内置 Adult Census、COMPAS 演示数据集，支持 PDF/CSV 报告导出

## 适用场景

- 模型上线前审计不同人群间的歧视性结果
- 理解哪些特征驱动了模型偏见并选择缓解策略
- 生成合规审计报告（提及对齐 EU AI Act 等法规）
- 教学场景中演示 AI 公平性概念

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L33: 1. **Audit** models for discriminatory behavior across demographic groups.
> L65: 3. **Auditing:** The Fairness Engine calculates disparity metrics across sensitive groups.
> L161: 3. **Run Audit:** Click "Run Fairness Audit". The backend will process the data and return the fairness metrics.

## 星数曲线

```mermaid
xychart-beta
    title "himanshu-jadhav108/fairlens-ai- 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e8a13e7f6830` · [字段定义](../../DATASET.md)*
