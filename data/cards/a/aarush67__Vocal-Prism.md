# aarush67/Vocal-Prism

⭐ 37 · Swift · MIT · 推送 2026-01-15 · [GitHub](https://github.com/aarush67/Vocal-Prism) · [官网](https://vocal.techfixpro.net/) · 个人维护

**macOS 本地音频转写应用：Whisper + CoreML，Apple Silicon 优化**

SwiftUI 编写的 macOS 桌面应用，调用捆绑的 whisper-cli（whisper.cpp）二进制在本地转写 MP3/WAV/M4A/FLAC 音频，实时流式显示转写文本与波形。通过 -ml 1 标志启用 CoreML 加速（Apple Neural Engine / GPU Metal），支持 base/small/medium/large 多种 Whisper 模型，可导出 .txt 与 .srt 字幕。限制：要求 macOS 26.0+、Apple Silicon（M1/M2/M3）、Xcode 15.0+，需自行在 Xcode 中捆绑模型与二进制资源并配置签名后编译运行；许可声明为教育与个人使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 whisper-cli 本地转写，实时流式输出与波形可视化
- CoreML 加速（ANE / GPU Metal），Apple Silicon 优化
- 支持 base/small/medium/large 多种 Whisper 模型与 CPU 线程配置
- 自动保存 .txt 并可导出带时间戳的 .srt 字幕

## 适用场景

- 在 Mac 上本地转写音频文件，不上传数据到云端
- 为视频生成带时间戳的 .srt 字幕文件
- 拖拽音频文件后实时查看转写进度与文本

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: A stunning, modern macOS application for transcribing audio files using OpenAI's Whisper model with CoreML accelerat
> L20: - ⚡ **CoreML Acceleration**: Automatic GPU acceleration on Apple Silicon

## 星数曲线

```mermaid
xychart-beta
    title "aarush67/Vocal-Prism 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-31 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `784138573d1e` · [字段定义](../../DATASET.md)*
