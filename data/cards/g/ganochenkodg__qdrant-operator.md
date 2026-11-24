# ganochenkodg/qdrant-operator

⭐ 55 · JavaScript · MIT · 推送 2026-11-24 · [GitHub](https://github.com/ganochenkodg/qdrant-operator) · 个人维护

**K8s 运维者：声明式部署与运维 Qdrant 向量数据库集群**

一个 Kubernetes operator，通过 QdrantCluster 与 QdrantCollection 两个 CRD 声明式管理 Qdrant 集群与集合：支持单/多节点集群创建与扩缩、读写/只读 API key 认证、客户端与节点间 TLS 加密、副本/分片/索引/量化配置、容斥与拓扑调度，以及即时与定时快照备份到 S3 兼容存储；operator 自身以集群模式运行并做 leader 选举。需 Kubernetes 1.26+，用 kubectl 安装 CRD 与 operator 后即可部署集群。项目声明仍在开发中，可能与新版本不兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- QdrantCluster/QdrantCollection 两个 CRD 声明式管理集群与集合
- API key 认证（读-写/只读）、TLS 双向加密、自动生成或自带证书
- 即时与定时快照备份至任意 S3 兼容存储
- operator 集群模式 leader 选举保证高可用

## 适用场景

- 在 Kubernetes 上声明式部署并扩缩 Qdrant 向量数据库集群
- 为 RAG/相似度检索后端配置认证、TLS 与副本分片
- 将向量库集合快照定时备份到 S3 兼容存储

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3:  Kubernetes operator for the Qdrant Vector Database.
> L17: The operator provides the following functionality:
> L32: The operator includes two custom resources - `QdrantCluster` and `QdrantCollection`. Install the CRDs by running th


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `af6e55b9deca` · [字段定义](../../DATASET.md)*
