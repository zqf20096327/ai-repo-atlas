# foo123/FILTER.js

⭐ 400 · JavaScript · 推送 2026-09-21 · [GitHub](https://github.com/foo123/FILTER.js) · [官网](https://foo123.github.io/examples/filter/) · 个人维护

**纯 JavaScript 图像/视频处理与计算机视觉库（浏览器/Node.js）**

面向 Web 与 Node.js 开发者的图像/视频处理库：以 Image 类与 Color 工具为基础，提供 14 种通用 Filter 类型及多种实现滤波器（灰度、阈值、高斯模糊、浮雕等），支持 CPU（Web Workers/进程）与 GPU（WebGL/GLSL）并行处理、WASM 版本滤波器及 CPU/GPU 混合使用，二者在浏览器和 Node.js 下均可用。滤波器可独立选取并自定义构建。部分代码改编自 Image Processing Library in Java、OpenCV 等开源库。README 未给出安装命令，版本 1.14.0 标注开发中。

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

- 14 种通用 Filter 类型加插件与额外滤波器
- CPU/GPU 并行处理透明支持浏览器与 Node.js
- WASM 与 GLSL 版本的滤波器实现
- 滤波器可按需混搭生成自定义构建

## 适用场景

- 在浏览器或 Node.js 中对图像/视频做滤波与特征处理
- 利用 WebGL/Web Workers 并行加速实时视觉处理
- 按需裁剪滤波器子集构建轻量库版本

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **A pure JavaScript Library for Image/Video Processing, Filtering and Computer Vision**
> L38: The framework defines an `Image` class, which represents a proxy for an Image, a number of utilities like `Color` c

## 星数曲线

```mermaid
xychart-beta
    title "foo123/FILTER.js 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 399 --> 401
    line [400, 400]
```

2026-10-18 400 → 2026-10-23 400（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fc2f335bb79d` · [字段定义](../../DATASET.md)*
