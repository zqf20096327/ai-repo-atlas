# quickpose/quickpose-ios-sdk

⭐ 327 · Swift · Apache-2.0 · 推送 2026-08-26 · [GitHub](https://github.com/quickpose/quickpose-ios-sdk) · [官网](https://docs.quickpose.ai/docs/MobileSDK) · 组织维护

**iOS 姿态估计 SDK：为 App 加入 MediaPipe 人体/手部检测**

面向 iOS 开发者的 Swift SDK，封装 MediaPipe/BlazePose 模型，处理相机视频帧并输出关节点位、姿态叠加图层、关节活动度（ROM）测量、健身动作检测与计数（深蹲、俯卧撑等 20 余种）、手指计数与点赞识别等功能。通过 Swift Package Manager 或 CocoaPods 安装，模块含 Core、MediaPipe（lite/full/heavy 变体）及 Camera/SwiftUI 工具类。需在 dev.quickpose.ai 注册 SDK Key（与 bundle ID 绑定，可能有用量限制），支持 iOS 14.0+ 与 Apple Silicon Mac 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 MediaPipe/BlazePose 的关节点位与全身/局部姿态叠加
- 健康场景的关节活动度（ROM）测量
- 20 余种健身动作检测与计数
- lite/full/heavy 三档模型变体可选

## 适用场景

- 在健身 App 中实现动作计数与姿态反馈
- 在康复或健康 App 中测量关节活动度
- 为视频通话或交互应用叠加人体姿态标记

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: QuickPose provides developer-oriented cutting edge ML features of MediaPipe and BlazePose, with easy integration and
> L22: QuickPose process a video frame and makes it easy for developers to perform complex AI features to the image, such 

## 星数曲线

```mermaid
xychart-beta
    title "quickpose/quickpose-ios-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 326 --> 328
    line [327, 327]
```

2026-10-18 327 → 2026-10-28 327（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `cc9d363cfc5a` · [字段定义](../../DATASET.md)*
