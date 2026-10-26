# atomind-ai/mlip-arena

⭐ 109 · Jupyter Notebook · Apache-2.0 · 推送 2026-07-02 · [GitHub](https://github.com/atomind-ai/mlip-arena) · [官网](https://huggingface.co/spaces/atomind/mlip-arena) · 组织维护

**机器学习原子间势（MLIP）的基准评测平台，评估物理合理性**

面向基础机器学习原子间势（MLIP）的统一基准平台，评测维度覆盖结构优化、状态方程、分子动力学（NVE/NVT/NPT）、声子、弹性模量、过渡态等任务，对模型架构与训练数据集保持中立。基于 Prefect 工作流编排，支持任务/流链接、缓存与并行扩展；提供 MLIPEnum 统一接口遍历运行已编译的各 MLIP，支持通过 PyPI 或源码脚本安装（源码安装附带预训练模型），并支持在 SLURM 集群经 Dask-Jobqueue 分布式提交。被 NeurIPS 2025 接收为 Spotlight。

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

- 提供 OPT/EOS/MD/PHONON/NEB/ELASTICITY 等模块化基准任务
- 基于 Prefect 的工作流编排，支持任务链接、缓存与并行扩展
- MLIPEnum 统一接口遍历运行多个已编译 MLIP
- 支持 SLURM 集群上经 Dask-Jobqueue 分布式运行基准

## 适用场景

- 评测自己训练或贡献的 MLIP 在多类物理任务上的表现
- 在 HPC 集群上并行批量运行基准扫描
- 以 ASE Calculator 或 Hugging Face 模型形式接入新模型进行评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L2:  Fair and transparent benchmark of foundation machine learning interatomic potentials (MLIPs)
> L21: **MLIP Arena** introduces a unified, cutting-edge benchmark platform for evaluating foundation MLIP performance far

## 星数曲线

```mermaid
xychart-beta
    title "atomind-ai/mlip-arena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-26 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `19293f724728` · [字段定义](../../DATASET.md)*
