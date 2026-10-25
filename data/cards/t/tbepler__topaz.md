# tbepler/topaz

⭐ 222 · Jupyter Notebook · GPL-3.0 · 推送 2026-09-17 · [GitHub](https://github.com/tbepler/topaz) · 组织维护

**冷冻电镜图像的 CNN 粒子挑选与微图降噪流水线**

面向冷冻电镜（cryo-EM）数据处理的开源 Python 流水线：用卷积神经网络从正样本-无标注样本（PU）训练中挑选显微图像中的粒子，提供图像降采样/归一化预处理、模型训练、分割与粒子提取等子命令，附 GUI 与 Jupyter 教程；另含基于深度去噪模型的微图与断层图降噪（含 3D）。提供预训练挑选与降噪模型，3D 粒子挑选在开发分支。通过 conda、pip、Docker、Singularity 或源码安装，GPU 加速需 NVIDIA CUDA 显卡。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 正样本-无标注（PU）训练的 CNN 粒子挑选流水线
- topaz denoise/denoise3d 深度去噪（含 3D 与预训练模型）
- 提供预训练粒子挑选模型与 GUI
- 提供 conda/pip/Docker/Singularity 多种安装途径

## 适用场景

- 在 cryo-EM 微图中自动挑选蛋白质颗粒坐标
- 对噪声严重的微图或断层图做深度学习降噪
- 用少量已标注粒子训练定制挑选模型并交叉验证

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: A pipeline for particle detection in cryo-electron microscopy images using convolutional neural networks trained fro
> L42: - The Topaz publication is out here

## 星数曲线

```mermaid
xychart-beta
    title "tbepler/topaz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 220 --> 222
    line [221, 221]
```

2026-10-18 221 → 2026-10-25 221（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cdfda1fa5655` · [字段定义](../../DATASET.md)*
