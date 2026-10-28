# Vinsmoke2110/CoreML-Live-Vision-Showcase

⭐ 56 · HTML · 推送 2026-10-27 · [GitHub](https://github.com/Vinsmoke2110/CoreML-Live-Vision-Showcase) · 个人维护

**给 iOS/macOS 开发者的 CoreML+Vision 实时图像识别示例应用**

面向 Swift 开发者的设备端机器学习演示项目，源自慕尼黑 Swift 聚会：用 CoreML 模型与 Vision 框架实现静态图像分类（Caltech-101 数据集、101 类）与实时视频识别（Apple 产品照片、约 30fps）。全部推理在设备本地完成，无外部服务器数据传输。架构分为模型层、Vision 封装层、处理层（帧丢弃、结果缓存、置信度过滤）、SwiftUI 展示层与工具层；支持替换自定义 CoreML 模型，界面支持多语言与 VoiceOver。定位为教学资源与参考实现。

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

- Caltech-101 静态图像分类与实时视频识别双示例
- 全部推理本地运行，无数据外传
- 模块化分层架构（模型/Vision/处理/展示/工具）
- 支持替换自定义 CoreML 模型

## 适用场景

- 学习 CoreML 与 Vision 框架的完整接入流程
- 作为图像识别应用的参考实现进行改造
- 在无相机硬件环境下测试 CoreML 模型效果

## 场景标签

`目标检测` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L6: An innovative demonstration project showcasing the seamless integration of CoreML and Vision frameworks for both sta
> L24: This implementation uses two distinct approaches to demonstrate the versatility of Apple's ML frameworks. The stati
> L50: ### 🖼️ Static Image Classification

## 星数曲线

```mermaid
xychart-beta
    title "Vinsmoke2110/CoreML-Live-Vision-Showcase 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-28 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2894e62a2d65` · [字段定义](../../DATASET.md)*
