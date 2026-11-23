# essmos/nonodb

⭐ 22 · Rust · MIT · 推送 2026-11-22 · [GitHub](https://github.com/essmos/nonodb) · [官网](https://nonodb.com) · 个人维护

**面向小型 VM 与边缘设备的 JSON 文档数据库（MongoDB 风格）**

单个 Rust 二进制守护进程，面向小型 VM（512 MB–2 GB）与边缘设备提供 JSON 文档数据库：存储基于 LMDB，空闲内存约 5 MB（100 万文档+3 个索引），通过 HTTP/JSON 提供 CRUD、SQL、聚合、二级索引、TTL、文档版本历史、多库托管；支持 BM25 全文、模糊三元组/Levenshtein 与精确向量搜索；可选 MongoDB 兼容端点供 PyMongo/Node.js/Go 官方驱动接入；含备份调度、凭据管理与主从复制/故障转移，内嵌浏览器 GUI。MIT 许可，无付费分层。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制 + LMDB，空闲内存约 5 MB，含面向 512 MB–2 GB VM 的 small/tiny 配置
- 同一库内提供 BM25 全文、模糊搜索与向量搜索（cosine/dot/l2），无需外部向量服务
- MongoDB 风格查询语法，可选 wire 端点兼容 PyMongo/Node.js/Go 官方驱动
- 内嵌 GUI、加密备份（gzip/age，本地/S3/R2）与异步主从复制、自动选举

## 适用场景

- 在小型 VM 或边缘设备上托管应用的共享 JSON 状态
- 用 MongoDB 风格查询替代部署完整 MongoDB 服务
- 需要内置全文/模糊/向量搜索的嵌入式文档存储场景
- 需要轻量复制与故障转移的小型生产部署

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L13: One Rust daemon for small VMs and edge boxes: owns the LMDB files, speaks
> L41: - **Search built in** — BM25 full-text search, fuzzy trigram/Levenshtein search, and exact vector search in the sam
> L170: - Vector search with `cosine`, `dot`, and `l2` metrics. Vectors are stored in


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `de27fb0109e8` · [字段定义](../../DATASET.md)*
