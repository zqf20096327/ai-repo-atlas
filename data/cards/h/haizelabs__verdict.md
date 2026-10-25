# haizelabs/verdict

⭐ 349 · Jupyter Notebook · MIT · 推送 2025-11-05 · [GitHub](https://github.com/haizelabs/verdict) · [官网](http://verdict.haizelabs.com/docs) · 组织维护

**构建与执行复合 LLM-as-a-judge 评测的声明式框架**

Python 库，用 Unit/Layer/Block 原语以依赖图方式组合多个 LLM 判定单元（推理、验证、辩论、聚合），执行层面提供客户端限流与可并发协调数千次 LLM 调用的并发模型，跨模型、提示词、提取方法与判定协议可替换。面向构建 LLM 应用的开发者与研究人员，用于自动化评测、生产 guardrails、测试时计算排序与强化学习奖励信号。集成 DSPy 作为优化指标。称在多个基准上达到 SOTA 或接近 SOTA 水平。

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

- Unit/Layer/Block 依赖图原语，组合辩论、分层验证等判定结构
- 并发框架可同时协调数千次 LLM 调用，客户端限流保护实验结果
- 跨模型/提示词/提取方法/判定协议即插即用
- 集成 DSPy 作为 AI 系统优化中的指标

## 适用场景

- 为 LLM 应用做自动化评测，替代人工反馈
- 在生产环境 AI 应用之上作为运行时 guardrails
- 测试时计算扩展中对候选输出排序与筛选
- 在奖励不可验证的强化学习场景提供奖励信号

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L9: Verdict is a declarative framework for specifying and executing compound LLM-as-a-judge systems. It is
> L54: ## Verdict Scales Up Judge-Time Compute
> L99: > 1. **Automated Evaluation of AI Applications**. Verdict judges enable *tailored* and *automated* evaluation of AI

## 星数曲线

```mermaid
xychart-beta
    title "haizelabs/verdict 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 348 --> 350
    line [349, 349]
```

2026-10-18 349 → 2026-10-25 349（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0d7d0248b2dd` · [字段定义](../../DATASET.md)*
