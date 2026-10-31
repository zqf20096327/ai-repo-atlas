# mingyu-hkustgz/RESQ

⭐ 15 · C++ · 推送 2026-02-03 · [GitHub](https://github.com/mingyu-hkustgz/RESQ) · 个人维护

**面向高压缩比向量量化的近似最近邻搜索方法（MRQ）官方实现**

VLDB 2026 论文 Quantization Meets Projection 的官方 C++/Python 实现：MRQ/MRQ+ 利用数据分布做 PCA 投影与 RaBitQ 量化的距离修正，实现高压缩比的向量编码与近似 k 近邻搜索，并对比 RabitQ 与 HNSW 基线。依赖 C++17、Python 与 OpenMP，需从源码编译运行；用户通过 shell 脚本指定数据集（ANN-Benchmark 的 fvecs/ivecs 格式）与索引、搜索参数进行实验复现。目录中含 HNSW、IVF、FastScan 辅助函数与 Python 数据预处理脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PCA 投影与 RaBitQ 量化结合的高压缩比向量编码（MRQ/MRQ+）
- 提供 RabitQ、HNSW 基线的索引与搜索测试脚本
- 支持 ANN-Benchmark 数据集（含 OpenAI embedding 维度）的复现流程

## 适用场景

- 复现论文中高压缩比量化搜索的实验结果
- 在新向量数据集上运行 MRQ/MRQ+ 索引与近似搜索
- 比较量化方法与图索引（HNSW）的精度-效率表现

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L5: This is the official implementation of the early paper Fast High-dimensional Approximate Nearest Neighbor Search wit
> L7: MRQ leverages data distribution to achieve better distance correction and a higher vector compression ratio. It sign

## 星数曲线

```mermaid
xychart-beta
    title "mingyu-hkustgz/RESQ 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b90f2672011a` · [字段定义](../../DATASET.md)*
