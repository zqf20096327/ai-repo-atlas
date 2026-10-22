# JosefAlbers/wtm

⭐ 227 · Python · MIT · 推送 2026-05-25 · [GitHub](https://github.com/JosefAlbers/wtm) · 个人维护

**基于 MLX 的 Whisper 语音转文本库，单文件实现**

Whisper Turbo MLX 的 Python 封装，核心代码为单文件、少于 300 行，在 Apple MLX 框架上运行 Whisper 语音转录。提供 CLI（wtm 命令，支持 multilingual/timestamps/quick 参数）与 Python API（transcribe 函数，返回文本与分段）。FFmpeg 为可选加速解码依赖，缺失时自动回退到 librosa；另提供 Linux 下 CUDA 与 CPU-only 的安装变体。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件、少于 300 行的 Whisper MLX 实现
- CLI 与 Python API 两种使用方式
- multilingual / timestamps / quick 参数控制输出
- FFmpeg 可选，缺失时自动回退 librosa 解码

## 适用场景

- 在 Apple Silicon 上转录音频为文本
- 需要带时间戳的语音转文字结果
- 在 Python 项目中集成 Whisper 转录功能

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Fast, lightweight Whisper transcription using MLX, in a single file under 300 lines.
> L36: wtm audio.mp3

## 星数曲线

```mermaid
xychart-beta
    title "JosefAlbers/wtm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 226 --> 228
    line [227, 227]
```

2026-10-18 227 → 2026-10-22 227（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `71fbe97e6cd3` · [字段定义](../../DATASET.md)*
