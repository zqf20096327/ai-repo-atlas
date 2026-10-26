# Dicklesworthstone/fast_vector_similarity

⭐ 429 · Rust · 推送 2026-09-04 · [GitHub](https://github.com/Dicklesworthstone/fast_vector_similarity) · [官网](https://pypi.org/project/fast-vector-similarity/) · 个人维护

**Rust 向量相似度计算库，提供 Python 绑定与多种相关性度量**

以 Rust 实现的向量相似度计算库，提供 Spearman ρ、Kendall τ、近似距离相关、Jensen-Shannon 依赖度量、Hoeffding's D、归一化互信息等度量，并支持自助法（bootstrapping）估计度量的置信区间。通过 rayon 并行与 ndarray 向量化优化，Kendall τ 用归并排序计数将复杂度降至 O(n log n)。以 Cargo 依赖与 PyPI 两种方式提供，Python 端暴露两个函数并以 JSON 返回结果；README 给出与 LLM 文本 embedding（如 4096 维向量）分析结合的工作流示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种相似度/依赖性度量（含归一化互信息）
- bootstrapped 置信区间估计
- rayon 并行 + ndarray 向量化 + Kendall τ 的 O(n log n) 逆序计数优化
- Python 绑定输出 JSON，支持高维 LLM embedding 分析

## 适用场景

- 我对 LLM 生成的高维文本 embedding 做相似度排序
- 我需要给相似度度量附上自助法置信区间
- 我在 Python 或 Rust 项目中做非参数相关性与依赖性分析

## 场景标签

 · 领域:数值计算/统计分析

## 证据(README 行号)

> L5: The Fast Vector Similarity Library is a high-performance Rust-based tool for efficiently computing similarity measur
> L61: This library is highly compatible with modern language models like Llama2, enabling easy analysis of text embedding

## 星数曲线

```mermaid
xychart-beta
    title "Dicklesworthstone/fast_vector_similarity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 428 --> 430
    line [429, 429]
```

2026-10-18 429 → 2026-10-26 429（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `689c9c3f1b40` · [字段定义](../../DATASET.md)*
