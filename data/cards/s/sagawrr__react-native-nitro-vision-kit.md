# sagawrr/react-native-nitro-vision-kit

⭐ 58 · Kotlin · MIT · 推送 2026-10-21 · [GitHub](https://github.com/sagawrr/react-native-nitro-vision-kit) · 个人维护

**React Native 端侧视觉库：主体抠图、图像标签与 OCR**

基于 Nitro Modules 的 React Native 原生模块，封装 Apple Vision（iOS）与 Google ML Kit（Android），提供 removeBackground 主体抠图（导出 PNG/JPEG/掩码）、classifyImage 离线图像标签、readText OCR（Android 支持 Latin/CJK/天城文，iOS 需 18+）及单次解码的 analyzeImage 组合调用。结果以 HybridObject 保留在原生侧，导出后需调 dispose()。要求 React Native 0.75+ 与新架构；Android 部分功能首次使用需在线下载 Play Services 模型。

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

- iOS 用 Vision、Android 用 ML Kit 的端侧抠图/标签/OCR 三合一 API
- analyzeImage 一次解码同时执行抠图、分类与 OCR
- 结果保留原生侧，支持导出文件、ArrayBuffer 与掩码缓冲
- 能力探测接口（capabilities）报告功能可用性与不可用原因

## 适用场景

- 在 React Native 应用中移除图片背景并导出主体
- 对本地图片做离线标签分类
- 在移动端读取图片中的文字（含中日韩文）

## 场景标签

`图像视频处理` `目标检测` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L7:  Cutouts · Labels · OCR — Vision on iOS,
> L8:  ML Kit on Android, built with
> L13:  <code>removeBackground</code>

## 星数曲线

```mermaid
xychart-beta
    title "sagawrr/react-native-nitro-vision-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-24 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `65fe4dae519f` · [字段定义](../../DATASET.md)*
