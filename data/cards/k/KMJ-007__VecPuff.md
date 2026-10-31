# KMJ-007/VecPuff

⭐ 14 · Rust · MIT · 推送 2026-03-07 · [GitHub](https://github.com/KMJ-007/VecPuff) · [官网](https://blog.karanjanthe.me/posts/vecpuff/) · 个人维护

**基于 S3 的 Rust 向量数据库，供学习可扩展向量检索架构**

VecPuff 是用 Rust 编写的向量数据库，存储层构建在 S3 之上，作者声明其定位为学习与实验可扩展向量检索架构的项目，灵感来自 turbopuffer。采用日志结构化架构：写入先批量写入 S3 的 WAL 文件，后台压缩进程将 WAL 合并为索引段，使用 SPFresh 近似最近邻索引加速查询，并对高频访问文件做本地缓存。通过 config.toml 与环境变量配置 S3 连接、批处理、压缩阈值等；以 HTTP API 提供命名空间管理、向量 upsert、相似度查询与元数据查询，支持 cosine 与 euclidean 距离度量。需从源码用 cargo 编译运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 存储层构建在 S3 之上，WAL + 后台压缩 + 本地缓存的日志结构架构
- SPFresh 近似最近邻索引
- HTTP API 提供命名空间、向量 upsert、查询与元数据接口
- 支持 cosine_distance 与 euclidean_squared 距离度量

## 适用场景

- 学习基于对象存储的向量数据库架构
- 实验可扩展向量检索的设计与实现
- 在本地运行一个轻量向量检索服务做原型验证

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: VecPuff is a vector database built on top of S3, inspired by turbopuffer. It's designed for learning and experimenta
> L11: 1. **WAL (Write-Ahead Log)**: All writes are batched and written to S3 as WAL files

## 星数曲线

```mermaid
xychart-beta
    title "KMJ-007/VecPuff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ba9f0781b379` · [字段定义](../../DATASET.md)*
