# cryoEM-CNIO/BinderFlow

⭐ 66 · Python · LGPL-3.0 · 推送 2026-09-23 · [GitHub](https://github.com/cryoEM-CNIO/BinderFlow) · 组织维护

**面向 SLURM 集群的从头蛋白 binder 设计自动化流水线**

为使用 SLURM 集群的结构生物学研究者提供的蛋白 binder 设计平台，包含两个工具：binderflow.sh 以批次方式依次运行骨架生成（RFDiffusion）、设计过滤、序列分配（ProteinMPNN）与候选打分（AF2/PyRosetta），批次机制支持与其他 GPU 任务共存并减少人工干预；BFmonitor.py 是 Web 仪表盘，用于监控设计活动、过滤设计并导出 DNA 序列用于订购。安装需克隆仓库、安装 RFDiffusion 与 dl_binder_design 分支，通过 install 脚本用 conda/mamba 建环境，还需系统安装 dssp。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 批次化流水线：骨架生成→过滤→序列分配→候选打分
- BFmonitor Web 仪表盘：实时监控、设计过滤、结构可视化与 DNA 序列导出
- 面向 SLURM 集群，支持与其他 GPU 任务共存
- 为非专家简化流程，同时为蛋白设计从业者提供新功能

## 适用场景

- 在 SLURM 集群上针对选定靶点批量设计蛋白 binder
- 实时监控设计活动进展并按指标筛选候选
- 从候选设计中提取 pdb、fasta 与 DNA 序列用于合成订购

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L7: BinderFlow provides a protein binder design platform for SLURM-based computer infrastructure users. BinderFlow eases
> L42: BinderFlow is a pipeline for protein binder design. It subdivides protein design projects, which are often run line

## 星数曲线

```mermaid
xychart-beta
    title "cryoEM-CNIO/BinderFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-28 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `787630cdab83` · [字段定义](../../DATASET.md)*
