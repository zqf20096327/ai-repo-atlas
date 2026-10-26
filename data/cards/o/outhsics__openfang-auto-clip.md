# outhsics/openfang-auto-clip

⭐ 38 · Python · MIT · 推送 2026-09-08 · [GitHub](https://github.com/outhsics/openfang-auto-clip) · [官网](https://github.com/outhsics/openfang-auto-clip#readme) · 组织维护 · 中文 README

**本地优先的长视频转短视频自动化流水线**

用 Python + FFmpeg 构建的本地视频处理流水线：通过 yt-dlp 下载源视频，按本地策略切出 9:16 短视频片段，提供 Level 1 视觉混音、Level 2 脚本再生包（transcript→script/shot plan，尚不能自动重建 成片）、双语 review report、synthetic benchmark 与本地 Web 管理界面。支持多种 STT/TTS 提供商（Groq/OpenAI Whisper/本地 Whisper、Edge/OpenAI/ElevenLabs TTS），可发布到 Telegram/WhatsApp。面向内容创作者，Level 3 与成片重建仍未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- yt-dlp 下载 + 本地策略切 9:16 短视频片段
- Level 2 脚本再生包：时间锚点、shot plan、voiceover note、review rubric
- 多种 STT/TTS 提供商可选，含完全离线的本地 Whisper
- 提供 --doctor/--dry-run、synthetic benchmark 与本地 Web 管理界面

## 适用场景

- 把长视频切成适合 TikTok/Reels/Shorts 的竖屏短视频
- 本地离线处理视频，不上传云端
- 生成带时间锚点的短视频脚本包供人工验收

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L72: - 跑一个可用的本地 Level 1 FFmpeg 视觉混音路径
> L73: - 在提供 transcript 的前提下生成一个带时间锚点、shot plan、asset request、voiceover note 和 review rubric 的 Level 2 脚本再生包
> L157: - **Groq Whisper** - ⚡ 超快速，部分免费

## 星数曲线

```mermaid
xychart-beta
    title "outhsics/openfang-auto-clip 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-26 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `005d7e14ac50` · [字段定义](../../DATASET.md)*
