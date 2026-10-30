# Dakera-AI/dakera-deploy

⭐ 19 · JavaScript · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/Dakera-AI/dakera-deploy) · [官网](https://dakera.ai/docs) · 组织维护

**AI agent 记忆服务器的自托管部署仓库：Docker/K8s/Helm**

Dakera agent 记忆平台的官方部署仓库，提供 Docker Compose、Kubernetes manifests 与 Helm 三类部署路径。服务本体为单个自托管 Rust 二进制，内置向量检索（HNSW）、BM25 混合检索、知识图谱、会话管理与嵌入生成，无外部依赖。提供 local/dev/default/ha/monitoring/kubernetes 多种部署 profile：本地零配置内存模式、MinIO 持久化、3 节点 Traefik 高可用集群、Prometheus+Grafana 监控。含 Dashboard 与 REST/gRPC API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单个 Rust 二进制内置向量+BM25 混合检索、知识图谱与嵌入生成，无外部依赖
- local/dev/default/ha/monitoring/kubernetes 多档部署 profile
- 3 节点 gossip 集群 + Traefik 负载均衡的 HA 配置
- Dashboard 0.5.2 以非特权 uid 10001 运行、服务端会话持有 API key

## 适用场景

- 自托管 AI agent 的持久化跨会话记忆后端
- 为多 agent 管线提供共享记忆与会话隔离
- 在 Kubernetes/Helm 环境部署生产级记忆服务
- 为部署附加 Prometheus + Grafana 监控

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Deploy AI agent memory anywhere — Docker, Kubernetes, or Helm.
> L44: Dakera is the **agent-native memory platform** — purpose-built for AI agents that need persistent, session-aware, c
> L52: |**Multi-agent pipelines**|Shared cross-agent memory, session isolation per agent, importance-ranked recall|

## 星数曲线

```mermaid
xychart-beta
    title "Dakera-AI/dakera-deploy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `1f40434f110b` · [字段定义](../../DATASET.md)*
