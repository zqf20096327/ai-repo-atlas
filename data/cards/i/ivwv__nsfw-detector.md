# ivwv/nsfw-detector

⭐ 32 · Vue · 推送 2026-05-13 · [GitHub](https://github.com/ivwv/nsfw-detector) · [官网](https://nsfw-detector.netlify.app/) · 个人维护 · 中文 README

**浏览器内本地运行的图片/视频 NSFW 内容检测 Web 应用**

基于 Vue 3 与 Hugging Face Transformers（Transformers.js）构建的 NSFW 内容检测 Web 应用：逐帧分析视频并生成时间线图表，支持单张图像检测与置信度展示，提供拖拽上传、可调帧间隔、隐私模糊控制、进度跟踪与可取消分析。推理通过设备自动检测在 CPU 或 WebGPU 上运行，处理过程在浏览器本地完成。检测结果的可视化基于 ECharts。面向需要本地检测图像/视频内容的前端用户，从克隆仓库源码运行。

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

- 视频逐帧实时 NSFW 检测，帧间隔可调并生成时间线图表
- 单张图像检测，输出置信度与饼图可视化
- 自动设备检测（CPU/WebGPU），处理全程本地进行
- 视频预览隐私模糊控制与可取消的分析过程

## 适用场景

- 在不上传文件的前提下本地检测图片或视频是否含 NSFW 内容
- 逐帧定位视频中 NSFW 片段出现的时间点
- 对含敏感内容的视频预览做模糊处理后再查看

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: A powerful and user-friendly NSFW (Not Safe For Work) content detection tool built with Vue 3 and Hugging Face Trans
> L15:  - Real-time frame-by-frame NSFW content detection
> L30:  - Automatic device detection (CPU/WebGPU)

## 星数曲线

```mermaid
xychart-beta
    title "ivwv/nsfw-detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `383f3add21b8` · [字段定义](../../DATASET.md)*
