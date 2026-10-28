# DarkPancakes/clipforge

⭐ 25 · Python · MIT · 推送 2026-03-17 · [GitHub](https://github.com/DarkPancakes/clipforge) · 个人维护

**一条命令生成 YouTube Shorts/TikTok 竖屏短视频的工具**

面向内容创作者的 Python 命令行工具与库：输入主题后，用 LLM 生成脚本、fal.ai 生成 AI 图像并加 Ken Burns 镜头效果、Edge TTS 合成语音、生成逐词高亮 ASS 字幕，最终由 FFmpeg 渲染 1080x1920/30fps/H.264 的 55-65 秒竖屏视频。脚本 LLM 可选 Groq/OpenAI/Anthropic，无 API key 时可自带脚本，无图像 key 时回退渐变片段，单条视频成本约 $0.01。系统需 FFmpeg。

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

- 单命令从主题到成片（脚本→AI 图像→TTS→字幕→FFmpeg 渲染）
- 14+ Edge TTS 免费语音与 11 种内容风格模板
- 无 LLM key 可自带脚本、无图像 API 回退渐变片段
- 输出 1080x1920、H.264、30fps、55-65 秒竖屏视频

## 适用场景

- 一键批量生成短视频频道内容
- 不会剪辑也能产出带配音和字幕的短视频
- 以低成本（约 $0.01/条）持续产出 Shorts/TikTok 内容

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L14: Give ClipForge a topic. It writes a script, generates cinematic AI visuals, narrates with a natural voice, adds wor
> L36: Topic → LLM Script → Scene Extraction → AI Images → Ken Burns Clips

## 星数曲线

```mermaid
xychart-beta
    title "DarkPancakes/clipforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `223135f47f1f` · [字段定义](../../DATASET.md)*
