# john-rocky/SemanticImage

⭐ 165 · Swift · MIT · 推送 2026-05-28 · [GitHub](https://github.com/john-rocky/SemanticImage) · [官网](https://john-rocky.github.io/) · 个人维护

**iOS 开发者用的 Swift 图像/视频语义滤镜库**

基于 Apple Vision/CoreML 框架的 Swift Package，为 iOS 开发者提供一组图像与视频处理 API：包括人物遮罩生成、人物与显著物体背景替换、人物背景模糊、人脸/人体/猫狗区域裁剪、文档矫正，以及对视频应用 CIFilter、虚拟背景与逐帧自定义处理。通过 Swift Package Manager 集成，或直接拖入 SemanticImage.swift 源文件，要求 iOS 14 及以上。作者为日本自由职业 iOS 程序员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人物遮罩、背景替换与背景模糊等语义分割滤镜
- 人脸/人体/猫狗矩形检测与裁剪，支持单人或多人
- 视频处理：应用 CIFilter、人物/显著物体虚拟背景、逐帧自定义处理

## 适用场景

- 在 iOS 应用中实现人像背景虚化或虚拟背景
- 自动裁剪照片中的人脸、人体或宠物区域
- 为视频批量应用滤镜或自定义逐帧处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: A collection of easy-to-use image / video filters.
> L31: let maskImage:UIImage? = semanticImage.personMaskImage(uiImage: yourUIImage)

## 星数曲线

```mermaid
xychart-beta
    title "john-rocky/SemanticImage 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 164 --> 167
    line [166, 165, 165]
```

2026-10-18 166 → 2026-10-27 165（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2d92b4956b16` · [字段定义](../../DATASET.md)*
