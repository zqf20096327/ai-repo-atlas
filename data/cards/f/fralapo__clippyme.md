# fralapo/clippyme

⭐ 61 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/fralapo/clippyme) · 个人维护

**自托管 Web 应用：把长视频自动切成竖屏短视频并发布**

面向创作者与剪辑者的自托管 Web 应用：输入 YouTube 链接或视频文件，自动转录后由 Google Gemini 挑选并排序可独立成段的片段，切为 9:16 竖屏并配字幕；支持主动说话人跟踪取景、调色、六种动效字幕、静音与填充词删除等编辑，经 Zernio 发布/排期到 TikTok、Instagram、YouTube，并可监控 Kick/Twitch/YouTube 频道全自动运行。转录默认用 Deepgram，可选 ElevenLabs 或本地 Whisper；无 Gemini key 时仍可按主题切分但不排序。以 Docker Compose 部署，数据存本地，默认仅监听 127.0.0.1。

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

- Gemini 挑选并排序片段，切口落在句子边界与静音处
- 主动说话人跟踪的竖屏取景，可切换居中或加黑边全帧
- 本地 Whisper / Deepgram / ElevenLabs 三种转录路径
- 可监控直播频道并自动剪辑发布，长任务重启后可续跑

## 适用场景

- 把长视频或直播录像自动剪成带字幕的竖屏短片
- 在发布前用浏览器内编辑器调整字幕、调色与钩子文案
- 自动排期发布短片到 TikTok / Reels / Shorts

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L11: ClippyMe is a self-hosted web app for creators and editors. Give it a YouTube
> L19: - **Finds the best moments.** The video is transcribed, and Google Gemini
> L49: Transcription uses Deepgram (the default) or ElevenLabs when you add its key

## 星数曲线

```mermaid
xychart-beta
    title "fralapo/clippyme 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 59 --> 62
    line [60, 61, 61]
```

2026-10-18 60 → 2026-10-24 61（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ea33f8498e60` · [字段定义](../../DATASET.md)*
