# kraina-ai/srai

⭐ 392 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/kraina-ai/srai) · [官网](https://kraina-ai.github.io/srai/) · 组织维护

**地理空间机器学习库：下载空间数据并生成区域嵌入向量**

面向地理空间机器学习的 Python 库，处理矢量几何数据：提供 OSM/OvertureMaps 数据下载、路网与 POI 提取、GTFS 特征提取、多种区域划分算法（Uber H3、Google S2、Voronoi、行政边界），以及 hex2vec、GTFS2Vec、Highway2Vec 等嵌入方法将区域映射到向量空间，部分嵌入器提供预训练模型，采用类似 scikit-learn 的 API。通过 pip 安装，可按需装可选依赖（osm/gtfs/torch 等）。README 声明库处于重度开发期，小版本间可能出现破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- H3/S2/Voronoi/行政边界等多种区域划分算法
- Hex2Vec/GTFS2Vec/Highway2Vec 等区域嵌入方法，含预训练模型
- OSM/OvertureMaps 数据下载与 GTFS 特征提取
- Loader→Regionalizer→Joiner→Embedder 统一 API，附数据集与基准模块

## 适用场景

- 为下游任务生成地理微区域的嵌入向量
- 下载并处理指定区域的 OpenStreetMap 路网/建筑/POI 数据
- 基于 GTFS 数据提取公交站点特征做区域比较

## 场景标签

 · 领域:地理空间机器学习

## 证据(README 行号)

> L19: Project **Spatial Representations for Artificial Intelligence** (`srai`) is a Python library for geospatial machine
> L29: * **Embedding** - embedding regions into a vector space based on different spatial features, and using different al

## 星数曲线

```mermaid
xychart-beta
    title "kraina-ai/srai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 391 --> 393
    line [392, 392]
```

2026-10-18 392 → 2026-10-23 392（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `594a2692273c` · [字段定义](../../DATASET.md)*
