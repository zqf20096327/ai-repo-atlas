# LiuXinchen1997/PCVisAPP

⭐ 20 · CSS · MIT · 推送 2026-07-08 · [GitHub](https://github.com/LiuXinchen1997/PCVisAPP) · 个人维护 · 中文 README

**3D 点云上采样与语义分割的 Web 演示与管理系统**

面向 3D 计算机视觉方向学生与研究者的毕业设计演示系统：基于 Django 后端与 jQuery/Three.js 前端，提供点云上采样、场景上采样、分割数据集可视化、场景分割四类算法演示，附模型上传、目录管理、回收站等轻量文件管理功能，以及可调参数的网页端 3D 渲染控件。上采样通过 TensorFlow 神经网络实现（参考 PU-GAN），无 GPU 时可跳过算子编译并注释相关调用。需以 conda 环境从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 点云上采样/场景上采样/分割数据集/场景分割四类算法演示，对比原始、生成与真值模型
- 网页端 3D 渲染控件，渲染参数可调（OBJ/PLY）
- 点云模型文件管理：目录增删改、上传下载移动、回收站
- 上采样算子可替换为自定义点云处理算法

## 适用场景

- 毕业设计或科研成果需要一个可视化展示系统
- 管理并在线预览 3D 点云模型文件
- 对比点云上采样/分割算法的输入输出效果

## 场景标签

`科研工具` `目标检测` `图像视频处理` · 领域:学习与行业

## 证据(README 行号)

> L7: PCVisAPP is a demonstration system for graduation-design research work, focusing on 3D point cloud upsampling and se
> L48:  The purpose of `upsample_points` is to call a TensorFlow-based neural network to upsample 3D point cloud models. Y

## 星数曲线

```mermaid
xychart-beta
    title "LiuXinchen1997/PCVisAPP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `d2af0b26c662` · [字段定义](../../DATASET.md)*
