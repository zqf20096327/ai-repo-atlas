# stubbi/hermes-operator

⭐ 39 · Go · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/stubbi/hermes-operator) · [官网](https://paperclip.inc/hermes-agent) · 组织维护

**在 Kubernetes 上部署管理 hermes-agent AI 代理的 Operator**

用 Go 编写的 Kubernetes Operator，以声明式 HermesInstance CR 驱动 NousResearch/hermes-agent（Python 多平台自改进 AI 代理）的完整运行栈：StatefulSet、Service、PVC、NetworkPolicy、HPA 等统一调和。机制包括默认拒绝网络策略、S3 备份与恢复、OCI 镜像自动更新加失败回滚、基于 SSA 的 HermesSelfConfig 允许代理在受保护键限制下自我修改并与 FluxCD/Argo GitOps 共存，以及从 openclaw-operator 的一次性迁移。面向平台/DevOps 工程师，通过 Helm、OLM 或 kustomize 分发，v1.0 起带版本化与弃用政策。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 HermesInstance CR 驱动全部运行栈并由 Operator 调和
- S3 备份（定时/删除前/更新前）与声明式一次性恢复
- SSA 字段管理器实现代理自我配置与 GitOps 共存不冲突
- OCI 镜像自动更新带探针失败回滚，多架构 amd64/arm64

## 适用场景

- 在 Kubernetes 集群上声明式部署和运行 hermes-agent
- 让 FluxCD/Argo 管理实例同时允许代理有限的自我配置
- 从 openclaw-operator 迁移现有部署并保留数据

## 场景标签

 · 领域:Kubernetes/DevOps

## 证据(README 行号)

> L14: Kubernetes operator for nousresearch/hermes-agent: a Python-based self-improving multi-platform AI agent. Declarati
> L15: opinionated security defaults, S3 backups, OCI-registry auto-update,
> L16: SSA-based GitOps coexistence, and a one-shot migration path from

## 星数曲线

```mermaid
xychart-beta
    title "stubbi/hermes-operator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-10-18 38 → 2026-10-27 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9f931f5025ca` · [字段定义](../../DATASET.md)*
