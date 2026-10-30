# yubainu/sibainu-engine

⭐ 15 · Python · NOASSERTION · 推送 2026-06-03 · [GitHub](https://github.com/yubainu/sibainu-engine) · 个人维护

**通过隐状态几何分析在采样前检测 LLM 幻觉的审计引擎**

面向 LLM 推理过程的幻觉审计层：监测 Transformer 各层隐状态的几何失谐（Layer Dissonance），在 token 生成前输出风险评分与 HIGH_RISK/SAFE 判定，无需二次 LLM 调用与训练，在 Gemma、Llama-3.2-1B、Mistral-7B 等模型上以 HaluEval-QA 数据集报告 ROC-AUC 与召回率。核计算为 NumPy 向量化实现（<1ms），另含实时干预 demo 与远程引擎代理架构。需 4GB 显存 GPU，核心分析由 Hugging Face 托管的引擎执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 token 采样前检测潜在轨迹坍缩，核心计算 <1ms
- 无需二次 LLM 调用与训练，冻结权重即用
- 在 Gemma/Llama/Mistral 多模型上报告 ROC-AUC 0.90-0.95（HaluEval-QA）
- 提供实时监控与转向向量干预、自动恢复两种闭环校正路径

## 适用场景

- LLM 生成管道中实时过滤高风险输出
- 在消费级 GPU 上对本地模型做幻觉风险监控
- 研究与评测 LLM 内部状态与幻觉的关联

## 场景标签

`模型评测` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L14: Sibainu is an ultra-lightweight auditor that detects hallucinations *before* they are sampled by monitoring "Layer 
> L29: This project demonstrates a lightweight auditing layer that monitors internal **Hidden State Dynamics** to detect h
> L134: ## 3. Benchmarks (Actual Measurements)

## 星数曲线

```mermaid
xychart-beta
    title "yubainu/sibainu-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `ae25bdae8d70` · [字段定义](../../DATASET.md)*
