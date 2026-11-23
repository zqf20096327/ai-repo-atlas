# laaielichter/Ai-edit-studio

⭐ 4 · JavaScript · MIT · 推送 2026-11-19 · [GitHub](https://github.com/laaielichter/Ai-edit-studio) · 个人维护

**本地优先视频编辑器：57+ MCP 工具让 AI 代理剪辑视频**

面向创作者与 AI 代理的 local-first 视频编辑器，同一引擎提供人工时间线界面与 59 个代理工具（MCP、HTTP/OpenAPI、CLI）。功能覆盖自动剪辑、竖屏 reframe、动画字幕、本地作曲、语音转写文本剪辑、长视频分段缓存渲染、QC 检查与发布包；素材仅在本机读取，不外传。Windows beta，经 npm 或 zip 安装，需 Node 20+ 与 FFmpeg；语音识别为可选 whisper.cpp 本地安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 同一引擎同时服务人工时间线与代理工具（MCP/HTTP/OpenAPI/CLI）
- 代理接入路径含 Claude Code 插件、Codex、OpenAI API、n8n 等
- 本地作曲引擎与本地语音识别，无样本、无联网
- 分段缓存渲染：修改后仅重渲染变更片段

## 适用场景

- 让 Claude Code 等 AI 代理通过 MCP 工具自动剪辑素材并出片
- 长视频切条、加字幕并按 TikTok/Shorts 等平台格式输出
- 游戏开发者本地制作预告片且素材不离开本机

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L13: A **local-first video editor** for creators, game developers and their agents. One engine with a
> L14: pro timeline for people and the same 59 tools for agents (MCP, HTTP/OpenAPI, CLI). Your footage never
> L101: **For agents** — see **AGENTS.md**, setup for Claude, Cursor, OpenAI Codex, the OpenAI API, n8n and others in

## 星数曲线

```mermaid
xychart-beta
    title "laaielichter/Ai-edit-studio 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-20", "2026-11-23"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-23 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `81e8b9dc9627` · [字段定义](../../DATASET.md)*
