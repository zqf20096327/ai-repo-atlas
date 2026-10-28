# princekjha-dev/Clipify

⭐ 26 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/princekjha-dev/Clipify) · [官网](https://clipify-in.vercel.app/) · 个人维护

**面向内容团队的 AI 长视频切短视频生成工具**

Clipify 将长视频转换为适配各平台的短视频：从本地文件或 YouTube URL 下载视频，用 Whisper 做带时间戳的转录，结合音频能量、文本信号与 hook 检测做病毒式片段评分，再用 FFmpeg 零重编码切割并按 9:16/16:9/1:1 多比例导出，附带 VTT 字幕。支持 9 个 AI 提供商（openrouter/groq/deepseek/openai/anthropic/gemini/xai 等）自动回退，也可 --ai local 完全离线运行，无需 API key。提供反幻觉模式，将输出约束在转录内容内。以 Python CLI 形式运行，需 Python 3.8+ 与 FFmpeg，通过 git clone 加 setup 脚本安装。

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

- 单命令完成转录、片段评分、切割与多比例导出
- 9 个 AI 提供商可选，--ai local 支持完全离线运行
- 反幻觉模式将输出约束在转录文本内
- FFmpeg 零重编码切割，逐片段生成 VTT 字幕

## 适用场景

- 把播客或访谈长视频批量切成 TikTok/Shorts/Reels 格式短视频
- 监听文件夹自动处理新到视频并产出片段
- 无 API key 的离线环境下生成本地转录切片

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L13: Clipify transforms long-form video into short-form, platform-ready clips using AI transcription, viral-moment detec
> L75: |**Transcription**|Whisper-based audio-to-text with segment-level timestamps|
> L107: - Nine supported AI providers with automatic fallback chain

## 星数曲线

```mermaid
xychart-beta
    title "princekjha-dev/Clipify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `e6c3f488cc8d` · [字段定义](../../DATASET.md)*
