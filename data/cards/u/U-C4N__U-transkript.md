# U-C4N/U-transkript

⭐ 14 · Python · MIT · 推送 2026-10-09 · [GitHub](https://github.com/U-C4N/U-transkript) · [官网](https://www.uc4n.com) · 个人维护

**YouTube 字幕提取、AI 翻译与视频下载的 Python 库**

零依赖的 Python 库，从任意视频、播放列表或频道提取字幕（SRT/WebVTT/JSON/文本），调用 Claude、OpenAI、Gemini、OpenRouter 或 Ollama 等 AI 服务商官方 SDK 做保留时间轴的字幕翻译并生成双语字幕；支持最高 8K 的并行可断点续传视频下载，除 .mp3 外无需 ffmpeg。提供 youtube-transcript-api 的兼容导入层（改一行 import 即可迁移），并附带 MCP 服务器 utmax-mcp，供 Claude、Codex 等 AI 助手调用六个工具。自称处于 Alpha 阶段，0.1.0 前 API 可能变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 提取任意视频/播放列表/频道的多语言字幕（人工或自动生成）
- 通过多家 AI 服务商官方 SDK 做保留时间轴的字幕翻译与双语字幕
- 最高 8K、并行且可断点续传的视频下载，除 .mp3 外无需 ffmpeg
- MCP 服务器提供 6 个工具，供 Claude Code、Codex、Claude Desktop 调用

## 适用场景

- 批量拉取 YouTube 视频或整个频道的字幕做内容分析
- 用 AI 把英文字幕翻译成其他语言并生成双语字幕文件
- 让 Claude/Codex 等 AI 助手直接下载视频并翻译字幕
- 从 youtube-transcript-api 低成本迁移

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L15: - **AI translation** that keeps every timing (Claude, OpenAI and compatible servers such as
> L52: `utmax-mcp` gives an AI assistant six tools: `list_tracks`, `get_transcript`, `list_formats`,

## 星数曲线

```mermaid
xychart-beta
    title "U-C4N/U-transkript 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e8c5effb9241` · [字段定义](../../DATASET.md)*
