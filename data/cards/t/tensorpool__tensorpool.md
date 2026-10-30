# tensorpool/tensorpool

⭐ 437 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/tensorpool/tensorpool) · [官网](https://tensorpool.dev/) · 组织维护

**通过 git 风格 CLI 提交 ML 训练任务与租用 GPU 集群**

TensorPool CLI 是面向机器学习开发者的命令行工具，提供 git 风格的接口用于提交 ML 训练任务、访问按需多节点 GPU 集群，并管理集群、存储、NFS、SSH 等资源。通过 pip 安装，要求 Python 3.8+，命令入口为 tp，覆盖 cluster/storage/nfs/job/ssh 等子命令。文档与社区分别托管于 docs.tensorpool.dev 与 Slack。

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

- git 风格接口提交 ML 训练任务
- 按需访问多节点 GPU 集群
- cluster/storage/nfs/job/ssh 等资源管理子命令
- pip 安装，支持 Python 3.8+

## 适用场景

- 用命令行提交 ML 训练任务
- 按需创建和管理多节点 GPU 集群
- 管理训练相关的存储与 NFS 资源

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L11: The TensorPool CLI is a git-style interface for running ML training jobs and accessing on-demand multi-node GPU clu
> L27: % tp --help

## 星数曲线

```mermaid
xychart-beta
    title "tensorpool/tensorpool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 436 --> 438
    line [437, 437]
```

2026-10-18 437 → 2026-10-30 437（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `30afc832bd33` · [字段定义](../../DATASET.md)*
