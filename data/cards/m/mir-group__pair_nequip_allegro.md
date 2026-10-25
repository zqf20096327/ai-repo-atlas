# mir-group/pair_nequip_allegro

⭐ 65 · C++ · MIT · 推送 2026-10-09 · [GitHub](https://github.com/mir-group/pair_nequip_allegro) · [官网](https://arxiv.org/pdf/2504.16068) · 组织维护

**在 LAMMPS 分子模拟中运行 NequIP/Allegro 机器学习势的 pair style**

提供两个 LAMMPS pair style，把 NequIP 框架训练的消息传递 GNN 模型（pair_nequip，限单 MPI rank）与严格局部化的 Allegro 模型（pair_allegro，支持 MPI 并行）接入 LAMMPS 分子动力学模拟。模型须先用 nequip-compile 编译为 TorchScript（.pth）或 AOTI（.pt2）文件，经 pair_coeff 指定原子类型映射后加载。安装方式为下载本仓库并以 patch 脚本打补丁进 LAMMPS 源码，用 CMake 编译；需 libtorch，可选 AOTI、Kokkos（仅 Allegro）或 OpenMP 加速。要求 2025 年 9 月 10 日版或更新 LAMMPS，且 KOKKOS 包以 double-double 精度编译。面向使用机器学习势做分子模拟的科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pair_nequip（消息传递 GNN，限单 MPI rank）与 pair_allegro（局部模型，支持 MPI 并行）两个 pair style
- 模型经 nequip-compile 编译为 TorchScript/AOTI 格式后在 LAMMPS 中加载
- Kokkos GPU 加速（仅 Allegro）与 OpenMP 加速（两者均可，互斥）
- AOTI 编译路径需 PyTorch ≥ 2.6.0

## 适用场景

- 在 LAMMPS 中用已训练的 NequIP/Allegro 势跑分子动力学模拟
- GPU 集群上用 Kokkos 并行运行 Allegro 势模拟
- 将机器学习势接入现有 LAMMPS 工作流做材料模拟

## 场景标签

 · 领域:计算材料科学/分子模拟

## 证据(README 行号)

> L6: These pair styles allow you to use models from the NequIP framework in LAMMPS simulations. This repository provides 
> L44: git clone --depth=1 https://github.com/lammps/lammps

## 星数曲线

```mermaid
xychart-beta
    title "mir-group/pair_nequip_allegro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-25 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `253e58a085fe` · [字段定义](../../DATASET.md)*
