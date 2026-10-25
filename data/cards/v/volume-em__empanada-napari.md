# volume-em/empanada-napari

⭐ 38 · Python · BSD-3-Clause · 推送 2026-10-08 · [GitHub](https://github.com/volume-em/empanada-napari) · [官网](https://empanada.readthedocs.io/en/latest/empanada-napari.html) · 组织维护

**napari 插件：在电子显微镜图像上运行 2D/3D 全景分割模型**

empanada-napari 是一个 napari 插件，用于在 2D 与 3D 电子显微镜细胞图像上运行基于深度学习的全景分割（panoptic segmentation）模型。内置 MitoNet 线粒体实例分割模型，1.2 版新增 NucleoNet 细胞核与 DropNet 脂滴分割基础模型，并提供切片/合并、标签形态学操作、标签计数过滤、训练样本导出等模块。依赖 Python 3.10-3.13 与 napari，基于 torch 运行模型，GPU 可选（插件附 CPU 优化版本），通过 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2D 与 3D 电子显微镜图像的全景分割推理
- 内置 MitoNet/NucleoNet/DropNet 基础模型，附 CPU 优化版本
- 切片/合并、标签形态学与过滤、训练 patch 导出等辅助模块
- 支持 GPU 加速（Windows/Linux，基于 torch）

## 适用场景

- 在 napari 中对电镜图像做线粒体/细胞核/脂滴实例分割
- 对大体积电镜数据切片后推理并合并结果
- 导出配对的灰度与标签 patch 用于微调训练

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L29: empanada is a tool for deep learning-based panoptic segmentation of 2D and 3D electron microscopy images of cells.
> L30: This plugin allows the running of panoptic segmentation models trained in empanada within napari.

## 星数曲线

```mermaid
xychart-beta
    title "volume-em/empanada-napari 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `28918a308e2e` · [字段定义](../../DATASET.md)*
