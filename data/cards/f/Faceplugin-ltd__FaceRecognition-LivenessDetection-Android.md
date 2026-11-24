# Faceplugin-ltd/FaceRecognition-LivenessDetection-Android

⭐ 475 · Kotlin · 推送 2026-11-23 · [GitHub](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Android) · [官网](https://faceplugin.com/face-recognition-sdk/) · 组织维护

**安卓端离线人脸识别与活体检测 SDK 及演示应用**

FacePlugin 的 Android 人脸 SDK 仓库，包含引擎二进制（facerecognitionsdk.aar）、两个辅助库模块和演示应用。功能覆盖人脸检测（边界框/关键点/姿态/属性）、被动活体检测、图像质量评估、模板提取与相似度比对、1:N 识别、带查重的注册，以及带椭圆引导的相机采集。全部计算在设备端运行，数据不发送到服务器；引擎通过绑定 applicationId 的离线许可证激活，演示应用自带演示密钥。需要实体手机（模拟器摄像头不可用）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端运行的人脸识别与被动活体检测，数据不出设备
- 1:N 识别与带查重的注册，注册数据存于 SQLite 与应用私有存储
- 可调节的 match/liveness/pose 阈值与 CallReport 调用报告
- 提供 iOS/RN/Flutter/MAUI/Cordova/Capacitor 多平台版本仓库

## 适用场景

- 银行与门禁类应用中的人脸身份核验
- 需要设备端离线运行的 eKYC 身份认证流程
- 在自有 Android 应用中集成注册、识别与活体检查

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L21: FacePlugin **Face Recognition + Liveness Detection for Android** runs face recognition and passive liveness entirel
> L29: |Face detection (bounding box, landmarks, pose, attributes)|`FaceDetector.detect`|
> L30: |passive liveness (anti-spoofing)|`face.liveness` · `FaceLimits.isLive`|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `efe2e1fdadbe` · [字段定义](../../DATASET.md)*
