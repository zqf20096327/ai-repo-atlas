# astra-vision/SceneRF

⭐ 381 · Python · Apache-2.0 · 推送 2026-03-25 · [GitHub](https://github.com/astra-vision/SceneRF) · [官网](https://astra-vision.github.io/SceneRF/)

**自监督单目 3D 场景重建的官方 PyTorch 实现**

ICCV 2023 论文 SceneRF 的官方代码：用辐射场（NeRF）从单张图像做自监督的单目 3D 场景重建，支持新视角深度/视图合成与 TSDF 场景重建。基于 PyTorch 1.7.1 + CUDA 10.2 + Python 3.7，提供 KITTI 与 Bundlefusion 两个数据集的训练、评估、预训练模型下载与网格提取脚本。训练配置为 4 块 v100-32g GPU，提供 Conda 与 Docker 两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自监督单目 3D 场景重建（ICCV 2023 官方实现）
- 新视角深度/视图合成与 TSDF 场景重建评估流程
- KITTI 与 Bundlefusion 双数据集训练/评估脚本
- 提供预训练模型与 open3d 网格可视化

## 适用场景

- 复现论文的单目 3D 场景重建实验
- 在 KITTI/Bundlefusion 上训练与评估重建模型
- 从模型输出提取网格并可视化

## 场景标签

 · 领域:计算机视觉/3D 重建

## 证据(README 行号)

> L1: # SceneRF: Self-Supervised Monocular 3D Scene Reconstruction with Radiance Fields
> L47: 2. This code was implemented with python 3.7, pytorch 1.7.1 and CUDA 10.2. Please install PyTorch:
> L128: 3. Train scenerf using 4 v100-32g GPUs with batch_size of 4 (1 item per GPU):

## 星数曲线

```mermaid
xychart-beta
    title "astra-vision/SceneRF 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 380 --> 382
    line [381, 381]
```

2026-10-18 381 → 2026-10-29 381（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `0b6e4ac5e16d` · [字段定义](../../DATASET.md)*
