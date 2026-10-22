# ptsochantaris/emeltal

⭐ 191 · C++ · MIT · 推送 2026-06-04 · [GitHub](https://github.com/ptsochantaris/emeltal) · 个人维护

**macOS/iOS 本地 ML 语音聊天应用，用高端开源模型**

面向终端用户的本地语音聊天应用，支持 macOS、iOS 与 visionOS，通过 TestFlight 分发构建。应用基于 llama.cpp 运行 LLM、whisper.cpp 做语音识别，在设备本地完成对话。提供精选的开源高性能模型列表（Qwen、Dolphin、Samantha、Gemma、Llama、Devstral、DeepSeek Coder、Whisper 等），多数模型以其最大上下文运行（特大变体上限 16384 tokens）。另提供轻量伴侣应用 Emellink，可在算力不足的设备上通过网络连接 Emeltal 获得相同语音界面。项目处于持续开发中；基于 MLX 的实验变体 Emextal 另行开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地运行 LLM 语音聊天，基于 llama.cpp 与 whisper.cpp
- 精选多系列开源模型（Qwen/Dolphin/Gemma/Llama/DeepSeek Coder 等）
- 覆盖 macOS、iOS、visionOS，经 TestFlight 分发
- Emellink 伴侣应用支持低算力设备远程接入

## 适用场景

- 在 Mac 或 iPhone 上进行本地离线语音对话
- 不依赖云端 API 使用开源 LLM 与 Whisper 语音识别
- 在算力不足设备上通过 Emellink 接入主机的语音界面

## 场景标签

 · 领域:语音对话应用/本地推理

## 证据(README 行号)

> L7: Local ML voice chat using high-end models, aiming for a self contained, user-friendly out-of-the-box experience as m
> L83: - Emeltal heavily relies on the llama.cpp for LLM processing, and whisper.cpp for voice recognition.

## 星数曲线

```mermaid
xychart-beta
    title "ptsochantaris/emeltal 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 190 --> 192
    line [191, 191]
```

2026-10-18 191 → 2026-10-22 191（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `45b8d5a0cf48` · [字段定义](../../DATASET.md)*
