# mila-iqia/ResearchTemplate

⭐ 54 · Python · 推送 2026-05-06 · [GitHub](https://github.com/mila-iqia/ResearchTemplate) · [官网](https://mila-iqia.github.io/ResearchTemplate/) · 组织维护

**Mila 出品的 ML 研究项目模板：快速搭建规范研究代码库**

由 Mila 开发的机器学习研究项目模板，通过 Copier 从模板生成新项目，用 uv 管理依赖。生成的项目内置 Hydra 配置管理（支持命令行覆盖）、PyTorch Lightning 训练框架（亦可按示例改用 Jax）、Weights & Biases 指标记录与 pytest 自动化测试（含可复现性测试，支持 SLURM 集群测试）。面向已熟悉 Python、有 PyTorch 与 SLURM 基础的研究人员。README 自述为进行中的项目（work-in-progress）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 uvx copier 一条命令从模板生成新项目
- Torch 与 Jax 双支持，Hydra 配置管理
- 内置自动化测试含可复现性测试，支持 SLURM 集群
- 集成 Weights & Biases 记录指标

## 适用场景

- 新开 ML 研究课题时快速获得规范的代码骨架
- 在 SLURM 集群上跑带可复现性测试的实验
- 统一团队研究的配置管理与实验记录方式

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L11: This is a project template for ML researchers developed at Mila. Our goal with this is to help you get started with
> L47: - Hydra is used to configure the project. It allows you to define configuration files and override them from the co
> L48: - PyTorch Lightning is used to as the training framework. It provides a high-level interface to organize ML researc

## 星数曲线

```mermaid
xychart-beta
    title "mila-iqia/ResearchTemplate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-29 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8941cd62fa49` · [字段定义](../../DATASET.md)*
