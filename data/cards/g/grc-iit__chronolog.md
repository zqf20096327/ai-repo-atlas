# grc-iit/chronolog

⭐ 15 · C++ · BSD-2-Clause · 推送 2026-10-30 · [GitHub](https://github.com/grc-iit/chronolog) · [官网](https://chronolog.dev) · 组织维护

**面向日志与活动负载的分布式分层共享日志存储系统**

ChronoLog 是 Gnosis Research Center（伊利诺伊理工）开发的分布式分层共享日志存储：以物理时间做数据分布、无中央序列器实现全序，StoryChunks 在快慢存储层间流转，支持 RDMA/TCP 多读多写，归档可落在 NFS 共享文件系统。提供可插拔服务层，附带 SQL 查询、键值、流式、pub/sub、Grafana 可视化、HPC 遥测接入及 LLM 集成的 MCP server 等插件。提供 tarball、DEB、RPM、Docker 与源码构建五种安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 物理时间分布日志条目，无中央序列器，写入与查询路径独立扩展
- 分层存储与层间持久交接，归档支持 NFS 共享文件系统
- 可插拔服务层：SQL 查询、KV、流式、pub/sub、Grafana、LDMS 遥测、MCP server
- RDMA/TCP 上的多写多读并发访问

## 适用场景

- HPC 集群中收集与回放大规模遥测/事件流
- 为 LLM 应用提供带时间序的共享日志后端（MCP 集成）
- 需要多节点部署、可弹性扩展容量的事件存储

## 场景标签

 · 领域:分布式系统/存储基础设施

## 证据(README 行号)

> L14:  A distributed and tiered shared log storage ecosystem that uses physical time to distribute log entries while prov
> L35: A pluggable serving layer lets custom services run directly on the log. Shipping plugins cover SQL-like queries, ke

## 星数曲线

```mermaid
xychart-beta
    title "grc-iit/chronolog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `47b7de69a243` · [字段定义](../../DATASET.md)*
