# arcadelab/deepdrr

⭐ 283 · Python · GPL-3.0 · 推送 2026-01-07 · [GitHub](https://github.com/arcadelab/deepdrr) · 组织维护

**从 CT 与网格仿真 X 光影像（DRR）的 GPU 框架，供合成训练数据**

基于 GPU 的数字影像重建放射图（DRR）仿真框架：读取 3D CT 体数据与网格，结合机器学习模型（材质分解、散射估计）与解析模型（投影、衰减、噪声注入），批量生成合成 X 光影像，用于训练医学影像机器学习模型。支持多体重叠、不同材质的网格渲染；非可微渲染器。需 Linux + NVIDIA GPU + CUDA，推荐 conda/mamba 从源码安装；材质分解模型基于 NIH 数据训练，散射估计目前仅限 Rayleigh 散射，且部分工具插入功能未经 1.0 版本测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结合 ML 材质分解与散射估计 + 解析投影/衰减/噪声注入的仿真管线
- 从 CT 体数据与网格批量生成合成 X 光影像数据集
- 支持多种 CUDA 版本的 cupy 安装选项（10.2–12.x）
- 提供 Python API（Volume/Projector/Mesh）与 Colab 演示

## 适用场景

- 为 X 光影像分割/检测模型生成大规模合成训练数据
- 手术导航与透视引导流程的仿真验证
- 机器人 C 臂与手术工具的 X 光成像模拟

## 场景标签

 · 领域:医学影像/手术仿真

## 证据(README 行号)

> L25: DeepDRR is a GPU-based framework for efficient simulation of X-ray images—or digitally reconstructed radiographs (D
> L130: DeepDRR combines machine learning models for material decomposition and scatter estimation in 3D and 2D, respectiv

## 星数曲线

```mermaid
xychart-beta
    title "arcadelab/deepdrr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 282 --> 284
    line [283, 283]
```

2026-10-18 283 → 2026-10-27 283（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8c9bfffaedcc` · [字段定义](../../DATASET.md)*
