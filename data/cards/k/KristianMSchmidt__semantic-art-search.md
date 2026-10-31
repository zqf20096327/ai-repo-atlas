# KristianMSchmidt/semantic-art-search

⭐ 23 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/KristianMSchmidt/semantic-art-search) · [官网](https://semantic-art-search.com/) · 个人维护

**面向公众的语义艺术品搜索引擎，支持自然语言与图像语义检索**

一个开源的艺术品语义搜索引擎：收录 SMK、克利夫兰艺术博物馆、荷兰国立博物馆、大都会博物馆、芝加哥艺术博物馆共 5 家开放数据机构的公有领域藏品，用户用自然语言（主题、情绪、风格）搜索，或粘贴藏品编号查找视觉/主题相似作品。机制：用 Jina CLIP v2 多模态模型将图像与查询嵌入同一向量空间，做最近邻检索排序；提供 Visual、By title、Auto 三种匹配模式和按作品类型、博物馆的元数据过滤。限制：仅含公有领域且有照片的视觉艺术（绘画、版画、素描），覆盖范围持续扩充。README 未给出安装运行说明，以在线服务形式使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Jina CLIP v2 多模态嵌入，图像与查询同空间最近邻检索
- 聚合 5 家博物馆开放数据的公有领域藏品
- 支持自然语言查询、藏品编号查相似、多语言查询（Jina 支持）
- Visual / By title / Auto 三种匹配模式及类型与博物馆过滤

## 适用场景

- 用『海战』『印象派』这类自然语言描述找画
- 通过藏品编号或『Find similar』发现视觉相似作品
- 跨多家博物馆按主题/情绪/风格浏览公有领域艺术

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: Semantic Art Search is an open-source search engine that uses advanced machine learning to explore digitized art col
> L54: The system uses *Jina CLIP v2* (a multimodal neural network) to embed both images and search queries into a shared 

## 星数曲线

```mermaid
xychart-beta
    title "KristianMSchmidt/semantic-art-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b56760b47d3a` · [字段定义](../../DATASET.md)*
