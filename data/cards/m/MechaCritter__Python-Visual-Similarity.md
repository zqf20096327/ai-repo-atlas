# MechaCritter/Python-Visual-Similarity

⭐ 21 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/MechaCritter/Python-Visual-Similarity) · [官网](https://mechacritter.github.io/Python-Visual-Similarity/) · 个人维护

**面向图像检索与聚类的图像相似度计算库（传统+深度方法）**

pyvisim 是一个计算机视觉库，提供从 PSNR、SSIM、Fisher Vectors、VLAD 等传统指标到 CLIP、孪生网络等深度学习方法的图像相似度计算。核心依赖仅为 numpy、scipy，深度学习功能通过可选的 torch 支持。内置基于 hnswlib 的近似最近邻搜索（也可传入 FAISS 索引），并提供 alpha 查询扩展与 k-reciprocal 重排序来精炼检索结果。部分指标使用 Cython 内核与 C++ 库加速 CPU 计算。面向需要图像检索、图像聚类的开发者，以 Python 包形式经 pip 安装。

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

- 聚合 PSNR/SSIM/Fisher Vectors/VLAD 传统指标与 CLIP/孪生网络深度方法
- 核心依赖仅 numpy/scipy，深度学习功能按需安装（pyvisim[nn]）
- 内置 hnsw ANNs 搜索，支持传入 FAISS 索引
- 提供查询扩展与 k-reciprocal 重排序提升检索精度

## 适用场景

- 计算两张图像的相似度分数（如 SSIM）
- 基于 CLIP 嵌入做图像检索与结果重排序
- 为图像聚类任务提取相似度度量

## 场景标签

`向量数据库` `图像视频处理` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L11: `pyvisim` is a computer vision library for computing image similarities using traditional and deep learning methods
> L26: traditional methods like `PSNR`, `SSIM`, `Fisher Vectors`, and `VLAD` to deep
> L27: learning methods like `CLIP` and `Siamese Networks`. Furthermore, advanced

## 星数曲线

```mermaid
xychart-beta
    title "MechaCritter/Python-Visual-Similarity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `09f9a151a513` · [字段定义](../../DATASET.md)*
