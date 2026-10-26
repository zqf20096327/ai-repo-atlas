# mir-group/allegro

⭐ 506 · Python · MIT · 推送 2026-05-29 · [GitHub](https://github.com/mir-group/allegro) · [官网](https://nequip.readthedocs.io/projects/allegro) · 组织维护

**面向计算化学的 E(3) 等变机器学习原子间势模型包**

Allegro 是 NequIP 框架的扩展包，实现 E(3) 等变机器学习原子间势模型，用于训练、测试与使用分子动力学模拟中的力场模型。提供 LAMMPS 插件 pair_allegro，支持 Kokkos 加速、MPI 与多 GPU 并行模拟；支持 CuEquivariance 集成与自定义 Triton 内核的 GPU 加速（二者互斥）。通过 PyPI（包名 nequip-allegro）安装，依赖 nequip 包与其对应的 PyTorch 版本。面向材料科学与药物发现等领域的原子尺度模拟研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 E(3) 等变机器学习原子间势模型
- NequIP 框架扩展包，提供训练配置示例
- LAMMPS 插件 pair_allegro，支持 Kokkos/MPI/多 GPU 并行
- CuEquivariance 与自定义 Triton 内核 GPU 加速选项

## 适用场景

- 训练分子动力学模拟用的机器学习力场
- 在 LAMMPS 中以 Allegro 势运行大规模原子模拟
- 材料与生物分子体系的原子尺度建模

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L8: This package implements the Allegro E(3)-equivariant machine learning interatomic potential.
> L29: The `allegro` package provides the Allegro model for use within the NequIP framework.

## 星数曲线

```mermaid
xychart-beta
    title "mir-group/allegro 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 504 --> 507
    line [505, 506, 506]
```

2026-10-18 505 → 2026-10-26 506（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9b2fdb58ce55` · [字段定义](../../DATASET.md)*
