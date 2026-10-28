# leemjnnkdzuy/auto-voice-over-tool

⭐ 24 · TypeScript · 推送 2026-06-12 · [GitHub](https://github.com/leemjnnkdzuy/auto-voice-over-tool) · 个人维护 · 中文 README

**视频自动配音桌面工具：下载-转录-翻译-配音-渲染一条龙**

基于 Electron（React 19 + TypeScript + Vite）的桌面应用，面向多语言内容创作者：输入视频链接（如 YouTube）后经 yt-dlp 下载，用本地 Whisper 引擎（ggml-org，CPU/CUDA 版）生成 SRT 字幕，可调用翻译 API 翻译并用 Edge TTS（msedge-tts）生成配音，最终经 FFmpeg NVENC 与 HandBrakeCLI 以恒定帧率合成成品视频。首次启动自动下载约 300MB 的外部二进制与模型（ggml-base.bin）。需 Node.js 20+，NVIDIA CUDA/NVENC 显卡为推荐配置，面向 Windows PowerShell 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Whisper（ggml CPU/CUDA）转录生成 SRT 字幕
- Edge TTS 多语言配音，可调语速对齐口型
- FFmpeg NVENC + HandBrakeCLI 恒定帧率防音画不同步
- yt-dlp 支持从多平台下载视频源

## 适用场景

- 把英文视频自动配音成日语、中文等多语言版本
- 为 YouTube 视频生成字幕、翻译并换上 AI 配音
- 批量制作多语言内容分发到全球市场

## 场景标签

`语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L29: 2. **Transcribe Phase:** Trích xuất lời thoại từ video thông qua AI Whisper cục bộ. Tự động chia các mốc thời gian 
> L31: 4. **TTS Phase (Text-to-Speech):** Sử dụng dịch vụ Edge TTS (`msedge-tts`) nhằm biến văn bản đã dịch thành các file

## 星数曲线

```mermaid
xychart-beta
    title "leemjnnkdzuy/auto-voice-over-tool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fdbc845c96b8` · [字段定义](../../DATASET.md)*
