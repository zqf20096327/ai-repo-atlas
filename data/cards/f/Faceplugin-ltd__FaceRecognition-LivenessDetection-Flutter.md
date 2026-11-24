# Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter

⭐ 25 · Dart · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Faceplugin-ltd/FaceRecognition-LivenessDetection-Flutter) · [官网](https://faceplugin.com/face-recognition-sdk/) · 组织维护

**Flutter 开发者的端侧人脸识别与活体检测 SDK**

FacePlugin 的 Flutter 插件，在设备本地运行人脸检测、被动活体（防伪）、模板提取、1:1 相似度与实时 1:N 识别，数据不发送到 FacePlugin 服务器。仓库包含插件本体、Android/iOS 原生桥接和由同一插件构建的示例应用（五个标签页）。原生二进制因体积原因从 GitHub release 页下载，Demo 内置许可证密钥，自有应用需联系获取绑定 applicationId 的离线许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端侧运行人脸检测、被动活体、模板提取与 1:N 识别
- Android/iOS 使用相同引擎二进制，两平台得分一致
- 许可证离线绑定 applicationId/Bundle ID，示例应用自带演示密钥
- 阈值（匹配、活体、姿态、闭眼）由 Dart 侧参数传入可调

## 适用场景

- 在银行类应用中做端侧人脸活体核验
- 门禁/身份核验应用做人脸注册与 1:N 比对
- 从照片提取人脸姿态、表情、年龄、性别等属性

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L22: FacePlugin **Face Recognition + Liveness Detection for Flutter** runs face recognition and passive liveness entirel
> L32: |Face detection (bounding box, landmarks, pose, attributes)|`faceDetection`|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `06ec8256ac40` · [字段定义](../../DATASET.md)*
