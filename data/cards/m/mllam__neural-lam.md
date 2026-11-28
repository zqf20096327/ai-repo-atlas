# mllam/neural-lam

⭐ 312 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/mllam/neural-lam) · [官网](https://kutt.to/mllam) · 组织维护

**面向研究者的有限区域图神经网络天气预测模型库**

基于 PyTorch、PyTorch Lightning 与 PyG 构建的图神经网络天气预测模型仓库，面向有限区域建模（LAM）。提供模块化、可替换的数据、图与模型组件，实现 Graph-LAM、Hi-LAM、Hi-LAM-Parallel 三种架构，支持确定性与概率性（集合采样）预测。研究者可在自有数据上训练、评估或通过子类扩展新的 StepPredictor 与 Forecaster。文档站提供安装、快速上手、DANRA 教程与 API 参考；另附两篇可复现论文的引用信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种图架构：Graph-LAM（平坦）、Hi-LAM（分层）、Hi-LAM-Parallel
- 确定性/概率性预测器与自回归 unroll 机制可自由组合扩展
- 模型、图、数据三层解耦，组件可独立替换
- 提供确定性与概率性论文的可复现分支

## 适用场景

- 在自己区域的气象数据上训练 GNN 天气预测模型
- 评估与对比确定性及概率性集合预报方法
- 子类化 Forecaster/StepPredictor 实现新模型架构

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Neural-LAM is a repository of graph-based neural weather prediction models for Limited Area Modeling (LAM).
> L8: It is aimed at researchers and engineers working on ML-based numerical weather prediction who want to train, evaluat

## 星数曲线

```mermaid
xychart-beta
    title "mllam/neural-lam 星数(近 11 点)"
    x-axis ["2026-10-26", "2026-10-29", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-15", "2026-11-16", "2026-11-20", "2026-11-22", "2026-11-28"]
    y-axis "stars" 302 --> 313
    line [303, 304, 305, 306, 303, 309, 310, 309, 310, 312, 312]
```

2026-10-26 303 → 2026-11-28 312（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `0ba4ec0619bd` · [字段定义](../../DATASET.md)*
