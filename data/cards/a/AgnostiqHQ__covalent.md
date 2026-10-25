# AgnostiqHQ/covalent

⭐ 868 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/AgnostiqHQ/covalent) · [官网](https://www.covalent.xyz) · 组织维护

**面向 AI/ML 工程师的 Python 工作流编排库：一行改动在任何云/本地集群跑计算任务**

Covalent 是 Agnostiq 维护的开源 Python 库，面向 AI/ML 工程师、开发者和科研人员，用于在异构计算环境（本地、云平台、SLURM/PBS/LSF 等本地 HPC 集群）上编排运行 AI/ML 与科研计算任务。核心机制是通过装饰器与 executor 插件切换执行后端，改动一行代码即可把 Python 函数分发到云端或本地集群，并将基础设施管理抽象到后台，提供实时监控 UI。仅支持 Linux 和 macOS。Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 装饰器+executor 插件：改一行代码将 Python 函数分发到任意云或本地集群
- 支持 SLURM/PBS/LSF 本地集群与 AWS/GCP/Azure 等云环境的统一接口
- 内置实时监控 UI，支持迭代式研发
- 提供 Docker 镜像/AMI 自托管部署与 pip 本地安装两种方式

## 适用场景

- 把本地写的 ML/LLM 训练代码不改业务逻辑迁移到云或 HPC 集群
- 科研计算任务在 SLURM 集群与多云之间统一编排执行
- 对计算工作流进行实时监控与迭代调试

## 场景标签

`工作流自动化` `MLOps` · 领域:效率与自动化

## 证据(README 行号)

> L27: Covalent is a Python library for AI/ML engineers, developers, and researchers. It provides a straightforward approa
> L47:  Unified Interface Across Environments: Consistent experience with on-prem HPC clusters and cloud platforms like SL

## 星数曲线

```mermaid
xychart-beta
    title "AgnostiqHQ/covalent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 867 --> 869
    line [868, 868]
```

2026-10-18 868 → 2026-10-25 868（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e784cc1f8a59` · [字段定义](../../DATASET.md)*
