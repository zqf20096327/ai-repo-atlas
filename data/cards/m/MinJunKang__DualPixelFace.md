# MinJunKang/DualPixelFace

⭐ 35 · Python · MIT · 推送 2026-03-06 · [GitHub](https://github.com/MinJunKang/DualPixelFace) · 组织维护

**ECCV22 论文官方实现：双像素相机人脸深度与法向估计**

论文 Facial Depth and Normal Estimation using Single Dual-Pixel Camera（ECCV 2022）的官方 PyTorch 实现：基于双像素传感器数据训练 StereoDPNet 模型，输出人脸深度与法向估计；同时发布约 481G 的人脸双像素基准数据集，需签署许可协议并邮件申请获取。支持 PSMNet、DPNet、StereoNet、BTS 等多个对比模型在同一基准上训练与评测，通过 JSON 配置切换数据集与模型。环境要求 Ubuntu 18.04 + CUDA 10.1/10.2，提供 Conda 与 Docker 两种环境搭建方式；Demo 页面标注待更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- StereoDPNet 模型：双像素输入的人脸深度与法向估计
- 约 481G 的人脸双像素基准数据集（邮件签署许可后获取）
- 统一框架下支持 6 种模型（PSMNet/DPNet/StereoNet/BTS 等）训练与评测
- 提供 Conda 与 Docker 两种环境配置方式

## 适用场景

- 在人脸双像素基准上复现论文或训练对比模型
- 做双像素深度估计相关研究时获取基准数据集
- 基于模板添加自定义模型与数据集进行实验

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: This is an official implementation of the paper,
> L4: > Facial Depth and Normal Estimation using Single Dual-Pixel Camera
> L64: (6) StereoDPNet **(Ours)** Code Pretrained

## 星数曲线

```mermaid
xychart-beta
    title "MinJunKang/DualPixelFace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `08c1ed39489a` · [字段定义](../../DATASET.md)*
