# huggingface/faceberg

⭐ 32 · Python · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/huggingface/faceberg) · [官网](https://faceberg.kszucs.dev/) · 组织维护

**将 HuggingFace 数据集映射为 Apache Iceberg 表的元数据桥接工具**

在 HuggingFace 数据集与 Apache Iceberg 表格式之间建立元数据映射，不复制数据：目录元数据存储在 HuggingFace Spaces 或 Buckets 上并自动部署 REST catalog 服务，DuckDB、PyIceberg、Spark 等 Iceberg 兼容引擎即可查询。提供 CLI（init/add/sync/serve/quack 等命令）与 Python API，支持本地文件系统目录用于开发与 CI，catalog Space 自带 Web UI 可在浏览器中运行 SQL。自述为早期 alpha 阶段软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 元数据映射而非数据复制，Iceberg 兼容引擎可直接查询
- 目录元数据托管于 HF Spaces/Buckets 并自动部署 REST catalog
- 本地文件系统目录模式，无需 token，适用于开发/测试/CI
- catalog Space 自带 Web UI，浏览器内通过 DuckDB-WASM 运行 SQL

## 适用场景

- 用 DuckDB/Spark 等 SQL 引擎直接查询 HuggingFace 数据集
- 将 HF 数据集纳入 Iceberg 表目录统一管理并跟踪版本修订
- 通过 REST catalog 与团队共享数据集目录

## 场景标签

 · 领域:数据工程/数据目录

## 证据(README 行号)

> L5: **Bridge HuggingFace datasets with Apache Iceberg tables — no data copying, just metadata.**
> L7: Faceberg maps HuggingFace datasets to Apache Iceberg tables. Your catalog metadata lives on HuggingFace Spaces (or B
> L124: **No data is copied** — only metadata is created. Query with DuckDB, PyIceberg, Spark, or any Iceberg-compatible t

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/faceberg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1042baf29ad9` · [字段定义](../../DATASET.md)*
