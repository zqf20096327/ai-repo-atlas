# Faceplugin-ltd/Open-Source-Face-Liveness-Detection-SDK

⭐ 3 · Python · MIT-0 · 推送 2026-11-12 · [GitHub](https://github.com/Faceplugin-ltd/Open-Source-Face-Liveness-Detection-SDK) · [官网](https://faceplugin.com/) · 组织维护

**本地 CPU 活体检测 SDK：区分真脸与打印/翻拍/屏幕攻击**

Faceplugin 开源的 Python 活体检测模型，基于 MobileNetV2 骨干加轻量分类头，对单张图片输出 0–1 欺骗分数并按可调阈值判定 Live/Fake。全部处理本地完成，运行时无需联网或 CUDA，依赖 Python 3.10+ 与两个 Python 依赖。提供 CLI（单图/文件夹批处理）与 LivenessDetector 类 API，支持 BGR NumPy 数组直接传入。注意整图分类，无内置人脸检测步骤，仅支持静态图片格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT-0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MobileNetV2 轻量模型，CPU 实时运行，无 CUDA 依赖
- 100% 本地处理，运行时离线可用
- 单图/文件夹批处理，欺骗分数与可调阈值
- MIT-0 许可，允许商业使用且无需署名

## 适用场景

- 人脸登录与门禁中拦截照片和视频翻拍攻击
- 远程开户 eKYC 流程确认真人在镜头前
- 考勤与访客签到系统加入活体校验

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L16: The Open Source Face Liveness Detection SDK tells a **live face** apart from a **spoofed face** (a printed photo, a
> L20: - 🔒 **100% On-Premise**: All processing happens locally, so no data leaves your device


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `39e18e5077c5` · [字段定义](../../DATASET.md)*
