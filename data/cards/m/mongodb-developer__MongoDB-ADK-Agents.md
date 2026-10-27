# mongodb-developer/MongoDB-ADK-Agents

⭐ 47 · Python · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/mongodb-developer/MongoDB-ADK-Agents) · 组织维护

**用 Google ADK 和 MongoDB 向量搜索搭建的 AI 购物 agent 示例**

MongoDB 官方开发者组织发布的示例项目：基于 Google ADK 构建食品杂货购物 agent，用 Gemini 嵌入与 MongoDB Atlas Vector Search 做商品语义检索，支持按品类预过滤，并通过 MongoDB 管理购物车与数量。附 27,555 条商品数据集、嵌入生成与向量索引脚本，另有讲师引导的 workshop 目录。限制：需要 Gemini API key 与 Atlas 集群，免费 M0 层需裁剪数据子集；购物车 username 以普通参数传递，生产环境需改从会话读取身份。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MongoDB Vector Search + Gemini 嵌入的商品语义搜索
- 品类预过滤可将搜索限定到单一店铺分区
- 提供嵌入生成与向量索引脚本（可断点重跑）
- 附 27,555 条商品数据集与 workshop 实验材料

## 适用场景

- 学习如何用 ADK + MongoDB 向量搜索构建 agent
- 参考 RAG/语义检索与购物车工具的组合实现
- 作为讲师引导的动手实验教材

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L3: An AI grocery-shopping agent built with Google ADK and MongoDB
> L11: - Semantic product search with MongoDB Vector Search and Gemini embeddings

## 星数曲线

```mermaid
xychart-beta
    title "mongodb-developer/MongoDB-ADK-Agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-27 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7a2012a53590` · [字段定义](../../DATASET.md)*
