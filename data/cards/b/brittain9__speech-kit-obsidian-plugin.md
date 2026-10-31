# brittain9/speech-kit-obsidian-plugin

⭐ 27 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/brittain9/speech-kit-obsidian-plugin) · [官网](https://community.obsidian.md/plugins/local-dictation) · 个人维护

**Obsidian 语音工具箱：本地听写、转写、翻译与朗读**

面向 Obsidian 用户的语音与语言处理插件：流式听写、本地转写音频/视频文件、导入 YouTube 字幕、本地翻译（英语与另外七种语言）、自然语音朗读笔记，以及可选的 LLM 文本工具（用本地模型或自选远端 provider 对转写稿做清理、摘要、改写）。模型按需下载管理，支持 Whisper Large V3 Turbo、Moonshine、Nemotron 3.5 ASR、Pocket TTS 等。本地功能无需账号或 API key，装好模型后可离线工作；跨 macOS/Windows/Linux。实现为 TypeScript 插件加 Rust 原生 sidecar。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 听写/转写/翻译/朗读/YouTube 字幕导入集成于单一插件
- 本地优先：无需账号、API key，模型安装后可离线运行
- 可选接入 LLM provider 对转写稿做清理、摘要、改写
- 跨 macOS/Windows/Linux，支持 Metal/CUDA 硬件加速

## 适用场景

- 在 Obsidian 中边说边写，长会话听写成 Markdown
- 把会议录音或视频文件在本地转成带说话人标签的文字稿
- 离线翻译笔记并用自然语音朗读
- 导入 YouTube 视频字幕而不下载视频

## 场景标签

`语音识别` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L11: - **Dictate:** Capture long sessions with live text and a choice of speech models.
> L12: - **Transcribe files:** Drop in audio or video and turn its audio into a local transcript.
> L45: **Transcribe files.** Run **Transcribe local audio file** to turn an audio or video recording into text in the curr

## 星数曲线

```mermaid
xychart-beta
    title "brittain9/speech-kit-obsidian-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 25 --> 28
    line [26, 27]
```

2026-10-18 26 → 2026-10-31 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5947d5f7e302` · [字段定义](../../DATASET.md)*
