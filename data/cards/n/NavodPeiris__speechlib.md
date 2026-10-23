# NavodPeiris/speechlib

⭐ 268 · Python · MIT · 推送 2026-04-19 · [GitHub](https://github.com/NavodPeiris/speechlib) · 个人维护

**统一说话人分离、识别与转录的 Python 管线库**

Speechlib 是一个 Python 库，将说话人分离（PyAnnote）、说话人识别（SpeechBrain）与语音转录（faster-whisper、Whisper、HuggingFace 模型、AssemblyAI 云端）组合为单一 Pipeline，输出带说话人姓名与时间戳的转录文本（txt/json/srt）。通过 voices_folder 中的参考音频将 SPEAKER_XX 标签映射为真实姓名；各阶段后端可通过继承抽象基类替换。要求 Python 3.10+ 与 ffmpeg，GPU 执行需 CUDA 11 及 cuBLAS/cuDNN 8；含音频预处理与批处理功能。

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

- 单一 Pipeline 组合 diarization + 说话人识别 + ASR，输出带姓名与时间戳的转录
- 可插拔后端：4 种 ASR 后端 + 自定义基类扩展
- voices_folder 参考音频将说话人标签映射为真实姓名
- 支持 96 种语言的转录与 txt/json/srt 输出格式

## 适用场景

- 为会议、访谈录音生成带真实说话人姓名的逐字稿
- 批量处理多路通话音频并输出结构化转录 JSON
- 用自己的微调 Whisper 模型或 HuggingFace ASR 模型构建本地转录管线

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L8: Speechlib is a Python library that unifies speaker diarization, speaker recognition, and transcription into a single
> L73: ### FasterWhisperASR _(recommended)_

## 星数曲线

```mermaid
xychart-beta
    title "NavodPeiris/speechlib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 267 --> 269
    line [268, 268]
```

2026-10-18 268 → 2026-10-23 268（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `85988c681755` · [字段定义](../../DATASET.md)*
