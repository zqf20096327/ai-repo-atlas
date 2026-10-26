# mlalma/KokoroTestApp

⭐ 51 · Swift · Apache-2.0 · 推送 2026-02-01 · [GitHub](https://github.com/mlalma/KokoroTestApp) · 个人维护

**在 macOS/iOS 上运行 Kokoro TTS 模型的 SwiftUI 测试应用**

基于 SwiftUI 的测试应用，演示 Kokoro TTS 神经网络语音合成模型在 Apple Silicon 上的运行：通过 MLX 框架执行推理，提供 28 种声音风格，生成速度快于实时并附带性能指标。支持 iOS 18.0+ 与 macOS 15.0+，需在真机运行（iOS 模拟器不支持 MLX）。仓库以 Git LFS 存储约 600MB 的模型文件（kokoro-v1_0.safetensors），通过 Xcode 打开并构建。依赖 Kokoro iOS、MLX、MisakiSwift 等 Swift 包。采用 Apache 2.0 许可证。

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

- 基于 MLX 在 Apple Silicon 上运行 Kokoro TTS 推理
- 提供 28 种声音风格生成语音
- 快于实时的语音生成并显示性能指标

## 适用场景

- 在 Mac 或 iPhone 上测试 Kokoro TTS 模型的语音合成效果
- 体验不同声音风格的离线语音生成
- 作为在 Apple 平台集成 Kokoro TTS 的参考实现

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: A SwiftUI test application for the Kokoro TTS (Text-to-Speech) model, demonstrating high-quality faster than real-ti
> L52: - **High-Quality TTS**: Leverages the Kokoro neural TTS model for natural-sounding speech synthesis

## 星数曲线

```mermaid
xychart-beta
    title "mlalma/KokoroTestApp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-26 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a240c338c6c4` · [字段定义](../../DATASET.md)*
