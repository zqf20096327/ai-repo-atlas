# CliMA/ClimaAtmos.jl

⭐ 130 · Julia · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/CliMA/ClimaAtmos.jl) · [官网](https://clima.github.io/ClimaAtmos.jl/dev/) · 组织维护

**CliMA 地球系统模式的全球大气模拟器，支持 GPU 运行**

CliMA 地球系统模式的大气分量：求解立方球面与柱网格上的可压缩大气运动方程，含湍流对流（PROPHET 方案）、云微物理与 RRTMGP 辐射参数化；参数化方案面向数据同化与机器学习校准设计。基于 ClimaCore.jl，同一代码库可运行于 CPU 与 NVIDIA GPU，提供 Julia 包安装、YAML/脚本配置、NetCDF/HDF5 诊断输出、重启与检查点功能。面向气候模拟科研用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 立方球面/柱网格求解可压缩大气方程，全球与单柱配置
- PROPHET 涡扩散质量通量方案，面向数据同化与 ML 校准
- 同一代码库运行于 CPU 与 NVIDIA GPU
- ERA5/GCM 驱动的初始条件与强迫，NetCDF/HDF5 输出

## 适用场景

- 开展全球或单柱大气过程模拟实验
- 作为 CliMA 耦合地球系统模式的大气分量
- 进行需长时间运行与重启的气候模拟

## 场景标签

 · 领域:气候科学/科学计算

## 证据(README 行号)

> L5: The atmosphere model of the CliMA Earth System Model: a GPU-capable global atmosphere model designed for calibration
> L7: ClimaAtmos.jl solves the compressible equations of atmospheric motion on cubed-sphere and column grids, with physics

## 星数曲线

```mermaid
xychart-beta
    title "CliMA/ClimaAtmos.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 129 --> 131
    line [130, 130]
```

2026-10-18 130 → 2026-10-29 130（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6fa068030e85` · [字段定义](../../DATASET.md)*
