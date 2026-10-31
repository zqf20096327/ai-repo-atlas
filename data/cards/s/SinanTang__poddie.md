# SinanTang/poddie

⭐ 21 · TypeScript · GPL-3.0 · 推送 2026-10-03 · [GitHub](https://github.com/SinanTang/poddie) · 个人维护

**macOS 本地文本式视频/播客编辑器：删词即剪辑**

面向播客创作者与视频创作者的 macOS 桌面应用：导入音视频后生成本地词级转录（whisper.cpp 本地模型或 OpenAI API），用户删除不想保留的词或静音段，应用按删除结果剪辑媒体并导出 MP4/M4A/MP3/SRT。附加功能包括静音自动裁剪、填充词一键删除、字幕烧录，以及基于 Ollama 本地 LLM（默认 Qwen3 8B）的章节整理。数据以 JSON sidecar 保存在源文件旁。仅支持 macOS，处于 beta 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 词级转录驱动剪辑：删除文字即删除对应媒体片段
- 本地 Whisper 免费离线转录，或改用 OpenAI API（约$0.006/分钟）
- Ollama 本地 LLM 章节整理，默认 Qwen3 8B，可换任意 Ollama 兼容模型
- 静音自动裁剪与 EN/CN 填充词一键删除

## 适用场景

- 不进时间线，靠校对文字快速剪掉播客口误与废话
- 在本地完成转录与剪辑，不把素材上传云端
- 为视频生成并烧录字幕

## 场景标签

`语音识别` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L16: - 🎙️ **Transcribe free & offline** with a local Whisper model — or use OpenAI's API
> L28:  at the chapter level before word-level editing. Runs entirely on your machine. Works with any Ollama-compatible mo

## 星数曲线

```mermaid
xychart-beta
    title "SinanTang/poddie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4fc61f459f98` · [字段定义](../../DATASET.md)*
