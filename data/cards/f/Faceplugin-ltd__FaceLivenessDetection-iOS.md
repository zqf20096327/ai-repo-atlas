# Faceplugin-ltd/FaceLivenessDetection-iOS

⭐ 19 · Swift · 推送 2026-09-30 · [GitHub](https://github.com/Faceplugin-ltd/FaceLivenessDetection-iOS) · [官网](https://faceplugin.com/face-liveness-detection/) · 组织维护

**iOS 人脸活体检测 SDK 演示应用：设备端反欺诈识别攻击**

FacePlugin 面向 iOS 的人脸活体检测 SDK 的官方演示工程：纯设备端（on-premise）被动活体检测，识别打印照片、视频回放、3D 面具与 deepfake 类攻击，自称 iBeta level 2 级别，全部处理留在 iPhone 上，生物特征数据不出设备。运行时框架（facelivenessdk/FaceLivenessEngine/onnxruntime）因体积过大从 Google Drive 以 zip 下载，解压到仓库根目录后用 Xcode 在实体 iPhone 上运行。许可离线且绑定 bundle id，demo 自带 key，自有 app 需联系获取。不支持模拟器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端被动活体检测（照片/视频回放/3D 面具/deepfake 攻击）
- 生物特征数据不出设备，无需云端
- demo 自带绑定 com.faceplugin.facelivenessdk 的离线许可
- 提供自有 app 集成步骤（Embed & Sign 三框架 + activate 调用）

## 适用场景

- 在 KYC / 远程身份验证流程中集成人脸活体检测
- 评估 FacePlugin SDK 的检测效果与 API 形态
- iOS 实体机上运行反欺诈相机演示

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L26: FacePlugin **Face Liveness Detection SDK for iOS** is a fully on-device anti-spoofing engine for KYC and remote ide
> L61: |1|Xcode 15+ and a **physical iPhone**|

## 星数曲线

```mermaid
xychart-beta
    title "Faceplugin-ltd/FaceLivenessDetection-iOS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `41e58e58fbc6` · [字段定义](../../DATASET.md)*
