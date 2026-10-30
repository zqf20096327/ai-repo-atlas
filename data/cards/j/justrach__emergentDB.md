# justrach/emergentDB

⭐ 22 · Rust · AGPL-3.0 · 推送 2026-01-23 · [GitHub](https://github.com/justrach/emergentDB) · [官网](https://emergentdb.com) · 个人维护

**自优化向量数据库：MAP-Elites 进化算法自动选索引配置**

以 Rust 编写的向量数据库（含 api-server 与 vector-core 库），核心机制为双 Quality-Diversity 系统：IndexQD 在 Recall×Latency×Memory 三维行为空间中进化索引类型与超参，InsertQD 在六种 SIMD 插入策略间择优；自动在 HNSW/Flat/IVF 间切换，并施加 99% 召回率下限（低于则施加立方适应度惩罚）。支持 RocksDB 持久化（设置 DATA_DIR）与平台 SIMD（ARM NEON/x86）。README 自述为 Proof of Concept，基准基于 768 维 Gemini 嵌入。面向需要语义检索后端的开发者，需从源码编译运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- MAP-Elites 双系统自动进化索引配置（HNSW/Flat/IVF 自适应切换）
- 99% 召回率下限的适应度惩罚机制
- 六种 SIMD 插入策略竞争择优，自述 5.6M vectors/second
- 内置预进化配置网格（来源标注 OpenSearch/Milvus/Pinecone 参数）与 RocksDB 持久化

## 适用场景

- 为语义检索应用提供免调参的向量存储后端
- 在召回率与延迟间按工作负载自动选索引配置
- 小规模数据集上跑嵌入式向量检索（Rust 库形式）

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: > **Proof of Concept** - A self-optimizing vector database that uses MAP-Elites evolutionary algorithm to automatica
> L33: EmergentDB uses a **Dual Quality-Diversity System**:
> L35: 1. **IndexQD** - 3D behavior space (Recall × Latency × Memory) evolves optimal index type and hyperparameters

## 星数曲线

```mermaid
xychart-beta
    title "justrach/emergentDB 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c7f1178a0af0` · [字段定义](../../DATASET.md)*
