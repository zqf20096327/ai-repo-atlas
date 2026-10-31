# Tom-Notch/USF

⭐ 15 · Python · BSD-3-Clause · 推送 2026-10-26 · [GitHub](https://github.com/Tom-Notch/USF) · [官网](https://tomnotch.com/USF/) · 组织维护

**CVPR 2026 球面图像旋转等变视觉前端框架（USF）**

CMU 机器人研究所发布的统一球面前端（USF）研究代码：面向任意相机的无畸变、镜头无关的旋转等变视觉框架，用于现代感知任务。提供 Conda/uv 本地环境搭建与 Docker/Singularity 容器支持，通过 Hydra 配置训练 MNIST 分类、目标检测与语义分割任务；另含球面图像 Open3D 可视化与镜头法向图生成等工具，数据集需自行下载并软链接至 data/ 目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 旋转等变的球面图像表示学习，镜头无关
- 支持 MNIST 分类、目标检测、语义分割训练任务
- 球面图像交互式 Open3D 可视化与镜头法向图生成命令
- 提供 Conda 环境文件、uv 安装与 Docker/Singularity 脚本

## 适用场景

- 复现论文中的球面图像感知实验
- 在全景/鱼眼等球形数据上训练检测与分割模型
- 生成相机镜头法向图并可视化球面图像

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L19: Unified Spherical Frontend (USF) is a distortion-free lens-agnostic rotation-equivariant vision framework for moder
> L96: - To train MNIST classification model, just do this in your shell
> L105: - To train object detection
> L115: - To train semantic segmentation

## 星数曲线

```mermaid
xychart-beta
    title "Tom-Notch/USF 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `31bf73bd246a` · [字段定义](../../DATASET.md)*
