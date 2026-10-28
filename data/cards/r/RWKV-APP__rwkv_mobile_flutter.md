# RWKV-APP/rwkv_mobile_flutter

⭐ 20 · Dart · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/RWKV-APP/rwkv_mobile_flutter) · 组织维护 · 中文 README

**连接 Flutter 应用与 rwkv-mobile 本地推理引擎的 FFI 桥接层**

位于 Flutter 应用与原生 rwkv-mobile C++ 推理引擎之间的中间层插件：通过 Dart FFI 与专用 isolate 封装原生运行时，负责请求/响应协议（ToRWKV/FromRWKV 密封类）、模型生命周期管理、原生库加载与运行时协调，支持文本生成、批处理推理、视觉编码、Whisper 音频与 SparkTTS 语音流。后端通过 Backend 枚举选择（ncnn/llama.cpp/QNN/MLX/CoreML/MNN 等），实际可用性取决于各平台打包的原生二进制。以路径依赖或 Git 仓库方式接入，Android/iOS/macOS/Windows/Linux 均以预构建原生库随插件分发，版本由 native-libraries.json 固定的不可变归档还原。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Isolate 隔离的运行时桥接，推理不占用 UI isolate
- ToRWKV/FromRWKV 类型化消息协议，覆盖模型加载、生成、视觉、音频、TTS
- 一套 Dart 协议复用 CPU/GPU/NPU 多后端（ncnn/llama.cpp/QNN/MLX/CoreML/MNN/web-rwkv/MTK NP7）
- 五平台预构建原生库，由带 SHA-256 校验的不可变归档还原

## 适用场景

- 在 Flutter 应用中集成 RWKV 本地推理能力
- 构建支持文本生成、视觉、语音的端侧多模态应用
- 与 RWKV_APP 配套开发，维护应用与引擎间的桥接层

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L13: `rwkv_mobile_flutter` sits between a Flutter app and the native `rwkv-mobile` C++ inference engine. It is not just 
> L92: - **This layer:** isolate boundary, protocol, platform library loading, runtime orchestration, Dart-facing API surf

## 星数曲线

```mermaid
xychart-beta
    title "RWKV-APP/rwkv_mobile_flutter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `011165504b4a` · [字段定义](../../DATASET.md)*
