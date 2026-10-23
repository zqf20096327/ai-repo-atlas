# umlx5h/LLPlayer

⭐ 4,400 · C# · GPL-3.0 · 推送 2026-09-10 · [GitHub](https://github.com/umlx5h/LLPlayer) · [官网](https://llplayer.com) · 个人维护

**面向语言学习的视频播放器：双语字幕、AI 字幕与实时翻译**

基于 C#/WPF 与 Flyleaf 库的 Windows 视频播放器，围绕字幕功能面向语言学习者：双语字幕同显、Whisper 驱动的实时 AI 字幕生成（whisper.cpp 与 faster-whisper 双引擎）、多引擎实时翻译（Google/DeepL/Ollama/LM Studio/OpenAI）、基于 LLM 的上下文感知翻译、OCR 位图字幕转文本、即时查词与浏览器搜索集成、yt-dlp 在线视频播放。ASR 与 OCR 本地执行；翻译可选本地 Ollama/LM Studio。当前为 Beta 版（0.X.X 期间会做破坏性变更），仅支持 Windows 10/11 x64，跨平台在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 双引擎（whisper.cpp/faster-whisper）实时 AI 字幕生成，支持 CUDA/Vulkan 加速
- 多翻译引擎含本地 LLM（Ollama、LM Studio），LLM 上下文感知翻译
- Tesseract/Microsoft OCR 将位图字幕实时转为文本
- ASR 与 OCR 全本地执行，仅需首次下载模型

## 适用场景

- 看外语视频时同时显示学习语言与母语双字幕
- 为无字幕视频实时生成 AI 字幕并翻译
- 播放时在字幕上即时查词、自定义浏览器搜索
- 配合 Yomitan/10ten 等浏览器扩展背单词

## 场景标签

`语音识别` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L5:  A video player focused on subtitle-related features such as dual subtitles, AI-generated subtitles, real-time trans
> L21: - **AI-generated subtitles (ASR):** Real-time automatic subtitle generation from any video and audio, powered by Op
> L22: - **Real-time Translation:** Supports many translation engines, such as Google, DeepL, Ollama, LM Studio, OpenAI.

## 星数曲线

```mermaid
xychart-beta
    title "umlx5h/LLPlayer 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 4365 --> 4403
    line [4368, 4383, 4389, 4400]
```

2026-10-18 4,368 → 2026-10-23 4,400（+32）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `7e9e502fc048` · [字段定义](../../DATASET.md)*
