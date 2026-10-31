# jatinkrmalik/localcaption

⭐ 15 · Python · MIT · 推送 2026-09-06 · [GitHub](https://github.com/jatinkrmalik/localcaption) · [官网](https://pypi.org/project/localcaption/) · 个人维护

**本地离线 Whisper 转录工具：URL/本地音视频生成字幕文件**

Python CLI 工具 localcaption，用 yt-dlp 下载 YouTube/Vimeo/Twitch 等 1000+ 站点音频，经 ffmpeg 转为 16kHz 单声道 WAV 后，用本地 whisper.cpp（默认）或可选的 faster-whisper 做离线转录，输出 .txt/.srt/.vtt/.json，无需 API key。面向播客作者、转录访谈/讲座的研究者等不愿上传音频到云端的人群。支持批量处理、YouTube 章节导出、本地 Ollama 生成摘要、历史转录检索（search 子命令）与模型管理；doctor --fix 自动安装系统依赖、克隆并编译 whisper.cpp、下载默认 small.en 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- whisper.cpp 默认后端，faster-whisper 可选，全流程本地无需 API key
- 一次运行输出 .txt/.srt/.vtt/.json 四种格式
- --summary 通过本地 Ollama 生成摘要，--batch 批量处理
- doctor --fix 自动安装缺失依赖、编译 whisper.cpp 并下载模型

## 适用场景

- 给播客或视频批量生成 SRT/VTT 字幕而不上传音频
- 研究者本地转录访谈或讲座录音
- 获取 YouTube 文字稿而无需登录或使用云端 API
- 转录后用 search 命令按时间戳检索历史内容

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L5: Offline Whisper transcription for YouTube and local files. Writes SRT, VTT, and JSON. No API key.
> L33: |Transcribe locally|`whisper.cpp` (default) or `faster-whisper`|
> L43: - **Offline Whisper.** Audio is transcribed on your machine. No API key, no account.

## 星数曲线

```mermaid
xychart-beta
    title "jatinkrmalik/localcaption 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2c11ecea537d` · [字段定义](../../DATASET.md)*
