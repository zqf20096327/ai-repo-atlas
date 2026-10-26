# lukaszliniewicz/Subdub

⭐ 28 · Python · 推送 2026-05-19 · [GitHub](https://github.com/lukaszliniewicz/Subdub) · 个人维护

**视频转配音视频的命令行工具：转录、翻译、TTS 配音与同步**

Python 命令行应用，提供视频到配音视频的完整流水线：用 WhisperX 转录、通过 LiteLLM 调用 LLM（或 DeepL）校正/翻译字幕、用 XTTS API 生成配音语音、再将配音音频与视频同步混合。为 Pandrator 项目开发，也可独立运行。支持 9 种任务模式（full/transcribe/translate/correct/sync 等）与大量 CLI 参数（模型选择、提示词覆盖、说话人分离、手动校正 GUI 等）。运行需 Python 3.10+、FFmpeg、WhisperX 和本地 XTTS API 服务，LLM 调用需相应 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WhisperX 转录 + LLM/DeepL 翻译 + XTTS 配音 + 音视频同步的端到端流水线
- LLM 调用统一经 LiteLLM 路由，支持 Anthropic/OpenAI/Gemini/OpenRouter 等提供商
- 9 种任务模式可单独运行（转录/翻译/校正/字幕均衡化/Zoom 转录整理等）
- 支持说话人分离、术语表记忆、二次评估改进与 PyQt6 手动校正 GUI（可选）

## 适用场景

- 把外语视频一键转成带配音和字幕的翻译版视频
- 仅转录视频生成 SRT 字幕并做文本校正
- 翻译和均衡化现有字幕文件

## 场景标签

 · 领域:媒体处理/翻译配音

## 证据(README 行号)

> L5: - transcribing media with WhisperX,
> L7: - generating dubbed speech with XTTS,
> L8: - and syncing dubbed audio back into video.

## 星数曲线

```mermaid
xychart-beta
    title "lukaszliniewicz/Subdub 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-26 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `58603ed4ac42` · [字段定义](../../DATASET.md)*
