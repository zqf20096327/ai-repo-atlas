# ochornenko/virtual-background-ios

⭐ 21 · Swift · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/ochornenko/virtual-background-ios) · 个人维护

**iOS 实时人像分割虚拟背景示例应用**

基于 Apple Vision 人像分割与 Metal 的 iOS 示例应用：用设备端深度学习模型将摄像头画面中的人物与背景分离，生成软边缘遮罩（matte），再用 Metal compute shader 将人物与自定义背景图像逐像素混合，实现实时虚拟背景替换。相机采集基于 AVFoundation，渲染基于 MetalKit。分割采用 .balanced 质量级别并复用请求以获得时间稳定遮罩。需在物理设备上运行，iOS Simulator 不支持人像分割。

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

- Vision VNGeneratePersonSegmentationRequest 设备端人像分割生成软遮罩
- Metal compute shader 按遮罩逐像素混合人物与虚拟背景，零拷贝共享 GPU 缓冲
- 复用 VNSequenceRequestHandler 保持帧间遮罩时间稳定
- 针对实时视频选择 .balanced 分割质量并在后台队列预热模型

## 适用场景

- 视频会议或直播中替换摄像头背景
- 学习 iOS 上 Vision + Metal 实时视频处理管道的实现
- 参考相机采集、分割与 GPU 混合渲染的集成方式

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L7: This project leverages Apple's Vision person segmentation to replace the background in real-time on iOS devices. Usi
> L36: The `CameraVirtualBackgroundProcessor` class is responsible for processing video frames to apply a virtual backgrou

## 星数曲线

```mermaid
xychart-beta
    title "ochornenko/virtual-background-ios 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-21"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-11-15 21 → 2026-11-21 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `614e59bb538b` · [字段定义](../../DATASET.md)*
