# rui-qian/BADet

⭐ 28 · Python · 推送 2026-02-05 · [GitHub](https://github.com/rui-qian/BADet) · [官网](https://github.com/rui-qian/BADet) · 个人维护

**基于点云的边界感知 3D 目标检测研究代码（Pattern Recognition 2022）**

BADet 是论文配套的 3D 目标检测 PyTorch 实现，面向自动驾驶点云检测研究者：将各 proposal 表示为图节点、在截断阈值内构建局部邻域图以利用边界相关性，并用轻量 Region Feature Aggregation Module 融合 voxel/pixel/point 级特征。在 KITTI 与 nuScenes 上验证，2021 年 4 月居 KITTI BEV 检测榜第一（ Moderate Car ），运行速度 7.1 FPS。代码基于 mmdetection 开发，需编译 C++/CUDA 模块并配置 CUDA 环境变量，提供 KITTI 数据准备脚本、预训练模型（Hugging Face/iCloud）与训练/评测命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- proposal 邻域图构建显式利用边界相关性
- Region Feature Aggregation Module 融合 voxel/pixel/point 级特征
- 提供 KITTI 预训练模型与训练/评测脚本
- 2021-04 居 KITTI BEV 检测榜第一（Moderate Car），运行 7.1 FPS

## 适用场景

- 在 KITTI/nuScenes 上复现论文的 3D 检测结果
- 基于预训练模型做点云目标检测评测
- 借鉴边界感知机制开发两阶段 3D 检测器

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L44: In this paper, we propose BADet for 3D object detection from point clouds. Specifically, instead
> L50: We validate BADet both on widely used KITTI Dataset and highly challenging nuScenes Dataset.

## 星数曲线

```mermaid
xychart-beta
    title "rui-qian/BADet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5b657cfe0953` · [字段定义](../../DATASET.md)*
