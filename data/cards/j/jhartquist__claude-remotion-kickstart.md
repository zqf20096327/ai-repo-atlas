# jhartquist/claude-remotion-kickstart

⭐ 122 · TypeScript · MIT · 推送 2025-12-09 · [GitHub](https://github.com/jhartquist/claude-remotion-kickstart) · [官网](https://youtu.be/z7Bkf3Vc63U) · 个人维护

**用 Claude Code 与 Remotion 以代码方式生成视频的启动模板**

基于 Remotion 的 GitHub 模板仓库，提供预置视频组件（标题页、代码块、Mermaid/D2 图表、字幕、B-roll 等）与通过 Claude Code 斜杠命令触发的 AI 资产生成流程：/generate-image 调用 Nano Banana Pro、/generate-video 调用 Veo 3.1、/transcribe 调用 Deepgram、配音经 ElevenLabs MCP。支持自定义 fps 与分辨率预设、Tailwind 样式、词级时间戳同步与 GitHub Actions CI 渲染。运行需 Node.js 20+、pnpm、Claude Code 与 ffmpeg；AI 功能需另外配置各服务 API key，且环境变量须在 shell 中设置而非 .env。作者声明此仓库为实验性质，文档可能存在多处 bug。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 预置 Title/Code/Diagram/BRoll 等视频组件库
- Claude Code 斜杠命令生成图片（Nano Banana Pro）、视频（Veo 3.1）与转录（Deepgram）
- 词级时间戳将视觉与配音同步
- 内置 GitHub Actions 工作流在 CI 中渲染视频

## 适用场景

- 用 Claude Code 辅助编写 Remotion 代码来制作讲解类视频
- 为技术内容快速生成含配音、字幕与代码展示的视频
- 在 CI 中自动渲染并产出 mp4 成品

## 场景标签

`视频生成` `图像生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Create videos programmatically with Claude Code and Remotion. This starter kit provides pre-built components, AI int
> L12: - **AI-powered asset generation** - Generate images, videos, and voiceovers with slash commands
> L132: ## Slash Commands (Claude Code)

## 星数曲线

```mermaid
xychart-beta
    title "jhartquist/claude-remotion-kickstart 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 120 --> 123
    line [121, 122]
```

2026-10-18 121 → 2026-10-24 122（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `89f6c6fb2ec6` · [字段定义](../../DATASET.md)*
