# awslabs/kubeflow-manifests

⭐ 186 · YAML · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/awslabs/kubeflow-manifests) · [官网](https://awslabs.github.io/kubeflow-manifests/) · 组织维护

**Kubeflow 在 AWS 上的发行版：提供集成 AWS 服务的 manifests 部署方案**

AWS 维护的 Kubeflow 开源发行版仓库，核心内容是一套 Kubeflow manifests，用于将 Kubeflow 部署到 Amazon EKS，并与多种 AWS 托管服务集成，目标是减少机器学习系统搭建的运维负担。README 本身较简略：仅含概述、指向 Kubeflow on AWS 官网部署文档的入口，以及问题反馈、贡献与安全说明。采用 Apache-2.0 许可证，实际部署步骤需参考外部网站文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Kubeflow on AWS 专属 manifests 发行版
- 支持与多种 AWS 托管服务集成
- 面向 Amazon EKS 的部署方案
- Apache-2.0 许可证

## 适用场景

- 在 AWS EKS 上部署 Kubeflow 机器学习平台
- 让数据科学团队使用与 AWS 服务集成的 Kubeflow 环境
- 降低自建 MLOps 基础设施的运维成本

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L8: Kubeflow on AWS is an open source distribution of Kubeflow that provides its own Kubeflow manifests to support integ
> L12: There are a number of deployment options for installing Kubeflow with AWS service integrations. To get started with

## 星数曲线

```mermaid
xychart-beta
    title "awslabs/kubeflow-manifests 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 185 --> 187
    line [186, 186]
```

2026-10-18 186 → 2026-10-30 186（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `10e381dfd7af` · [字段定义](../../DATASET.md)*
