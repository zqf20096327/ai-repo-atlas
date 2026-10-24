# Tencent-Hunyuan/R-DMesh

⭐ 64 · Python · 推送 2026-08-11 · [GitHub](https://github.com/Tencent-Hunyuan/R-DMesh) · [官网](https://r-dmesh.github.io/) · 组织维护 · 中文 README

**视频驱动的 4D 网格动画生成框架（SIGGRAPH 2026 论文官方代码）**

腾讯混元与华中科大合作的 SIGGRAPH 2026 论文官方实现：给定静态网格与参考视频，自动将网格校正到视频起始姿态并生成时间一致的动态网格动画；支持姿态重定向、动作重定向与整体 4D 生成。机制上包含 R-DMesh VAE（压缩动态网格到隐空间，采用 AnimateAnyMesh++ 的 PLTA attention）与条件 Diffusion Transformer，以 Wan2.2-TI2V-5B 提取视频隐特征作为条件。提供推理脚本与 6 阶段训练流程；自定义驱动视频需先做抠图去背景（纯黑背景），数据构建部分代码尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 静态网格+参考视频生成动态网格动画，自动校正初始姿态
- 支持姿态重定向、动作重定向与整体 4D 生成
- R-DMesh VAE + 条件 DiT 架构，视频条件来自 Wan2.2-TI2V-5B
- 提供 6 阶段训练流程与 HuggingFace 预训练权重

## 适用场景

- 用一段参考视频驱动已有 3D 角色网格生成动画
- 做姿态/动作重定向或 4D 资产生成
- 复现论文实验或在自有数据上训练 R-DMesh 模型

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L16: We present **R-DMesh**: a unified video-guided 4D mesh generation framework that tackles the long-overlooked pose m
> L20: * May 13, 2026: 👋 The checkpoint of **R-DMesh** has been released! Please give it a try!

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/R-DMesh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-18 64 → 2026-10-24 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `22164d8bcc45` · [字段定义](../../DATASET.md)*
