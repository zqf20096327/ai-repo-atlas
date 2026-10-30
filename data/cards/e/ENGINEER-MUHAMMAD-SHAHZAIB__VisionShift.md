# ENGINEER-MUHAMMAD-SHAHZAIB/VisionShift

⭐ 24 · Python · AGPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/ENGINEER-MUHAMMAD-SHAHZAIB/VisionShift) · 个人维护

**实时人脸替换与视频 deepfake 摄像头工具**

基于单张图片即可实时换脸/生成视频 deepfake 的桌面应用，支持摄像头实时模式、嘴部遮罩保留原口型、多人脸映射、电影模式替换影片人脸，可配合 OBS 用于直播或视频通话。底层使用 GFPGANv1.4 与 inswapper_128_fp16.onnx 模型，支持 CUDA 与 CoreML 加速。提供 Windows/Mac 预编译版供非技术用户，也可从源码手动安装（Python 3.10、ffmpeg 等）。内置不当媒体检查，要求用户获得人脸使用授权。本仓库为 hacksider/Deep-Live-Cam 的改名复刻。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单张图片一键实时换脸（摄像头模式）
- 嘴部遮罩、多人脸映射、电影模式等功能
- GFPGANv1.4 + inswapper_128_fp16.onnx 模型驱动
- 提供 Windows/Mac 预编译版，支持 CUDA/CoreML 加速

## 适用场景

- 直播或视频通话中实时替换人脸
- 实时替换影片中的角色人脸
- 制作换脸梗图或动画自定义角色

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3:  **VisionShift** enables seamless real-time face swapping and video deepfakes with just a single image and a single 
> L81:  - GFPGANv1.4
> L82:  - inswapper_128_fp16.onnx

## 星数曲线

```mermaid
xychart-beta
    title "ENGINEER-MUHAMMAD-SHAHZAIB/VisionShift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `7d5c29acb8ff` · [字段定义](../../DATASET.md)*
