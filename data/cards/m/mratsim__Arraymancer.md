# mratsim/Arraymancer

⭐ 1,415 · Nim · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/mratsim/Arraymancer) · [官网](https://mratsim.github.io/Arraymancer/) · 个人维护

**Nim 语言的张量计算与深度学习库，支持 CPU/CUDA/OpenCL**

用 Nim 编写的 N 维张量（ndarray）库，提供切片、广播、重塑、读写 .csv/.npy/HDF5 等张量操作，矩阵代数与 K-means/PCA/最小二乘等机器学习原语，以及全连接、卷积、循环神经网络定义与自动微分等深度学习能力。后端可选 OpenMP、CUDA、OpenCL 与 CuDNN，通过编译开关启用。张量部分可不依赖机器学习组件单独使用；深度学习接口自述仍在开发中、不稳定。面向需要在 Nim 中进行科学计算与建模的开发者与研究人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- CPU/CUDA/OpenCL 多后端张量，编译开关切换（-d:cuda/-d:openmp 等）
- 张量可读写 .csv、Numpy .npy 与 HDF5 文件
- 支持神经网络定义、模型组合与自定义层（接口自述为 work in progress）
- 模型可打包为仅依赖 BLAS 库的自包含二进制，适配移动设备与树莓派

## 适用场景

- 在 Nim 中做数值计算与张量运算，替代 Python 数科栈的原型到生产两次开发
- 编写并训练全连接/卷积/循环神经网络模型
- 将模型部署到资源受限设备（手机、树莓派、Tegra）

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: Arraymancer is a tensor (N-dimensional array) project in Nim. The main focus is providing a fast and ergonomic CPU, 
> L140: ### Arraymancer as a Deep Learning library

## 星数曲线

```mermaid
xychart-beta
    title "mratsim/Arraymancer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 1413 --> 1416
    line [1414, 1415]
```

2026-10-18 1,414 → 2026-10-22 1,415（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `95c09cc51551` · [字段定义](../../DATASET.md)*
