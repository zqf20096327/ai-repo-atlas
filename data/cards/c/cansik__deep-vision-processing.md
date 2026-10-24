# cansik/deep-vision-processing

⭐ 108 · Java · 推送 2026-01-09 · [GitHub](https://github.com/cansik/deep-vision-processing) · 个人维护

**为 Processing 提供深度计算机视觉推理的 Java 库**

面向 Processing 创意编程框架的机器视觉库：提供 DeepVision 类下载预训练模型并创建网络，通过 run() 方法对 PImage 输入产出检测结果。内置 YOLOv3/v4/v5、SSDMobileNetV2、人脸/手部检测、姿态估计、MidasNet 深度估计、风格迁移、超分辨率等网络，并支持网络流水线组合。推理后端支持 CPU/OpenCL/CUDA（CUDA 需下载捆绑版，Windows/Linux），仅做推理不支持训练。API 处于开发中可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 30+ 种预训练网络：目标检测、分割、分类、关键点、深度估计、风格迁移
- CUDA/OpenCL 推理后端支持（0.6.0 起），无 CUDA 硬件时回退 CPU
- 网络流水线：检测结果可级联分类器
- 预训练权重自动下载，可存全局库目录或 sketch 目录

## 适用场景

- 在 Processing 草图中直接运行 YOLO 目标检测
- 摄像头实时人脸/手部检测用于交互艺术项目
- 单目深度估计、风格迁移等效果在创意编码中使用

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L4: The idea behind this library is to provide a simple way to use (inference) machine learning algorithms for computer 
> L50: Each network has a `run()` method, which takes an image as a parameter and outputs a result. You can just throw in 
> L54: ResultList<ObjectDetectionResult> detections = network.run(myImg);

## 星数曲线

```mermaid
xychart-beta
    title "cansik/deep-vision-processing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-24 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `603420b99ec1` · [字段定义](../../DATASET.md)*
