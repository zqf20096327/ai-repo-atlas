# triton-inference-server/model_analyzer

⭐ 530 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/triton-inference-server/model_analyzer) · 组织维护

**CLI 工具：为 Triton 推理服务模型搜索最优配置并生成报告**

NVIDIA Triton 生态的命令行工具，面向在 Triton Inference Server 上部署模型的用户：通过 Quick Search、Brute Search、Optuna Search（Alpha）四种搜索模式，在指定硬件上为单模型、多模型、Ensemble、BLS 及 LLM 模型寻找更优的 Max Batch Size、Dynamic Batching、Instance Group 等配置；生成汇总与详细报告展示各配置的计算/内存权衡，支持按延迟预算等 QoS 约束过滤结果。文档覆盖 Kubernetes 部署方式。限制：Optuna 搜索处于 Alpha 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 4 种配置搜索模式（启发式/穷举/Optuna 超参优化）
- 支持单模型、多并发模型、Ensemble、BLS、LLM 的 profiling
- 生成汇总与详细报告，展示配置间计算/内存权衡
- QoS 约束过滤（如延迟预算阈值）

## 适用场景

- 部署前为 Triton 模型寻找给定硬件上的最优配置
- 比较多模型并发在同一 GPU 上的配置方案
- 按延迟预算筛选满足 QoS 要求的模型配置

## 场景标签

 · 领域:推理服务/性能分析

## 证据(README 行号)

> L5: Triton Model Analyzer is a CLI tool which can help you find a more optimal configuration, on a given piece of hardwa
> L36: - LLM: Model Analyzer can help you

## 星数曲线

```mermaid
xychart-beta
    title "triton-inference-server/model_analyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 529 --> 531
    line [530, 530]
```

2026-10-18 530 → 2026-10-29 530（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a1509f0a26a3` · [字段定义](../../DATASET.md)*
