# tobecwb/facial-features-yolo8x-seg

⭐ 15 · 推送 2026-10-09 · [GitHub](https://github.com/tobecwb/facial-features-yolo8x-seg) · 个人维护

**女性面部五官分割模型：为修图生成眼睛/眉毛/鼻子/嘴部掩码**

基于 YOLOv8 的图像分割模型，将面部划分为 eye、eyebrow、nose、mouth 四类并生成掩码，专门用于为 stable-diffusion-face-dataset 中图像的手动编辑提供遮罩。训练数据仅使用 100 张 1024px 女性人脸（来自作者自建的正则化图像仓库），标注经 Roboflow 完成，训练通过 Ultralytics HUB 进行。README 声明初步测试对男性人脸也有效果，但建议补充男性人脸训练数据。仓库以模型与示例为主，未给出安装或推理命令。

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

- eye/eyebrow/nose/mouth 四类面部特征分割
- 面向图像手动编辑的掩码生成用途
- 训练数据为 100 张 1024px 女性人脸，标注经 Roboflow

## 适用场景

- 为修图工作流自动生成面部五官掩码
- 配合 Stable Diffusion 人脸数据集做编辑前预处理

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L1: ## YOLOx8 model segmentation for face features
> L12: Segmentation model specially made to generate image masks for manual editing of images from https://github.com/tobe

## 星数曲线

```mermaid
xychart-beta
    title "tobecwb/facial-features-yolo8x-seg 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `2156dd079f57` · [字段定义](../../DATASET.md)*
