# NTU-Siqiang-Group/AsterVec

⭐ 38 · C++ · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/NTU-Siqiang-Group/AsterVec) · [官网](https://lsmvec.com) · 组织维护

**面向端侧 AI 记忆与本地 RAG 的磁盘型向量检索引擎**

以 C++/Python 库形式提供的向量检索引擎，索引驻留磁盘，内存中仅保留少量导航结构与缓存，可在数百 MB 内存内检索数百万向量。架构上为图存储（基于图导向 LSM-tree Aster）与向量存储分离的双存储设计，支持原地插入、更新、删除，无重建步骤，另附可选 HTTP 服务器。面向本地 AI agent 记忆与桌面 RAG 场景，README 给出与 Chroma、LanceDB 的基准对比数据。

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

- 索引驻留磁盘，内存仅保留导航层与缓存，可设内存预算
- 图/向量分离存储：边写入走图导向 LSM-tree，向量打包页存
- 原地插入/更新/删除，无索引重建步骤
- 线程安全 Python 与 C++ 嵌入式库，附带可选 HTTP 服务器

## 适用场景

- 本地 AI agent 的记忆存储与检索
- 桌面端 RAG 在低内存设备上检索大规模向量
- 数据持续增长的向量集合免重建更新

## 场景标签

`向量数据库` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: AsterVec is a vector search engine that keeps its index on disk and puts
> L19: within a few hundred MB of memory. It is built for local AI agents and
> L32: - **Embeddable.** A thread-safe Python and C++ library that runs inside

## 星数曲线

```mermaid
xychart-beta
    title "NTU-Siqiang-Group/AsterVec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3a82382f76ab` · [字段定义](../../DATASET.md)*
