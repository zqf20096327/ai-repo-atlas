# cvxgrp/pymde

⭐ 595 · Python · Apache-2.0 · 推送 2026-02-26 · [GitHub](https://github.com/cvxgrp/pymde) · [官网](https://pymde.org) · 组织维护

**Python 库：为有限项集合计算最小失真向量嵌入**

PyMDE 是斯坦福 cvxgrp 团队开发的 Python 嵌入库，基于最小失真嵌入（MDE）通用框架，可复现 t-SNE/UMAP 等经典嵌入并支持自定义目标函数与约束（如标准化去相关）。提供 preserve_neighbors 与 preserve_distances 两个开箱函数，用于数据可视化、生成监督学习特征向量、高维数据压缩与图绘制。CPU 与 GPU（PyTorch）均可运行，Rust 实现的 kNN 与最短路径预处理加速。配套专著 arXiv 2021 论文，README 自称仍处于早期活跃开发阶段。

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

- 最小失真嵌入通用框架，支持自定义目标函数与约束
- preserve_neighbors / preserve_distances 开箱函数
- Rust 实现的近似/精确 kNN 与 BFS 最短路径预处理
- 支持 CPU 与 GPU（PyTorch）运行

## 适用场景

- 把高维数据集降维后做可视化
- 为监督学习生成特征向量
- 压缩高维向量数据
- 绘制大规模图并保留局部或全局结构

## 场景标签

 · 领域:机器学习/降维嵌入

## 证据(README 行号)

> L8: PyMDE is a Python library for computing vector embeddings for finite sets of
> L12: **A general framework.** What sets PyMDE apart from other embedding libraries is that it provides a
> L33: * generate feature vectors for supervised learning;

## 星数曲线

```mermaid
xychart-beta
    title "cvxgrp/pymde 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 594 --> 596
    line [595, 595]
```

2026-10-18 595 → 2026-10-27 595（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `14cd8050a015` · [字段定义](../../DATASET.md)*
