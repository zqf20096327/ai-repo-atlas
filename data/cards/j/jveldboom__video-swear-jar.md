# jveldboom/video-swear-jar

⭐ 20 · JavaScript · 推送 2026-07-31 · [GitHub](https://github.com/jveldboom/video-swear-jar) · 个人维护

**本地 Docker 工具：转录视频音频并剪除脏话片段**

以 Docker 容器形式提供的视频粗话过滤工具：用 OpenAI Whisper 转录视频音频，按预定义 swear-words.json 检测脏话，生成时间戳并用 FFmpeg 剪切生成无脏话的新视频文件，全程本地处理无需联网。转录引擎默认 whisper-ctranslate2，可选 whisper（README 注明后者可能被移除）。另提供手动剪切视频、读取字幕查脏话、直接调用 whisper/ffmpeg CLI 等辅助命令。已知问题：容器内存不足会导致报错，small.en 模型建议至少分配 4GB 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Whisper 转录 + 词表匹配检测脏话 + FFmpeg 自动剪切生成新视频
- 完全本地处理，无需联网与上传视频
- 支持选择 whisper 模型（tiny 至 large）与转录引擎（whisper-ctranslate2/whisper）
- 附带 cut-video/read-subtitles 等辅助命令

## 适用场景

- 把含脏话的视频处理成家庭友好版本
- 离线批量处理视频而无需上传云端
- 手动核对字幕中的脏话位置再自行剪辑

## 场景标签

`语音识别` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Introducing Video Swear Jar, your AI-powered solution for creating clean video content! This project offers a Docker
> L11: - Transcribe the video file using OpenAI Whisper

## 星数曲线

```mermaid
xychart-beta
    title "jveldboom/video-swear-jar 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c618ab60ec74` · [字段定义](../../DATASET.md)*
