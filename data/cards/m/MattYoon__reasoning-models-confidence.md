# MattYoon/reasoning-models-confidence

⭐ 23 · Python · 推送 2025-11-19 · [GitHub](https://github.com/MattYoon/reasoning-models-confidence) · [官网](https://arxiv.org/abs/2505.14489) · 个人维护

**NeurIPS 2025 论文官方代码：分析推理模型表达置信度的能力**

论文《Reasoning Models Better Express Their Confidence》的官方代码仓库：研究推理模型（reasoning models）能否可靠表达自身答案的置信度，通过大规模实验与分析（校准指标 ECE、Brier Score、AUROC，线性回归、消融、上下文慢思考）探究该能力的来源。基于 lm-eval-harness 与 evalchemy 构建评测脚本，对 Qwen3、R1、GLM Z1、EXAONE Deep 等推理与非推理模型进行评测，并提供分割后 CoT 数据集路径。面向复现实验的科研人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供主实验、线性回归、消融、上下文慢思考的完整评测脚本
- 计算 ECE、Brier Score、AUROC 校准指标
- 区分推理模型/非推理模型两套评测流程与预置数据集路径

## 适用场景

- 复现论文中推理模型置信度表达的实验
- 评测自身模型的置信度校准情况
- 基于分割 CoT 数据做校准回归分析

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # [NeurIPS 2025] Reasoning Models Better Express Their Confidence
> L41: 4. Finally, use the notebook `results/calculate_metrics.ipynb` to calculate ECE, Brier Score, and AUROC for the out

## 星数曲线

```mermaid
xychart-beta
    title "MattYoon/reasoning-models-confidence 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3687f1a60356` · [字段定义](../../DATASET.md)*
