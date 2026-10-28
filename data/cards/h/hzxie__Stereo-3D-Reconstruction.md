# hzxie/Stereo-3D-Reconstruction

⭐ 21 · 推送 2026-06-15 · [GitHub](https://github.com/hzxie/Stereo-3D-Reconstruction) · [官网](https://haozhexie.com/projects/stereo-3d-reconstruction) · 个人维护

**科研代码：双目立体图像重建物体 3D 体素/点云（Neurocomputing 2021 论文）**

论文 "Toward 3D Object Reconstruction from Stereo Images"（Neurocomputing 2021）的官方源码实现，提供 Stereo2Voxel（体素重建）与 Stereo2Point（点云重建）两个分支。实验使用 StereoShapeNet 数据集，并提供在该数据集上训练的预训练模型（309/356 MB）。安装方式为 git clone 源码并用 pip 安装依赖，Stereo2Point 分支需额外编译 chamfer_dist CUDA 扩展；训练/测试通过修改 config.py 中的数据集路径后运行 runner.py 完成。代码以 MIT 许可开源，面向计算机视觉研究者复现与实验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双目立体图像到体素与点云两种 3D 重建实现
- 提供 StereoShapeNet 上的预训练模型（Stereo2Voxel/Stereo2Point）
- 基于 PyTorch，含训练与测试入口 runner.py

## 适用场景

- 复现论文中的立体图像 3D 重建结果
- 在 StereoShapeNet 数据集上训练或微调重建模型
- 以预训练模型直接测试生成立体图像的体素/点云

## 场景标签

`科研工具` `图像视频处理` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository contains the source code for the paper Toward 3D Object Reconstruction from Stereo Images.
> L12: @article{xie2021towards,

## 星数曲线

```mermaid
xychart-beta
    title "hzxie/Stereo-3D-Reconstruction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d76562932e49` · [字段定义](../../DATASET.md)*
