# T3-Venture-Labs-Limited/clipyyy

⭐ 4 · Python · MIT · 推送 2026-11-05 · [GitHub](https://github.com/T3-Venture-Labs-Limited/clipyyy) · 组织维护

**自托管的 AI 视频切片工具：长视频转短视频切片**

开源（MIT）的自托管视频切片工具：输入 YouTube 链接、播客或本地视频，用 faster-whisper 在本地转写音频，LLM 选取独立成段的时刻并生成标题、文案与话题标签，MediaPipe 人脸跟踪重构成 9:16 等竖屏画幅，ffmpeg 烧录逐词动画字幕，输出可直接发布的 MP4。提供 Web 应用与 JSON 命令行（供脚本和 AI agent 调用，附 SKILL.md 技能文件），通过 OpenRouter 接入任意模型；视频不出本机，仅转写文本发给所选模型。源码运行需 Python 3.11–3.12、Node 22+、uv 与带 libass 的 ffmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 基于全转写文本排序切片并对齐句子边界
- faster-whisper 本地转写，支持 90+ 语言、CPU 或 GPU
- MediaPipe 人脸跟踪自动重构 9:16/4:5/1:1 画幅
- 全命令行支持 --json 输出并提供 agent 技能文件

## 适用场景

- 把播客和访谈批量切成 TikTok/Reels/Shorts 短视频
- 本地处理视频，不把素材上传到第三方服务器
- 用脚本或 AI agent 自动化切片流程
- 通过 Buffer 定时发布切片到多个社交平台

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L18: clipyyy is an open-source tool that cuts long-form video into short vertical clips automatically. Give it a YouTube
> L26: - **Local transcription.** faster-whisper with word-level timestamps, on CPU or GPU, in 90+ languages.
> L103: |3. Find clips|The LLM returns ranked clips with titles, captions, hashtags and B-roll ideas. Clips are checked ag

## 星数曲线

```mermaid
xychart-beta
    title "T3-Venture-Labs-Limited/clipyyy 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-22"]
    y-axis "stars" 2 --> 5
    line [3, 4]
```

2026-11-19 3 → 2026-11-22 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `f0b9d4cd198f` · [字段定义](../../DATASET.md)*
