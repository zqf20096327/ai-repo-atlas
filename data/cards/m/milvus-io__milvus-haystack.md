# milvus-io/milvus-haystack

⭐ 24 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/milvus-io/milvus-haystack) · 组织维护

**为 Haystack 提供 Milvus 向量数据库文档存储集成**

Milvus 官方维护的 Haystack Document Store 集成包：以 MilvusDocumentStore 组件接入 Haystack 流水线，支持 Milvus Lite 本地文件、Milvus Server（Docker/K8s）与 Zilliz Cloud 三种连接方式。提供稠密检索、稀疏检索（Haystack sparse embedder 或 Milvus 内置 BM25 函数）与混合检索示例，内置 BM25 可在服务端生成稀疏向量以简化流水线。以 pip 包分发，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MilvusDocumentStore 可直接嵌入 Haystack 流水线
- 支持 Milvus Lite / Milvus Server / Zilliz Cloud 三种连接方式
- 支持 Milvus 内置 BM25 函数在服务端生成稀疏向量
- 提供稠密、稀疏、混合检索与 RAG 流水线示例

## 适用场景

- 在 Haystack RAG 流水线中使用 Milvus 作向量存储
- 大规模数据场景下连接 Milvus Server 或 Zilliz Cloud
- 用内置 BM25 简化混合检索流水线构建

## 场景标签

`RAG` `向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L1: # Milvus Document Store for Haystack
> L25: Use the `MilvusDocumentStore` in a Haystack pipeline as a quick start.

## 星数曲线

```mermaid
xychart-beta
    title "milvus-io/milvus-haystack 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7c99ff942938` · [字段定义](../../DATASET.md)*
