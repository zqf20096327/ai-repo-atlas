# Hkshoonya/nvidia-broadcast-linux

⭐ 200 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/Hkshoonya/nvidia-broadcast-linux) · [官网](https://nvbroadcast.com) · 个人维护

**Linux/macOS 的开源 AI 摄像头与麦克风特效应用**

面向 Linux/macOS 用户的非官方 NVIDIA Broadcast 替代：提供 AI 背景虚化/替换/绿幕、人脸跟踪自动构图、视线校正、视频增强、麦克风降噪与语音特效，以及基于本地 Whisper 的会议转录与摘要。视觉模型支持 RVM/IS-Net/BiRefNet，含 9 种从 CUDA 到 CPU 的处理模式；虚拟摄像头兼容 Chrome/Zoom/Discord/OBS。Linux 源码安装器构建独立运行时，GPU 模式仅限 Linux 且要求 NVIDIA GPU；macOS 需 Apple Silicon 与 Homebrew 栈，虚拟摄像头依赖 OBS 注册。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 背景虚化/替换/绿幕与人脸跟踪自动构图（RVM/IS-Net/BiRefNet 三模型可选）
- 麦克风/扬声器降噪、语音特效与本地 Whisper 会议转录与 AI 摘要
- 9 种处理模式，从融合 CUDA 内核到纯 CPU 回退
- 虚拟摄像头输出兼容 Chrome、Firefox、Zoom、Discord、OBS

## 适用场景

- 在 Linux/macOS 上为视频会议做背景虚化、替换与降噪
- 直播时使用绿幕、自动构图与视频增强
- 录制会议并生成本地转录文本与行动项摘要

## 场景标签

`语音识别` `图像视频处理` `人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L14:  Open-source, unofficial NVIDIA Broadcast alternative for Linux and macOS. AI-powered virtual camera and audio tool
> L42: - **Background Blur** — AI-powered, person stays crystal sharp
> L65: - **AI Meeting Transcription** — Local Whisper speech-to-text (GPU-accelerated)

## 星数曲线

```mermaid
xychart-beta
    title "Hkshoonya/nvidia-broadcast-linux 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23", "2026-10-24"]
    y-axis "stars" 192 --> 200
    line [193, 195, 197, 198, 199]
```

2026-10-18 193 → 2026-10-24 199（+6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fa9fb74df428` · [字段定义](../../DATASET.md)*
