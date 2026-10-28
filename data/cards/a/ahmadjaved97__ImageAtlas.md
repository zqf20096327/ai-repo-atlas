# ahmadjaved97/ImageAtlas

⭐ 20 · Python · MIT · 推送 2026-03-23 · [GitHub](https://github.com/ahmadjaved97/ImageAtlas) · [官网](https://ahmadjaved97.github.io/ImageAtlas/) · 个人维护

**图像数据集整理工具包：聚类、去重与可视化**

面向图像数据集管理的 Python 工具包，提供基于深度特征提取的图像聚类、重复/近重复图像检测（感知哈希、DINOv2 嵌入、CLIP 语义相似度）与可视化组织功能。支持 DINOv2/ViT/ResNet/CLIP 等 9 类特征模型，聚类算法含 K-Means、HDBSCAN、GMM，降维方法含 PCA、UMAP。通过 pip 安装，CLIP 需从 GitHub 单独安装。README 声明处于活跃开发中，t-SNE 尚在开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 9 类特征提取模型（DINOv2/ViT/ResNet/CLIP/ConvNeXt 等）
- 三种重复检测方法：phash / embedding / clip
- K-Means、HDBSCAN、GMM 聚类与 PCA、UMAP 降维
- 重复项自动保留策略（分辨率/文件大小优先）

## 适用场景

- 训练前对图像数据集做聚类整理与可视化
- 检测并清理数据集中的重复或近重复图像
- 图像数据集的探索性分析与质量控制

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L6: ImageAtlas is a comprehensive toolkit designed to organize, clean, and analyze image datasets.
> L104: |`embedding`|Deep learning embeddings (DINOv2, etc.)|Semantic similarity|

## 星数曲线

```mermaid
xychart-beta
    title "ahmadjaved97/ImageAtlas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6a6f82bc40a4` · [字段定义](../../DATASET.md)*
