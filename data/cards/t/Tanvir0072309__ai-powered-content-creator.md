# Tanvir0072309/ai-powered-content-creator

⭐ 13 · HTML · MIT · 推送 2026-07-18 · [GitHub](https://github.com/Tanvir0072309/ai-powered-content-creator) · 个人维护

**输入 URL 自动生成印地语/乌尔都语心理学短视频的本地 Web 应用**

PsychClips 是面向印地语/乌尔都语内容创作者的本地 Flask Web 应用：用户粘贴 YouTube 短视频 URL 并输入主题，系统经 5 步流水线自动完成——Groq（llama-3.3-70b）生成脚本、ElevenLabs 或 gTTS 生成配音、yt-dlp 下载素材、FFmpeg 剪辑/滤镜/混音并导出竖屏成片。需自备 Groq API key（必需）与 ElevenLabs key（可选，缺失时回退免费 gTTS）。API key 以 XOR+Base64 加密本地存储。README 另附未来转为 SaaS 的分阶段计划。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 主题→脚本→配音→剪辑→成片的 5 步自动流水线
- Groq llama-3.3-70b 生成脚本，ElevenLabs/gTTS 生成配音
- FFmpeg 剪辑、滤镜、背景音乐混音、1080x1920 竖屏导出
- API key XOR+Base64 加密存储，含 PWA 离线外壳

## 适用场景

- 印地语/乌尔都语创作者批量制作心理学类短视频
- 粘贴素材 URL 后自动产出可上传的竖屏短片与文案标签
- 无配音预算时用免费 gTTS 兜底生成 Hindi 配音

## 场景标签

`AI 写作` `视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L12: > - Generates a script *(Groq AI)*
> L65: |**1**|Topic|Groq AI|Hindi Script *(hook + full script + mood)*|
> L153: |7|Click **"VIDEO BANAO"** (Generate Video)|

## 星数曲线

```mermaid
xychart-beta
    title "Tanvir0072309/ai-powered-content-creator 星数(近 3 点)"
    x-axis ["2026-10-23", "2026-10-29", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-23 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1f135b304899` · [字段定义](../../DATASET.md)*
