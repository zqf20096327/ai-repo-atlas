# redhat-na-ssa/demo-ai-gitops-catalog

⭐ 18 · HTML · MIT · 推送 2026-09-03 · [GitHub](https://github.com/redhat-na-ssa/demo-ai-gitops-catalog) · [官网](https://redhat-na-ssa.github.io/demo-ai-gitops-catalog/) · 组织维护

**OpenShift 上供给 AI/ML 工作负载的 GitOps 配置与演示目录**

由 Red Hat 北美 SA 组织维护的配置目录：以 kustomize 配置与 Argo 应用形式，在 OpenShift 4.14+ 集群上供给支持机器学习与 AI 工作负载的基础设施，涵盖 operator 安装、GPU 相关 overlay（如 devspaces-nvidia-gpu-autoscale、rhoai-workshop-ready）、登录配置、serverless/ACS operator 等。使用方式为 `oc apply -k` 或封装函数 `apply_firmly` 逐项应用，另有 bootstrap.sh 交互脚本与 shell 函数库。README 声明仓库处于频繁破坏性变更阶段，引用需固定 commit hash 或 tag。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- kustomize 配置目录，逐项或整体应用到 OpenShift 集群
- 提供 GPU 相关 overlay（Dev Spaces + NVIDIA GPU 自动扩缩、RHOAI workshop）
- apply_firmly 函数解决 CRD 先于 CR 创建导致的首次 apply 失败
- bootstrap.sh 交互脚本处理非声明式配置步骤

## 适用场景

- 在 OpenShift 集群上快速搭建 AI/ML 演示或实验环境
- 参考现成 kustomize 配置与 Argo 应用组织自己的 GitOps
- 为 workshop 批量配置多用户环境

## 场景标签

 · 领域:云原生/基础设施配置

## 证据(README 行号)

> L6: This project is a catalog of configurations used to provision infrastructure, on
> L9: The intention of this repository is to help support practical use of OpenShift for AI / ML workloads and provide a c

## 星数曲线

```mermaid
xychart-beta
    title "redhat-na-ssa/demo-ai-gitops-catalog 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `156644582525` · [字段定义](../../DATASET.md)*
