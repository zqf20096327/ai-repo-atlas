# null-void-Q/IOS-ObjectDetection

⭐ 15 · Swift · 推送 2026-01-05 · [GitHub](https://github.com/null-void-Q/IOS-ObjectDetection) · 个人维护

**在 iOS 设备上实时运行 YOLOv7 目标检测的示例应用**

一个 iOS 应用，通过 Core ML 在设备摄像头画面上运行预训练的 YOLOv7 目标检测模型，实时输出边界框与标签。要求 iOS 14+、Xcode 12+ 及带摄像头的实体设备（模拟器不可用），推理全部在本地完成。获取方式为 git clone 源码后在 Xcode 中配置签名与 bundle identifier 构建运行，模型已预先训练并针对 iOS 优化。

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

- 摄像头画面的实时目标检测
- YOLOv7 模型经 Core ML 在设备本地推理
- 输出边界框与标签

## 适用场景

- 在 iPhone 上体验本地实时目标检测
- 学习 Core ML 集成 YOLOv7 的示例工程

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: iOS app that runs YOLOv7 object detection model on device camera feed.
> L20: - YOLOv7 model via Core ML

## 星数曲线

```mermaid
xychart-beta
    title "null-void-Q/IOS-ObjectDetection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7466c3be975b` · [字段定义](../../DATASET.md)*
