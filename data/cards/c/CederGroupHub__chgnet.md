# CederGroupHub/chgnet

⭐ 413 · Python · NOASSERTION · 推送 2026-09-15 · [GitHub](https://github.com/CederGroupHub/chgnet) · [官网](https://doi.org/10.1038/s42256-023-00716-3) · 组织维护

**带电荷推断的通用神经网络势，用于原子级材料模拟**

CHGNet 是在 Materials Project 超过 150 万结构（146k 化合物）的 GGA/GGA+U DFT 轨迹上预训练的图神经网络势，可直接预测给定结构的能量、力、应力和磁矩，支持电荷与磁性推断，精度接近 DFT。面向计算材料科研人员，提供分子动力学（经 ASE 或 LAMMPS）、结构优化、微调训练等流程，多版本预训练权重可选。README 声明新实现已迁移至 MatGL 仓库，本仓库作为遗留实现仅限关键缺陷修复。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预测能量/力/应力/磁矩，经 DFT 磁矩正则化实现电荷推断
- 在 150 万+ 结构的 MPtrj 数据集上预训练，覆盖全元素周期表
- 支持分子动力学（ASE/LAMMPS）、结构优化与自定义数据微调
- 运行于 CPU、CUDA、Intel XPU、Apple MPS 并自动选择设备

## 适用场景

- 用预训练模型快速预测晶体结构性质，替代高成本 DFT 计算
- 运行电荷感知的分子动力学模拟并输出轨迹与磁矩
- 对特定体系微调以获得更高精度的势函数

## 场景标签

`科研工具` `微调` · 领域:学习与行业

## 证据(README 行号)

> L14: **C**rystal **H**amiltonian **G**raph neural **Net**work is pretrained on the GGA/GGA+U static and relaxation traje
> L82: Pretrained `CHGNet` can predict the energy (eV/atom), force (eV/A), stress (GPa) and

## 星数曲线

```mermaid
xychart-beta
    title "CederGroupHub/chgnet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 412 --> 415
    line [413, 414, 413]
```

2026-10-18 413 → 2026-10-28 413（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ebfbe163d5f9` · [字段定义](../../DATASET.md)*
