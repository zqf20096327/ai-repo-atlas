# yaoyue123/VidDub

⭐ 19 · Python · MIT · 推送 2026-07-01 · [GitHub](https://github.com/yaoyue123/VidDub) · 个人维护 · 中文 README

**YouTube 视频自动中文配音并发布到国内平台的端到端管线**

面向内容创作者与开发者的视频翻译配音工具：管线为 yt-dlp 下载 YouTube 视频，本地 Whisper 生成带时间戳字幕，经 SiliconFlow API（Qwen2.5/DeepSeek）翻译为中文，CosyVoice2 TTS 合成配音，ffmpeg 替换音轨合成视频，并由 social-auto-upload 自动发布到 Bilibili、抖音、快手、腾讯视频、小红书 5 个平台；另提供 AI 生成标题候选与标签。提供 Web UI、CLI 与 REST API 三种使用方式，依赖 SiliconFlow API 密钥与本地 ffmpeg，Docker Compose 可部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YouTube URL→转写→翻译→TTS→合成→发布的全自动管线
- 本地 Whisper 转写 + CosyVoice2 TTS（支持声音克隆）
- 一键发布到 Bilibili/抖音/快手/腾讯视频/小红书
- Web UI + CLI + REST API 三种接口，Docker Compose 部署

## 适用场景

- 把英文 YouTube 视频做成中文配音视频
- 将配音后视频一键分发到多个国内视频平台
- 无头服务器上批量跑视频翻译配音任务

## 场景标签

`语音合成` `语音识别` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L15: > **v5.0** 端到端管线：YouTube URL → Whisper STT → SiliconFlow 翻译 → CosyVoice2 TTS → ffmpeg 合成 → 字幕 → 多平台自动发布。
> L27: 3. 🌐 **翻译** — 通过 **SiliconFlow AI**（Qwen2.5 / DeepSeek）将英文字幕翻译为中文
> L28: 4. 🗣️ **配音** — 使用 **CosyVoice2 TTS** 合成自然流畅的中文语音

## 星数曲线

```mermaid
xychart-beta
    title "yaoyue123/VidDub 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c860c8e25e09` · [字段定义](../../DATASET.md)*
