# yakupbulbul/scenarix

⭐ 16 · JavaScript · MIT · 推送 2026-06-26 · [GitHub](https://github.com/yakupbulbul/scenarix) · [官网](https://scenarix.online) · 个人维护

**端到端生成短剧系列的工作室：剧本/图像/配音/字幕/配乐导出竖屏视频**

面向短剧内容创作者的自托管 Web 应用：从管理面板或 MCP 工具驱动整条流水线——基于系列 bible 生成多集剧本与场景图像，自动翻译剧集，用 ElevenLabs 生成配音，经 Remotion 导出带字幕、水印与背景音乐的 9:16 竖屏视频，并按张力、声音一致性等维度评分。支持多家 AI 提供商（文本：Anthropic/Google/OpenAI/Qwen；图像：Gemini/Leonardo/OpenAI/Qwen），需自备 API key，依赖 Node.js 20+ 与 PostgreSQL 14+。内置 13 个工具的 MCP 服务器，可被 Claude Code、Cursor、Copilot 以对话方式操作。

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

- 多集剧本生成：系列 bible 跟踪角色、情节线与悬念
- 多提供商图像生成，逐集选择提供商
- ElevenLabs 配音 + Remotion 导出 9:16 竖屏视频（字幕/水印/背景音乐）
- 内置 13 工具的 MCP 服务器，供 Claude Code/Cursor/Copilot 对话式管理剧集

## 适用场景

- 从零批量生成带配音字幕的短剧竖屏视频
- 把短剧系列自动翻译成其他语言
- 在编辑器里用 AI 编程助手对话式创建和管理剧集

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: I built this to generate short-form drama series end-to-end: screenplays, images, voiceovers, subtitles, background 
> L21: - Generates screenplays with a series bible that tracks characters, plot threads, and cliffhangers across episodes
> L25: - Exports 9:16 vertical video with subtitles, watermark, and background music using Remotion

## 星数曲线

```mermaid
xychart-beta
    title "yakupbulbul/scenarix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `24585a9fd962` · [字段定义](../../DATASET.md)*
