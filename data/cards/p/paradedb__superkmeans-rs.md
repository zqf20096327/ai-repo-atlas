# paradedb/superkmeans-rs

⭐ 14 · Rust · MIT · 推送 2026-10-26 · [GitHub](https://github.com/paradedb/superkmeans-rs) · [官网](https://crates.io/crates/superkmeans-rs) · 组织维护

**SuperKMeans 论文的 Rust 移植：高维向量 k-means 聚类**

CWI SuperKMeans 论文的 Rust 实现，用于高维向量嵌入的 k-means 聚类，训练与分配阶段通过 Rayon 并行，并采用 ADSampling 风格的距离剪枝。默认后端为纯 Rust（基于 matrixmultiply），无需系统 BLAS；可选启用 OpenBLAS 或 macOS Accelerate 特性。提供流式接口（train_iter/train_dataset）处理超出内存的数据，HierarchicalSuperKMeans 可按规模上限递归拆分聚类。以 Rust crate 形式发布，需 Rust 1.89+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rayon 并行的训练与分配，支持 RAYON_NUM_THREADS 控制并行度
- ADSampling 风格距离剪枝加速
- train_iter/train_dataset 流式扫描处理超出内存的数据
- HierarchicalSuperKMeans 按大小上限递归拆分聚类

## 适用场景

- 对高维向量嵌入做 k-means 聚类训练与分配
- 在内存受限场景下流式处理大规模向量数据
- macOS/Linux/Windows 上可选接入系统 BLAS 后端

## 场景标签

 · 领域:机器学习/向量聚类

## 证据(README 行号)

> L9: A Rust port of SuperKMeans for k-means clustering of high-dimensional vector
> L10: embeddings. Training and assignment run in parallel using Rayon, with

## 星数曲线

```mermaid
xychart-beta
    title "paradedb/superkmeans-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c0c5567cd009` · [字段定义](../../DATASET.md)*
