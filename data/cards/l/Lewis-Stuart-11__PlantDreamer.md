# Lewis-Stuart-11/PlantDreamer

⭐ 43 · Python · Apache-2.0 · 推送 2025-11-01 · [GitHub](https://github.com/Lewis-Stuart-11/PlantDreamer) · 组织维护

**扩散模型引导的高斯泼溅 3D 植物生成框架（CVPPA@ICCVW 2025）**

面向植物表型与计算机视觉研究者的 text-to-3D 框架：以合成 L-System 网格或真实植物点云为初始化，通过扩散模型引导的高斯泼溅训练生成 3D 植物模型，目前支持 bean、kale、mint 三种植物。以 Threestudio 自定义扩展形式安装，L-System 初始化依赖 Blender（推荐 4.4）及 Blender_L-Systems 插件；新增物种需训练 LoRA（建议基于 stable-diffusion-2-1-base）并编写新的 L-System 文法。配套提供含点云、3DGS 结果与真值图像的数据集及论文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 L-System 合成网格或真实点云两种初始化方式
- 扩散引导的高斯泼溅生成 3D 植物，支持 bean/kale/mint 三种物种
- 以 Threestudio 0.2.3 自定义扩展形式集成
- 提供含真实植物点云、合成数据与训练结果的配套数据集

## 适用场景

- 从文本与 L-System 初始化生成特定物种的 3D 植物模型
- 基于实测植物点云重建 3DGS 植物模型
- 植物表型/计算机视觉研究中的 3D 植物数据生成与实验复现

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Generation of 3D plant models is difficult, with many popular text-to-3D models failing to capture the intricate geo
> L38: python launch.py --config custom/PlantDreamer/configs/plantdreamer.yaml  --train --gpu 0 system.geometry.plant_type

## 星数曲线

```mermaid
xychart-beta
    title "Lewis-Stuart-11/PlantDreamer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a94101bcd0ab` · [字段定义](../../DATASET.md)*
