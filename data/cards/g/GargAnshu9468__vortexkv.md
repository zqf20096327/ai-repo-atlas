# GargAnshu9468/vortexkv

⭐ 19 · Go · MIT · 推送 2026-10-11 · [GitHub](https://github.com/GargAnshu9468/vortexkv) · [官网](https://garganshu9468.github.io/vortexkv/) · 个人维护

**纯 Go 内存键值数据库：Redis 协议兼容并带 HNSW 向量检索**

纯 Go、零 CGO 的内存数据引擎，在专用端口 7379 上实现 RESP2/RESP3 协议，可与 redis-cli 及各语言 Redis 客户端直接配合使用。功能包括 Lua 5.1 与 Wasm 脚本引擎、Redis Streams 与消费组、AOF/RDB 持久化、主从复制、16,384 槽位集群与 gossip 故障转移、Kubernetes Operator 与 Helm Chart，以及嵌入端口 7380 的 Web 管理界面。AI 相关部分为内建 HNSW 图索引的向量命令（VADD/VSEARCH 等），支持 cosine/euclidean/dot 度量，可存储向量嵌入并做 top-K 近邻查询。提供安装脚本、Docker Compose 与源码 make build 三种部署方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RESP2/RESP3 协议兼容，端口 7379，可配合 redis-cli 与多语言 Redis 客户端
- HNSW 向量索引命令（VADD/VSEARCH/VSIM），支持三种距离度量
- Lua 5.1 与 Wasm（wazero）脚本引擎，MULTI/EXEC 原子批处理
- 集群 gossip、槽位迁移、K8s Operator 与 Prometheus /metrics

## 适用场景

- 需要 Redis 协议兼容的内存缓存与流处理场景
- 在键值库中直接存储向量嵌入并做近邻检索
- 用 Docker Compose 或 Kubernetes 部署多节点数据集群

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L6:  Drop-in Redis Alternative • Native Vector Search • Redis Streams • Cluster Gossip • Lua 5.1 & Wasm
> L42: - 🧠 **Native HNSW AI Vector Graph Indexing**: Million-scale sub-millisecond approximate nearest-neighbor search (`V

## 星数曲线

```mermaid
xychart-beta
    title "GargAnshu9468/vortexkv 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `f7b21b84b657` · [字段定义](../../DATASET.md)*
