# iaavas/simile-search

⭐ 35 · TypeScript · MIT · 推送 2025-12-28 · [GitHub](https://github.com/iaavas/simile-search) · [官网](https://www.npmjs.com/package/simile-search) · 个人维护

**本地离线混合搜索引擎库：语义向量+模糊+关键词**

基于 TypeScript/npm 的搜索库，结合 AI 嵌入（Transformers.js，Xenova/all-MiniLM-L6-v2 模型）、模糊匹配与关键词搜索，本地运行无需 API 调用。支持 HNSW 近似最近邻索引（O(log n)）、float16/int8 量化、LRU 嵌入缓存、嵌套对象路径搜索与持久化快照。面向需要在商品目录、内容库、用户目录中做容错检索的应用开发者，以库形式集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义/模糊/关键词三种策略混合打分，可配置权重
- Transformers.js 全本地嵌入，无 API 调用
- HNSW 近似最近邻索引与 float16/int8 量化降内存
- 快照持久化避免重复嵌入，异步非阻塞索引更新

## 适用场景

- 给商品目录或内容库加容错的智能搜索
- 嵌套结构数据（如书籍元数据）的混合检索
- 离线/无外部依赖场景下的语义搜索

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L13: Simile is a high-performance search engine that combines semantic understanding, fuzzy matching, and keyword search
> L226: **Embedding Model:** Xenova/all-MiniLM-L6-v2 via Transformers.js

## 星数曲线

```mermaid
xychart-beta
    title "iaavas/simile-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `23fe345bb2c1` · [字段定义](../../DATASET.md)*
