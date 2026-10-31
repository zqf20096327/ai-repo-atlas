# epam/statgpt-helm

⭐ 14 · MIT · 推送 2026-10-29 · [GitHub](https://github.com/epam/statgpt-helm) · [官网](https://statgpt.dialx.ai) · 组织维护

**StatGPT 的 Helm Chart 部署仓库：Kubernetes 安装图表**

由 EPAM 维护的 Helm Chart 仓库，用于在 Kubernetes 上部署 StatGPT（一个结合 LLM 与 SDMX 统计数据的应用）。提供标准 Helm 工作流：helm repo add 添加仓库、helm install 安装 statgpt chart、helm delete 卸载，可通过 helm search 查询版本。README 仅含安装说明，不含应用功能细节；采用 MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 statgpt 的 Helm Chart 分发
- 支持 helm repo add / install / delete 标准工作流
- 含 GitHub Release 与 CI Workflow 状态徽章

## 适用场景

- 在 Kubernetes 集群上部署 StatGPT
- 通过 Helm 包管理器安装和升级 StatGPT

## 场景标签

 · 领域:云原生部署/LLM应用

## 证据(README 行号)

> L1: # StatGPT Helm Repository
> L9: Helm must be installed to use the charts. Please refer to Helm's documentation to get started.

## 星数曲线

```mermaid
xychart-beta
    title "epam/statgpt-helm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `80a0c2a79fbc` · [字段定义](../../DATASET.md)*
