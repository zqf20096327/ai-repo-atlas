# sb-ai-lab/RePlay

⭐ 416 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/sb-ai-lab/RePlay) · [官网](https://sb-ai-lab.github.io/RePlay/) · 组织维护

**端到端推荐系统开发与评测框架，覆盖数据处理到模型上线**

面向推荐系统开发者的 Python 框架，覆盖推荐流水线全生命周期：数据预处理与切分、从 SOTA 到基线的多种推荐模型构建、超参数优化（Optuna）、评测指标、模型集成与混合，以及从离线实验到线上生产的模式切换。兼容 CPU/GPU/多 GPU，通过 PySpark 支持分布式计算，并可用 polars 做数据预处理。提供 PyPI 安装与 spark/torch 扩展包，可选支持 OpenVINO 模型编译、向量库检索（hnswlib）与 LightFM（实验性）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖预处理、模型构建、超参优化、评测、集成混合的完整流水线
- PySpark 分布式计算与 polars 快速数据预处理
- 支持 SASRec/BERT4Rec/TwoTower 等基于 transformer 的模型与 bandit 模型
- OpenVINO 模型编译、向量库分层检索等可选功能

## 适用场景

- 在统一框架下对比多种推荐模型的效果
- 大规模场景下用 PySpark 训练推荐模型
- 从离线实验平滑迁移到线上推荐服务

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L11: RePlay is an advanced framework designed to facilitate the development and evaluation of recommendation systems. It
> L15: * **Wide Range of Recommendation Models:** Enables building of recommendation models from State-of-the-Art to commo

## 星数曲线

```mermaid
xychart-beta
    title "sb-ai-lab/RePlay 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 414 --> 417
    line [415, 416, 416]
```

2026-10-18 415 → 2026-10-30 416（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9e7a02c448b0` · [字段定义](../../DATASET.md)*
