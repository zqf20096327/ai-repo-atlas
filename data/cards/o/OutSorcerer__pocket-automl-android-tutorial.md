# OutSorcerer/pocket-automl-android-tutorial

⭐ 27 · Kotlin · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/OutSorcerer/pocket-automl-android-tutorial) · 个人维护 · 中文 README

**教程：用 Pocket AutoML 训练图像分类模型并构建 Android 应用**

分步教程，指导用户在 Android 应用中运行深度学习图像分类模型：先用 Pocket AutoML 手机应用采集图像、训练模型并导出 LiteRT（原 TensorFlow Lite）.tflite 格式；再克隆本仓库示例源码，在 Android Studio 中构建并安装到设备或模拟器，从后置摄像头持续分类画面。示例现为 Kotlin 编写，使用 LiteRT CompiledModel API 推理，GPU 上强制 FP32 精度，类别标签从模型元数据读取。面向想制作自定义图像分类 App 的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖训练→导出 tflite→Android 构建→替换自定义模型的完整流程
- 示例基于 Google AI Edge LiteRT 图像分类示例，Kotlin + CameraX
- GPU 推理强制 FP32 精度以避免 EfficientNet 模型 NaN 输出
- 类别标签与输入归一化参数从 tflite 元数据直接读取

## 适用场景

- 训练自己的图像分类模型并做成 Android 应用
- 学习 LiteRT 在 Android 上的模型集成方式
- 做分拣、手势控制等端侧视觉识别小应用

## 场景标签

`教程课程` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L1: # Pocket AutoML: Tutorial for Creating an Android App for Image Classification with Deep Learning
> L11: This document will walk you through the steps for creating your Android app that runs a deep learning image classif
> L13: This tutorial is based on the Google AI Edge LiteRT image classification Android example.

## 星数曲线

```mermaid
xychart-beta
    title "OutSorcerer/pocket-automl-android-tutorial 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `31611022cce1` · [字段定义](../../DATASET.md)*
