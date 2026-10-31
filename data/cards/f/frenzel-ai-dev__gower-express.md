# frenzel-ai-dev/gower-express

⭐ 15 · Python · MIT · 推送 2026-04-11 · [GitHub](https://github.com/frenzel-ai-dev/gower-express) · 个人维护

**混合数值与分类数据的 Gower 距离 Python 库**

提供混合数值与分类数据的成对 Gower 距离计算工具，附带 Top-N 相似性搜索辅助函数。可选 sklearn 兼容接口；可选加速路径使用 numba、向量化代码，并在可用时支持 GPU。以 pip 包 gower_exp 发布在 PyPI，可选 extras 包括 [gpu]、[sklearn] 及其组合。仓库含 pytest 测试套件、性能基准脚本、文档与示例 notebooks，面向使用聚类与客户分群等无监督学习流程的开发者。

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

- 混合类型数据集的成对 Gower 距离计算
- Top-N 相似性搜索辅助函数
- 可选 sklearn 兼容接口
- 可选加速路径：numba、向量化代码与 GPU 支持

## 适用场景

- 聚类或客户分群前计算混合类型数据的距离矩阵
- 在混合数值与分类数据集中做相似性搜索
- 在 sklearn 流程中使用 Gower 距离

## 场景标签

 · 领域:数据科学/机器学习工具库

## 证据(README 行号)

> L10: Gower Express provides Gower distance utilities for mixed numerical and categorical data, with optional sklearn int
> L37: - Pairwise Gower distance for mixed-type datasets

## 星数曲线

```mermaid
xychart-beta
    title "frenzel-ai-dev/gower-express 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8ac03993234a` · [字段定义](../../DATASET.md)*
