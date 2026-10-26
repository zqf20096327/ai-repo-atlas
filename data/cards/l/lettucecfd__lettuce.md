# lettucecfd/lettuce

⭐ 296 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/lettucecfd/lettuce) · 组织维护

**基于 PyTorch 与格子玻尔兹曼方法的 CFD 仿真框架**

面向计算流体力学研究者的 Python 仿真框架：以格子玻尔兹曼方法（LBM）求解流体问题，计算后端采用 PyTorch，支持 GPU 加速与 2D/3D 仿真，含自定义 PyTorch 扩展实现原生 CUDA 核，并集成神经网络与自动微分用于增强 LBM。通过 PyPI（lettucecfd，需 Python 3.12+）安装，提供 lettuce 命令行工具做收敛性检验与基准测试；CUDA 为可选路径，亦支持 CPU 运行。附论文与 CFDML2021 演讲资料。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PyTorch 后端的格子玻尔兹曼 2D/3D 流体仿真
- 自定义 PyTorch 扩展提供原生 CUDA 核
- 集成神经网络与自动微分增强 LBM
- 提供 lettuce CLI（convergence / benchmark）与 Jupyter 示例

## 适用场景

- 我在 GPU 上跑 2D/3D 流体力学仿真
- 我把神经网络或自动微分结合进 LBM 研究流场问题
- 我需要快速原型验证 CFD 算法

## 场景标签

 · 领域:科学计算/计算流体力学

## 证据(README 行号)

> L9: Lettuce is a Computational Fluid Dynamics framework based on the lattice Boltzmann method (LBM).
> L13: - **Advanced Techniques**: Integrates neural networks and automatic differentiation to enhance LBM.

## 星数曲线

```mermaid
xychart-beta
    title "lettucecfd/lettuce 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 295 --> 297
    line [296, 296]
```

2026-10-18 296 → 2026-10-26 296（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `6cfb34b9a0b7` · [字段定义](../../DATASET.md)*
