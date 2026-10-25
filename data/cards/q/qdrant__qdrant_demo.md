# qdrant/qdrant_demo

⭐ 193 · TypeScript · 推送 2026-09-04 · [GitHub](https://github.com/qdrant/qdrant_demo) · 组织维护

**Qdrant 混合检索演示：对创业公司数据做语义/关键词/混合搜索**

Qdrant 官方演示项目，对创业公司目录（startups_demo.json）构建向量检索：用 mxbai-embed-large-v1 做语义检索、bm25 稀疏向量做关键词检索、RRF 融合的混合检索，三种模式可在同一数据上切换对比。提供 FastAPI 后端与 React 前端，本地通过 Docker 运行 Qdrant 容器，本地嵌入用 fastembed，也可指向 Qdrant Cloud 由服务端嵌入。支持换用更大的 Crunchbase 数据集（托管版约 300 万条）。需 Python 3.11 与 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一数据上对比 semantic / keyword / hybrid 三种检索模式
- dense 向量 + bm25 稀疏向量，RRF 融合
- 本地 Docker 运行，无需云账户；也可指向 Qdrant Cloud 服务端嵌入
- 可换用 Crunchbase 更大数据集构建检索库

## 适用场景

- 想快速体验/学习 Qdrant 混合检索的开发者搭建本地演示
- 对比语义、关键词、混合三种检索模式的效果差异
- 以 Qdrant 为基础构建自己的语义搜索原型

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L17: Qdrant does the retrieval end to end: a named `dense` vector for semantic, a
> L117: |Qdrant|Vector search engine handling dense and sparse retrieval, and the fusion between them.|

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/qdrant_demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 192 --> 194
    line [193, 193]
```

2026-10-18 193 → 2026-10-25 193（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `64610b73a475` · [字段定义](../../DATASET.md)*
