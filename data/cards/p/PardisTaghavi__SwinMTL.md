# PardisTaghavi/SwinMTL

⭐ 50 · Jupyter Notebook · GPL-3.0 · 推送 2026-09-13 · [GitHub](https://github.com/PardisTaghavi/SwinMTL) · [官网](https://pardistaghavi.github.io/#swinmtl) · 组织维护

**单目图像同时做深度估计与语义分割的多任务学习框架**

IROS 2024 论文的官方代码库：基于 Swin Transformer 的共享架构多任务学习框架，从单目相机图像同时输出深度估计与语义分割结果。提供预训练模型下载、testLive.ipynb 测试入口，并支持 ROS 环境下用 roslaunch 部署，在 KITTI 上展示零样本结果与 3D 建图结果。安装方式为 git clone 源码加 conda 环境配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单目图像同时输出深度估计与语义分割
- 基于 Swin Transformer 的共享架构
- 提供 ROS 启动方式（roslaunch）
- 提供预训练模型与 KITTI 零样本评测结果

## 适用场景

- 机器人/自动驾驶中从单目相机获取深度与语义信息
- 在 ROS 系统中部署多任务视觉模型
- 复现 IROS24 论文实验结果

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: A multi-task learning framework designed for simultaneous depth estimation and semantic segmentation using the Swin 
> L47: ### ROS Launch

## 星数曲线

```mermaid
xychart-beta
    title "PardisTaghavi/SwinMTL 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 48 --> 51
    line [49, 50, 50]
```

2026-10-18 49 → 2026-10-31 50（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5cba13568730` · [字段定义](../../DATASET.md)*
