# REASY/k8s-ariadne-rs

⭐ 22 · Rust · MIT · 推送 2026-07-23 · [GitHub](https://github.com/REASY/k8s-ariadne-rs) · 组织维护

**把 Kubernetes 集群状态建模为属性图的 MCP 服务器，供编码代理用 Cypher 查询**

Ariadne 是一个 Rust 编写的 MCP 服务器，面向编码代理：将 Kubernetes 集群状态摄取到 Memgraph 属性图中，暴露三个确定性工具——graph_query（只读 Cypher）、graph_schema（模式发现）、graph_health（新鲜度检查）。模型针对建模后的图生成 Cypher 查询，无需将原始集群状态放入上下文，适合多跳关系类问题（如 Ingress 到 Pod 的链路）。默认对环境变量值等敏感字段脱敏，仓库另含本地 CLI 调试工具与 Python 评估代理。

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

- 集群状态摄取为属性图，暴露 graph_query/graph_schema/graph_health 三个 MCP 工具
- 模型生成 Cypher，由图执行已建模的关系，避免原始 JSON 进入上下文
- 支持多跳遍历查询，并从原始对象派生 Host/Endpoint 等辅助节点
- 默认脱敏环境变量值，可选关闭以保留配置查询能力

## 适用场景

- 让编码代理回答跨资源类型的关系类 Kubernetes 问题
- 查询某个 Host 背后由哪些 Pod 支撑等链路遍历
- 查找无 EndpointSlice 的 Service、无 StorageClass 的 PV 等负向图查询

## 场景标签

 · 领域:云原生/DevOps 工具

## 证据(README 行号)

> L3: Ariadne is a Kubernetes graph MCP for coding agents. It ingests the cluster state into a property graph and exposes 
> L15: - **MCP-first**: Ariadne is designed to plug into coding agents, not replace them.

## 星数曲线

```mermaid
xychart-beta
    title "REASY/k8s-ariadne-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `da086d17f3e6` · [字段定义](../../DATASET.md)*
