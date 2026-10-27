# timoncool/VibeVoice_ASR_portable_ru

⭐ 41 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/timoncool/VibeVoice_ASR_portable_ru) · [官网](https://github.com/timoncool/VibeVoice_ASR_portable_ru/releases) · 个人维护

**Windows 便携离线语音识别工具：微软 VibeVoice 模型音频转文字**

面向 Windows 用户的便携语音识别（ASR）应用，基于微软 VibeVoice-ASR 模型，将音频/视频文件或麦克风录音转为文字，支持说话人分离、逐段时间戳、4-bit 量化模型（约 4GB VRAM）以降低显存占用。安装通过 install.bat 一键完成，自动下载便携 Python、CUDA 版 PyTorch、FFmpeg 与依赖；运行 run.bat 后在浏览器中打开俄语界面（Gradio），全程离线，所有文件隔离在单文件夹内。需 NVIDIA GPU（推荐 8GB+ VRAM）或 CPU 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Microsoft VibeVoice-ASR 的语音转文字，支持说话人分离与时间戳
- 4-bit 量化模型（约 4GB VRAM）与全量模型（约 8GB VRAM）两种选择
- install.bat 一键安装便携 Python、CUDA PyTorch、FFmpeg 等依赖
- 通过 FFmpeg 支持 MP3/WAV/MP4/MKV 等多种音视频格式

## 适用场景

- 离线转录会议录音或访谈并区分说话人
- 为视频文件提取语音文字与时间戳
- 显存有限的 NVIDIA 显卡上用 4-bit 模型做本地语音识别

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L12: VibeVoice ASR — современная модель распознавания речи от Microsoft, которая преобразует аудио в текст с высокой точ
> L16: - Распознавание речи в текст с высокой точностью

## 星数曲线

```mermaid
xychart-beta
    title "timoncool/VibeVoice_ASR_portable_ru 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-27 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `617ae214b107` · [字段定义](../../DATASET.md)*
