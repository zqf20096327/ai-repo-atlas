# christopherkarani/MetalANNS

⭐ 18 · Swift · MIT · 推送 2026-08-25 · [GitHub](https://github.com/christopherkarani/MetalANNS) · 个人维护 · 中文 README

**Apple Silicon 上的 Swift 向量检索库，GPU/Metal 加速**

面向 Apple Silicon 的 Swift 6 向量检索库，基于 Metal GPU 与 NEON 实现。默认检索路径为精确扫描（recall@10 = 1.000），可选 `.fast` 模式（IVF-flat）以换取更低延迟与约 0.95–0.99 的召回。构建阶段使用 CAGRA 式固定度图索引以支持全量可变、编辑与大规模回退；元数据过滤基于 SQLite (GRDB) 的 DSL；支持完整加载、零拷贝 mmap 与磁盘只读三种持久化方式。类型状态 API 在编译期阻止对未构建索引的搜索。通过 Swift Package Manager 安装，支持 macOS 14+/iOS 17+/visionOS 1+。README 提供与 FAISS、hnswlib、USearch、sqlite-vec 的同机基准对比。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认精确检索路径（recall@10 = 1.000），Metal GPU + CPU NEON 融合扫描
- CAGRA 式图索引用于构建、编辑与大规模回退，GPU 并行构建
- 元数据过滤 DSL（SQLite/GRDB）与三种持久化模式（全量/mmap/磁盘只读）
- Swift 6 类型状态 API：Unbuilt→Ready→ReadOnly 编译期约束

## 适用场景

- 在 iOS/macOS 应用中做本地设备端向量检索
- 为 RAG 流水线在 Apple 设备上提供嵌入式向量索引
- 需要可变索引（流式插入、编辑）与元数据过滤的检索场景

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L11: **MetalANNS** is a Swift vector search library for Apple Silicon. Search runs on-device. Default search is **exact*
> L65: Default search is a fused exact scan (CPU NEON / int8 prefilter / one GPU dispatch), not a per-hop graph walk. A CA
> L20: - **Filters.** Metadata DSL on top of SQLite (GRDB).

## 星数曲线

```mermaid
xychart-beta
    title "christopherkarani/MetalANNS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6365fde9e5ef` · [字段定义](../../DATASET.md)*
