# virelay/corelay

⭐ 32 · Python · LGPL-3.0 · 推送 2026-04-30 · [GitHub](https://github.com/virelay/corelay) · 组织维护

**单机 XAI 分析流水线组合库，产出可视化用结果**

Python 库，用于组合单机数据处理与分析流水线，主要面向可解释人工智能（XAI）场景。核心机制为 Pipeline—Task—Processor 三层结构，内置聚类、嵌入、降维等处理器，支持并行/串行执行与中间结果 memoization；结果以 HDF5 文件存储，可配合可视化工具 ViRelAy 使用，并提供 SpRAy 全流程示例脚本。安装需 C++ 编译器（依赖 metrohash-python），HDBSCAN/UMAP 为可选安装项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pipeline—Task—Processor 模块化组合结构
- 内置聚类/嵌入/降维处理器库
- 中间结果 memoization 复用机制
- 生成 HDF5 结果供 ViRelAy 可视化

## 适用场景

- 组合单机 XAI 数据分析流水线
- 对模型分析结果做聚类、降维并输出 HDF5 供 ViRelAy 可视化
- 复用中间计算结果加速重复分析

## 场景标签

 · 领域:机器学习/可解释性分析

## 证据(README 行号)

> L11: **CoRelAy** is a library designed for composing efficient, single-machine data analysis pipelines. It enables the r
> L30: - **Pipeline Composition**: CoRelAy allows you to compose pipelines of processors, which can be executed in paralle

## 星数曲线

```mermaid
xychart-beta
    title "virelay/corelay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-25 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f9c6e9583a16` · [字段定义](../../DATASET.md)*
