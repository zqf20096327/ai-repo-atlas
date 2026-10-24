# lab-cosmo/upet

⭐ 244 · Python · BSD-3-Clause · 推送 2026-10-02 · [GitHub](https://github.com/lab-cosmo/upet) · [官网](https://lab-cosmo.github.io/upet/latest) · 组织维护

**覆盖全元素周期表的通用原子间势模型包，用于材料/分子模拟**

UPET 提供基于 Point Edge Transformer (PET) 架构的通用机器学习原子间势家族（PET-MAD、PET-OAM、PET-OMat、PET-OMATPES、PET-SPICE），跨周期表预测体系能量与原子力，另含预测电子态密度、费米能级与带隙的 PET-MAD-DOS 模型。检查点托管于 HuggingFace，首次调用自动下载并本地缓存。通过 pip 安装，提供 ASE 计算器接口，并支持 LAMMPS（含 KOKKOS GPU）、i-PI、TorchSim、GROMACS 及 NVIDIA ALCHEMI Toolkit 集成与微调。面向材料模拟与分子动力学领域的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多家族预训练通用原子间势，PET-MAD-1.6 覆盖 102 种元素
- PET-MAD-DOS 预测电子态密度、费米能级与带隙
- ASE 计算器接口与 LAMMPS/i-PI/TorchSim/GROMACS/ALCHEMI 等多模拟器集成
- 检查点自动从 HuggingFace 下载并本地缓存

## 适用场景

- 在 ASE/LAMMPS 等工作流中做分子动力学与结构弛豫
- 预测材料的电子态密度、费米能级与带隙
- 材料发现筛选中批量评估能量与力

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L30: **UPET** is a family of universal interatomic potentials for advanced materials
> L33: and they are capable of predicting energies and forces in complex atomistic
> L34: workflows. The package also ships **PET-MAD-DOS**, a universal model for

## 星数曲线

```mermaid
xychart-beta
    title "lab-cosmo/upet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 242 --> 245
    line [243, 244, 244]
```

2026-10-18 243 → 2026-10-24 244（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `b9dfba064ba6` · [字段定义](../../DATASET.md)*
