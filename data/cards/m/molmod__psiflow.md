# molmod/psiflow

⭐ 144 · Python · MIT · 推送 2026-04-28 · [GitHub](https://github.com/molmod/psiflow) · [官网](https://molmod.github.io/psiflow/) · 组织维护

**面向化学与材料科学的可扩展分子模拟引擎**

psiflow 是用于化学和材料科学应用的分子模拟 Python 库：支持多层级量子力学计算（CP2K/GPAW/ORCA）、可训练与通用机器学习势（如 MACE-MP0）以及多种采样算法（NVE/NVT/NPT、路径积分分子动力学、metadynamics 等，借助 i-PI 与 PLUMED）。基于 Parsl 并行执行库，可将自定义工作流自动提交到本地、HPC 或云基础设施运行；重计算任务通过预配置 Apptainer/Singularity 容器执行，无需额外编译，也无需数据库或服务器；不支持自动化 VASP 计算。安装通过一键脚本创建 micromamba 环境，需提供 config.yaml 定义计算资源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 GGA/杂化 DFT、MP2/RPA、耦合簇等级别的量子力学计算（CP2K/GPAW/ORCA）
- 基于 Parsl 在本地/HPC/云上自动执行任意复杂工作流，可扩展至数千节点
- 重计算任务（QM、PyTorch 训练、i-PI 动力学）运行于预配置 Apptainer/Singularity 容器，无需额外软件编译
- 提供可训练相互作用势与通用势（如 MACE-MP0）

## 适用场景

- 在 HPC 集群上运行大规模分子模拟流水线（数据生成、ML 势训练、采样）
- 在本地工作站执行小规模模拟或调试
- 组合量子力学计算、机器学习势与增强采样进行材料/化学建模

## 场景标签

 · 领域:计算化学/材料模拟

## 证据(README 行号)

> L13: Psiflow is a scalable molecular simulation engine for chemistry and materials science applications.
> L16: - **trainable interaction potentials** as well as easy-to-use universal potentials, e.g. MACE-MP0
> L21: To achieve this, psiflow is built using Parsl: a parallel execution library which manages job submission and worklo

## 星数曲线

```mermaid
xychart-beta
    title "molmod/psiflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 143 --> 145
    line [144, 144]
```

2026-10-18 144 → 2026-10-24 144（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b9486b2ed63e` · [字段定义](../../DATASET.md)*
