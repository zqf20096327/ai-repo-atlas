# Netesh5/image_background_remover

⭐ 29 · Shell · BSD-3-Clause · 推送 2026-09-13 · [GitHub](https://github.com/Netesh5/image_background_remover) · [官网](https://pub.dev/packages/image_background_remover) · 个人维护

**Flutter 图像抠图包：内置 ONNX 模型离线去除图片背景**

面向 Flutter 开发者的 pub 包，通过 ONNX Runtime 运行内置分割模型，在移动端离线去除图片背景。提供 initializeOrt/removeBg/addBackground 三个核心 API，支持阈值调节、平滑掩码与边缘增强，并可在抠图后填充自定义背景色。v2.0.0 迁移到 flutter_onnxruntime，支持 Android 16KB 页大小与 iOS 16+；需配置 Podfile 与 ProGuard 规则，模型打包使应用体积约增 30MB，且不能与 Dart isolates 配合使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完全离线运行，无需外部 API 依赖
- removeBg 支持阈值、平滑掩码与边缘增强参数
- 抠图后可用 addBackground 填充自定义背景色
- v2.0.0 支持 Android 16KB 页大小与 iOS 16+

## 适用场景

- 在我的 Flutter 应用里给用户照片做离线抠图
- 电商/证件类应用中批量替换图片背景色
- 无网络环境下处理图像且不依赖云端 API

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: A Flutter package that removes the background from images using an ONNX model. The package provides a seamless way t
> L36: - Remove the background from images with high accuracy.

## 星数曲线

```mermaid
xychart-beta
    title "Netesh5/image_background_remover 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4d642d3f6a35` · [字段定义](../../DATASET.md)*
