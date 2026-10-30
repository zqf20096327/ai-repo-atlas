# AHHHZ975/Semantic-Visibility-UV-Param

⭐ 19 · Python · 推送 2026-08-21 · [GitHub](https://github.com/AHHHZ975/Semantic-Visibility-UV-Param) · [官网](https://ahhhz975.github.io/Automatic3DMeshParameterization/) · 组织维护

**ICLR 2026 论文官方代码：无监督 3D 网格 UV 参数化**

论文《Unsupervised Representation Learning for 3D Mesh Parameterization with Semantic and Visibility Objectives》（ICLR 2026 接收）的官方实现。框架在保持几何的 UV 学习上加入语义与可见性目标：先将网格分割为语义部件，用无监督逐部件 UV 参数化骨干生成并聚合为统一 UV 图集；可见性方面以环境光遮蔽（AO）为暴露代理，通过可微软 AO 加权接缝目标使切缝偏向遮挡区域。依赖 SAMesh（含 SAM2）做 3D 分割，需 NVIDIA GPU 与 CUDA，编译安装 CD/EMD 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语义感知：网格分割为语义部件后逐部件 UV 参数化并聚合为统一图集
- 可见性感知：可微 AO 加权接缝目标使切缝偏向遮挡区域
- 提供 SAMesh 与 ShDF 两种 3D 分割基座的可选运行路径
- 覆盖训练、推理与 UV 图集聚合的完整命令

## 适用场景

- 对 3D 网格自动生成 UV 展开以替代手工 UV 映射
- 为 3D 生成管线的纹理生成提供接缝更不显眼的 UV 图集
- 复现论文的定性/定量实验结果

## 场景标签

 · 领域:计算机图形学/3D 深度学习

## 证据(README 行号)

> L1: The code for the paper:
> L2: # Unsupervised Representation Learning for 3D Mesh Parameterization with Semantic and Visibility Objectives
> L9: Recent 3D generative models produce high-quality textures for 3D mesh objects. However, they commonly rely on the he

## 星数曲线

```mermaid
xychart-beta
    title "AHHHZ975/Semantic-Visibility-UV-Param 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `1dbfe63d32ec` · [字段定义](../../DATASET.md)*
