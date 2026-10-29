# pauloacs/DLpisoFoam

⭐ 26 · C++ · MIT · 推送 2026-10-24 · [GitHub](https://github.com/pauloacs/DLpisoFoam) · 个人维护

**面向 CFD 研究者：深度学习加速的 OpenFOAM 流体求解器集合**

包含五个机器学习增强的 OpenFOAM 求解器（DLpisoFoam、DLpisoFoam_2d、DLbuoyantPimpleFoam、DLpimpleFoam_auto、DLpimpleFoam_oracle），用深度学习代理模型估计压力及压力-速度修正以加速 CFD 收敛。提供两条工作流：Classic 离线先训练代理再部署；AUTO 在 CFD 运行中自动采样、训练并激活代理。支持等温与热流、2D/3D 案例。本地安装需 OpenFOAM v8、Python 3.11（conda）并用 wmake 编译求解器，也提供预构建 Docker 镜像；oracle 为参考场诊断，不加载学习模型，热流 AUTO 版未收录。代理用 TensorFlow 训练，输出 HDF5 模型与 Tucker/PCA 压缩工件。

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

- 五个 ML 增强求解器，代理模型输出压力/压力-速度修正的初始估计
- AUTO 工作流：单次 CFD 运行内采样、训练并激活代理，无需预训练模型
- README 声明相比标准 OpenFOAM 求解器最多减少 40% 收敛迭代次数
- 提供预构建 Docker 镜像与 2D/3D 等温/热流训练数据生成案例

## 适用场景

- 我在做流场仿真，想用预训练/在线训练的代理模型加速压力 Poisson 求解收敛
- 我有自己的 CFD 数据，想训练压力代理模型并接入 OpenFOAM 求解器
- 我想在单次仿真内完成采样、训练与加速运行（AUTO 模式）

## 场景标签

 · 领域:计算流体力学/科学机器学习

## 证据(README 行号)

> L13: This repository contains **machine learning-enhanced OpenFOAM solvers** that accelerate computational fluid dynamic
> L94: Alternatively, **sample, train and simulate in one AUTO run** using `DLpimpleFoam_auto`. In the new PIMPLE integrat
> L99: - 🧠 **ML-powered**: Machine Learning surrogate models enhance pressure Poisson solver

## 星数曲线

```mermaid
xychart-beta
    title "pauloacs/DLpisoFoam 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `04da909477ef` · [字段定义](../../DATASET.md)*
