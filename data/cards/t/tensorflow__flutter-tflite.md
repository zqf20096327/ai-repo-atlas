# tensorflow/flutter-tflite

⭐ 654 · Dart · Apache-2.0 · 推送 2025-10-28 · [GitHub](https://github.com/tensorflow/flutter-tflite) · 组织维护

**Flutter 的 TensorFlow Lite 推理插件：加载 TFLite 模型执行推理**

TensorFlow 维护的 Flutter 插件，直接绑定 TFLite C API，提供类似 Java/Swift API 的接口加载任意 .tflite 模型并执行单/多输入输出推理；支持 NNAPI、GPU（Android）、Metal/CoreML（iOS）、XNNPack（桌面）加速代理，并提供 IsolateInterpreter 在独立 isolate 中异步推理以免阻塞 UI 线程。Android/iOS 支持动态库下载，macOS/Linux/Windows 需手动编译并添加 TFLite 动态库。项目自述为进行中状态，原 helper 库已弃用并由 flutter-mediapipe 替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 直接绑定 TFLite C API，加载任意 .tflite 模型推理
- 多平台加速代理：NNAPI/GPU/Metal/CoreML/XNNPack
- IsolateInterpreter 异步推理避免阻塞 UI 线程
- 支持 Android/iOS/macOS/Linux/Windows（后三者需手动构建动态库）

## 适用场景

- 在 Flutter 应用中运行 TensorFlow Lite 模型做设备端推理
- 构建跨 Android/iOS 的机器学习移动应用
- 利用 GPU/NNAPI 代理加速端侧推理

## 场景标签

 · 领域:移动/端侧 ML 推理框架

## 证据(README 行号)

> L31: TensorFlow Lite Flutter plugin provides a flexible and fast solution for accessing TensorFlow Lite interpreter and 
> L19: This repo is a TensorFlow managed fork of the tflite_flutter_plugin project by the amazing Amish Garg. The goal of 

## 星数曲线

```mermaid
xychart-beta
    title "tensorflow/flutter-tflite 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 653 --> 655
    line [654, 654]
```

2026-10-18 654 → 2026-10-23 654（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `4172704d4635` · [字段定义](../../DATASET.md)*
