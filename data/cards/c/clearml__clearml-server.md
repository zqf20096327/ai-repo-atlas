# clearml/clearml-server

⭐ 470 · Python · NOASSERTION · 推送 2026-03-24 · [GitHub](https://github.com/clearml/clearml-server) · [官网](https://clear.ml/docs) · 组织维护

**ClearML 自托管后端服务器：实验管理与协作的基础设施**

ClearML 实验管理套件的自托管后端服务，包含 Web 应用（实验浏览与管理 UI）、RESTful API（记录与查询实验信息、统计和结果）以及存储图像与模型的本地文件服务器。支持多用户协作，可通过 Docker、AWS EC2 AMI、GCP 镜像或 Kubernetes 部署；dockerized 部署自 0.15 版起附带 ClearML-Agent Services 容器，可运行自动扩缩、流水线控制器、超参优化等长时任务。可手动启用 Web 登录认证与无响应实验看门狗。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Web UI + RESTful API + 本地文件服务器三组件架构
- 支持 Docker、AWS/GCP 镜像与 Kubernetes（含 Helm）多种部署方式
- 内置 ClearML-Agent Services 容器，运行自动扩缩、流水线、超参优化等长时任务
- 可启用 Web 登录认证与无响应实验看门狗

## 适用场景

- 团队自托管 ClearML 服务器替代官方免费托管服务
- 实验记录、日志与模型的集中存储和协作管理
- 在 Kubernetes 集群上运行实验管理基础设施

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L11: The **ClearML Server** is the backend service infrastructure for ClearML.
> L19: * RESTful API for:

## 星数曲线

```mermaid
xychart-beta
    title "clearml/clearml-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 469 --> 471
    line [470, 470]
```

2026-10-18 470 → 2026-10-28 470（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d096dba845b3` · [字段定义](../../DATASET.md)*
