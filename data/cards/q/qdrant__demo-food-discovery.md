# qdrant/demo-food-discovery

⭐ 52 · JavaScript · 推送 2026-09-02 · [GitHub](https://github.com/qdrant/demo-food-discovery) · 组织维护

**基于 Qdrant 的菜品图片发现式搜索演示应用**

Qdrant 官方的演示项目：以 Wolt 菜品数据集（200 万+ 图片）为语料，图片用 CLIP（clip-ViT-B-32, Sentence-Transformers）向量化并索引到 Qdrant。用户通过对喜欢/不喜欢图片的正负反馈进行发现式搜索，Qdrant Recommendation API 基于正负例查找相似/不相似菜品，也支持文本查询语义过滤。前端 React+Vite，后端 FastAPI，Docker Compose 一条命令启动，需导入数据快照后使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 正负例反馈的发现式搜索，基于 Qdrant Recommendation API
- Wolt 数据集 200 万+ 菜品图片，CLIP clip-ViT-B-32 向量化
- Docker Compose 一条命令启动，支持 Qdrant Cloud 或本地实例
- 机制与嵌入模型无关，可换用任意多模态嵌入模型

## 适用场景

- 体验基于向量搜索的图片发现式交互范式
- 学习 Qdrant Recommendation API 与快照导入的用法
- 了解 CLIP 图文向量化在菜品检索中的应用

## 场景标签

`推荐系统` `语义搜索` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L10: This is a demo project for the Qdrant vector search engine. It
> L27: the Qdrant design system. Qdrant [Recommendation API](
> L30: and dissimilar to the disliked ones. All the components are enclosed in Docker Compose

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/demo-food-discovery 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-30 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f741ef0a2eac` · [字段定义](../../DATASET.md)*
