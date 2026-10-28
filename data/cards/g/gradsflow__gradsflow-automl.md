# gradsflow/gradsflow-automl

⭐ 306 · Python · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/gradsflow/gradsflow-automl) · [官网](https://docs.gradsflow.com/) · 组织维护

**基于 PyTorch 的开源 AutoML 与模型训练库**

GradsFlow 是基于 PyTorch 的开源 AutoML 库，面向初学者与专家两类用户：AutoTasks 提供零代码的自动建模与训练（图像识别、情感分析、文本摘要等任务），Model 与 Tuner 提供自定义模型训练与超参数优化 API，可在笔记本或远程集群上构建并训练深度学习模型。支持 PyTorch Lightning Flash，2021-8 迁移到 Ray Tune。README 明确声明在 0.1.0 之前会有大量破坏性变更。通过 pip/conda 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- AutoTasks 零代码自动建模与训练（图像识别/情感分析/文本摘要）
- model.fit 可训练任意 PyTorch 模型的训练 API
- Tuner 简化超参数搜索
- 支持 PyTorch Lightning Flash 并基于 Ray Tune

## 适用场景

- 零代码完成图像识别、情感分析等任务的自动建模训练
- 用统一 API 训练自定义 PyTorch 模型并做超参数优化
- 从笔记本直接向远程集群提交训练任务

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L32: GradsFlow is an open-source AutoML Library based on PyTorch.
> L43:  Gradsflow is built for both *beginners* and *experts*! `AutoTasks` provides zero-code AutoML while
> L96: - `gradsflow.tuner`: AutoModel HyperParameter search with minimal code changes.

## 星数曲线

```mermaid
xychart-beta
    title "gradsflow/gradsflow-automl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 305 --> 307
    line [306, 306]
```

2026-10-18 306 → 2026-10-28 306（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `34ca2dfb1aa8` · [字段定义](../../DATASET.md)*
