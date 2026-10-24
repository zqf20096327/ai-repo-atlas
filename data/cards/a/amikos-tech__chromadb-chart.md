# amikos-tech/chromadb-chart

⭐ 61 · Shell · MIT · 推送 2026-04-15 · [GitHub](https://github.com/amikos-tech/chromadb-chart) · 组织维护

**Helm Chart：在 Kubernetes 上部署单节点 ChromaDB**

由 Amikos Tech 维护的 Helm Chart，用于在 Kubernetes 集群上部署单节点 Chroma 向量数据库（支持 Chroma 0.4.3–1.x）。通过 values.yaml 或 --set 参数配置 PVC 持久化、镜像仓库覆盖、ServiceAccount、OTEL 遥测等；<1.0.0 版本支持 token/basic 认证（安装时生成 Secret），>=1.0.0（Rust 服务端）的 auth 等旧参数被忽略，需改用网络层安全控制。多节点部署计划由未来的 Operator 提供，当前不支持。面向在 K8s 环境运行 Chroma 的平台/DevOps 使用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Helm 一条命令部署单节点 ChromaDB，支持 0.4.3–1.x 版本
- PVC 持久化、存储类、数据卷大小与保留策略可配置
- 支持镜像仓库覆盖与 imagePullSecrets（适配离线/私有环境）
- 旧版 token/basic 认证开箱启用（<1.0.0），含验证用 curl/kubectl 流程

## 适用场景

- 在现有 Kubernetes 集群上部署 Chroma 向量数据库供应用调用
- 气隙或私有镜像环境下部署带镜像覆盖配置的 ChromaDB
- 为 RAG 应用提供集群内的向量存储实例

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L1: # Kubernetes Chart for Chroma AI application database
> L5: This chart deploys a single-node Chroma database on a Kubernetes cluster using the Helm package manager.

## 星数曲线

```mermaid
xychart-beta
    title "amikos-tech/chromadb-chart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-24 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `2ea8ef9d78b6` · [字段定义](../../DATASET.md)*
