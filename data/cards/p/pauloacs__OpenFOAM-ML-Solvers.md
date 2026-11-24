# pauloacs/OpenFOAM-ML-Solvers

⭐ 26 · C++ · MIT · 推送 2026-11-22 · [GitHub](https://github.com/pauloacs/OpenFOAM-ML-Solvers) · 个人维护

**用深度学习代理模型加速 OpenFOAM CFD 模拟的求解器集**

一组基于 OpenFOAM 的机器学习增强 CFD 求解器，覆盖等温与热流动：用深度学习代理模型估算压力与压力-速度修正，加速 PISO/PIMPLE 求解。提供两种工作流——离线生成数据并训练代理模型后部署，以及 AUTO 模式在模拟运行中采样、训练并激活模型；另有 oracle 求解器回放参考场作积分对比诊断。模型输出为 HDF5（TensorFlow）格式，附 Tucker/PCA 压缩工件。求解器需用 wmake 编译，支持 Docker 预构建镜像或本地 OpenFOAM v8 + Conda 环境。README 声称相较标准求解器收敛迭代最多减少 40%。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个 DL 增强求解器源码，替代 pisoFoam 与 buoyantPimpleFoam 的工作流
- AUTO 模式在 CFD 运行中自动采样并训练代理模型，无需预训练模型
- 支持 gridded CNN 与 mesh-graph 代理后端，含压力-速度联合预测
- 提供 2D/3D 代理模型与预构建 Docker 镜像

## 适用场景

- 为芯片阵列散热、绕流等场景加速 CFD 模拟收敛
- 在单次模拟内完成采样、训练与代理模型部署
- 用 oracle 参考场对比评估代理模型积分收益

## 场景标签

 · 领域:科学计算/流体力学仿真

## 证据(README 行号)

> L11: This repository contains **machine learning-enhanced OpenFOAM solvers** that accelerate computational fluid dynamic
> L91: Alternatively, **sample, train and simulate in one AUTO run** using `DLpimpleFoam_auto`. In the new PIMPLE integrat
> L98: - 🔧 **OpenFOAM compatible**: Drop-in replacement for `pisoFoam` and `buoyantPimpleFoam`

## 星数曲线

```mermaid
xychart-beta
    title "pauloacs/OpenFOAM-ML-Solvers 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-24"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-11-15 26 → 2026-11-24 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 low · 依据 README sha `03fae532a6a3` · [字段定义](../../DATASET.md)*
