# aichatwatch/aicw-video

⭐ 14 · TypeScript · MIT · 推送 2026-10-10 · [GitHub](https://github.com/aichatwatch/aicw-video) · [官网](https://aichatwatch.com/aicw-video/?utm_source=github) · 组织维护

**把人物访谈视频剪成带字幕与隐私保护的社交媒体短片的本地 AI 应用**

开源的独立视频剪辑应用与 MCP 工具：本地转录语音（whisper.cpp）生成字幕、本地 TensorFlow 检测人脸后打码或表情替换、用合成配音替换原声保护声音隐私、AI 场景分析推荐短片区间，并导出 TikTok/Reels/Shorts 等格式。可经浏览器 hub 单独运行，也可作为 stdio MCP server 接入 Claude Code、Claude Desktop、Codex。转录与人脸检测完全本地，场景分析可用云端 CLI 或本地 Ollama（当前仅文本）。仅支持 macOS，配音为 alpha，通过 Homebrew 或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 本地 whisper.cpp 转录生成并渲染字幕
- 本地人脸检测实现面部模糊/表情替换与合成配音
- stdio MCP server + Claude Skill，接入 Claude Code / Desktop / Codex
- AI 场景分析推荐短片区间，支持云端 CLI 或本地 Ollama 后备

## 适用场景

- 把访谈视频批量剪成 TikTok / Reels / Shorts 等社交短片
- 发布前对面部和声音做隐私保护处理
- 让 Claude Code 等 agent 通过自然语言完成剪片流程

## 场景标签

`语音识别` `人脸识别` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L13: - **Auto-generate captions** Transcribes speech locally, previews captions, and renders them into the final video.
> L14: - **Protects faces** Detects face regions locally, then blurs them or replaces them with emoji overlays.
> L15: - **Protects voices** Replaces original speaking audio with computer-generated voice-over.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f7736406d6b8` · [字段定义](../../DATASET.md)*
