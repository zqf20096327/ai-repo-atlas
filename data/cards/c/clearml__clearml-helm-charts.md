# clearml/clearml-helm-charts

⭐ 50 · Go Template · 推送 2026-06-08 · [GitHub](https://github.com/clearml/clearml-helm-charts) · [官网](https://clear.ml/docs) · 组织维护

**ClearML 服务端在 Kubernetes 上的 Helm 部署 charts**

ClearML 官方提供的 Helm chart 仓库，用于在 Kubernetes 集群上部署 clearml-server 及 agent、serving 组件。clearml-server 是 ClearML 的后端服务，包含实验管理 Web UI、记录与查询实验信息/统计/结果的 RESTful API、以及存储图像和模型的本地文件服务器；默认 ClearML 使用定期重置的公开 demo 服务器，自托管需安装 clearml-server 并将客户端指向它。许可为 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 clearml-server / agent / serving 三个 chart
- server 含 Web UI、RESTful API 与本地文件服务器
- 支持多用户协作管理实验
- Apache 2.0 许可

## 适用场景

- 在自有 Kubernetes 集群自托管 ClearML 服务端
- 替代公开 demo 服务器进行长期实验管理
- 部署 ClearML agent 与 serving 组件

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: Helm charts provided by ClearML, ready to launch on Kubernetes using Kubernetes Helm.
> L9: The **clearml-server** is the backend service infrastructure for ClearML.
> L22: Use this repository to deploy **clearml-server** on Kubernetes clusters.

## 星数曲线

```mermaid
xychart-beta
    title "clearml/clearml-helm-charts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-26 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eb487cfb745b` · [字段定义](../../DATASET.md)*
