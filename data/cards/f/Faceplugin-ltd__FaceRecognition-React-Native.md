# Faceplugin-ltd/FaceRecognition-React-Native

⭐ 22 · TypeScript · MIT · 推送 2026-09-28 · [GitHub](https://github.com/Faceplugin-ltd/FaceRecognition-React-Native) · [官网](https://faceplugin.com/face-recognition-sdk/) · 组织维护

**面向 React Native 的端上人脸识别 SDK（1:N 识别与活体检测）**

FacePlugin 公司的 React Native 人脸识别 SDK，封装 Android/iOS 原生引擎，以 npm 包 face-recognition-sdk 分发。功能覆盖人脸检测、14 点关键点、模板提取与 1:1/1:N 比对、摄像头实时 1:N 识别（VideoWorker）、2D 活体/防欺诈、姿态/表情/年龄/性别等属性。全部处理在设备端完成，不向云端发送生物识别数据。原生运行时（AAR 与 iOS 框架，含 onnxruntime）体积过大不在 GitHub，需从 Google Drive 下载后手动放入指定路径；许可证离线且绑定 applicationId/bundle id，示例 App 自带 key，自有 App 需联系厂商获取。不支持 Expo Go，建议真机运行。

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

- 端上 1:N 实时识别（VideoWorker）与 2D 活体/防欺诈
- 人脸检测、关键点、年龄/性别/情绪等属性分析
- 所有处理在设备本地，生物识别数据不回传云端
- TypeScript 单一 API 覆盖 Android 与 iOS

## 适用场景

- 移动端 KYC/eKYC 与用户注册流程中做人脸注册与活体验证
- 在 React Native 应用中实现 1:N 现场人脸识别
- 分析照片中人脸的关键点、姿态、质量与属性

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L34: FacePlugin **Face Recognition SDK for React Native** is a fully on-device biometric library for Android and iOS. En
> L54: |**Identify**|Live 1:N camera match (VideoWorker) with 2D liveness / anti-spoofing|
> L36: All processing stays on the device. **No** biometric data is sent to FacePlugin cloud — built for KYC, eKYC, and cr

## 星数曲线

```mermaid
xychart-beta
    title "Faceplugin-ltd/FaceRecognition-React-Native 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-27"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-27 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b428b4b4c504` · [字段定义](../../DATASET.md)*
