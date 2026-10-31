# raphaelsulzer/dsr-benchmark

⭐ 44 · Python · MIT · 推送 2025-12-02 · [GitHub](https://github.com/raphaelsulzer/dsr-benchmark) · [官网](https://arxiv.org/abs/2301.13656) · 个人维护

**点云表面重建方法的基准评测数据集与代码（TPAMI 论文）**

TPAMI 论文 A Survey and Benchmark for Automatic Surface Reconstruction from Point Clouds 的配套仓库，提供 Berger et al.、ModelNet10、ShapeNet v1 三个数据集的水密网格与扫描点云下载链接（Zenodo 等），含 ConvONet、Points2Surf、POCO 等方法的训练/评测数据，以及 Python 评测代码（MeshEvaluator 等）。用户克隆仓库后经 install.sh 创建 conda 环境，编译 mesh-tools 到 CPP_DIR，即可对自己的重建算法进行评测。面向表面重建方向的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Berger/ModelNet10/ShapeNet 三个数据集的网格与扫描点云
- 含多种深度学习方法（ConvONet、Points2Surf、POCO 等）的训练与评测数据
- Python 评测代码（MeshEvaluator）可评测自有重建算法

## 适用场景

- 评测自己的点云表面重建算法并与基准对比
- 获取带水密网格真值的扫描点云数据集
- 复现论文中的表面重建方法评测结果

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # A Survey and Benchmark of Automatic Surface Reconstruction from Point Clouds
> L3: Data and evaluation code for the TPAMI paper **A Survey and Benchmark of Automatic Surface Reconstruction from Point

## 星数曲线

```mermaid
xychart-beta
    title "raphaelsulzer/dsr-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `33bc1aa888fe` · [字段定义](../../DATASET.md)*
