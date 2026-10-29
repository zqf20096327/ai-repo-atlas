# vicperdana/SemantiClip

⭐ 80 · C# · GPL-3.0 · 推送 2026-03-01 · [GitHub](https://github.com/vicperdana/SemantiClip) · [官网](https://github.com/vicperdana/SemantiClip/) · 个人维护

**把视频转成转录文本与博客文章的 .NET AI 应用**

面向内容创作者与教育者的视频转结构化文字应用：用 FFmpeg 从视频提取音频，经 Azure OpenAI Whisper 转录为文本，再生成可阅读的博客文章，并可通过 ModelContextProtocol 将文章发布到 GitHub 仓库。技术栈为 .NET 9、Blazor WebAssembly（MudBlazor UI）、Semantic Kernel Process/Agent 框架编排流程；内容生成支持 Azure GPT-4o 或本地 Ollama（如 phi4-mini）。README 声明这是概念验证项目，不用于生产环境。运行需自配 Azure OpenAI、Ollama、FFmpeg 与 GitHub token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- FFmpeg 提取音频 + Azure OpenAI Whisper 语音转文字
- 自动从转录文本生成博客文章
- 支持本地 Ollama（phi4-mini 等）做内容生成
- 通过 ModelContextProtocol 将博客文章发布到 GitHub

## 适用场景

- 把课程或演讲视频快速转成可发布的博客文章
- 视频内容的文字化存档与二次编辑
- 在本地 LLM 上离线生成内容草稿

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L22: - ✍️ **Transcription** – Converts speech to text using Azure OpenAI Whisper.
> L23: - 📝 **Blog Post Creation** – Automatically generates readable blog posts from transcripts.
> L25: - 🧩 **Local Content Generation** – Supports on-device LLM processing with Ollama.

## 星数曲线

```mermaid
xychart-beta
    title "vicperdana/SemantiClip 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-29 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fdaa387c8139` · [字段定义](../../DATASET.md)*
