# wangxin6x/AutoVideo-Agent

⭐ 90 · Python · MIT · 推送 2026-08-26 · [GitHub](https://github.com/wangxin6x/AutoVideo-Agent) · 个人维护 · 中文 README

**给编码 Agent 用的 Markdown 转视频流水线工具**

将 Markdown 脚本解析为分镜、场景清单、占位素材、时间线，经 FFmpeg 渲染输出 MP4 并生成 QA 报告。v0.1 本地优先且确定性：无需 API key 或云账号，生成可检视的占位场景卡与静音音频；无 FFmpeg 时优雅降级保留素材与报告。面向 Codex、Claude Code、Gemini CLI 等编码 Agent 工作流，提供 AGENTS.md 与 SKILL.md 集成。ComfyUI 媒体 provider 已实现但未经实机验证，MiniMax 等托管 provider 为规划项。运行时无第三方依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Markdown→分镜→场景清单→时间线→FFmpeg→QA 报告的确定性流水线
- 无需 API key/云账号的本地优先占位素材渲染
- Codex Skill / AGENTS.md 集成供编码 Agent 调用
- ComfyUI API 媒体 provider（实验性）与 Mock/命令行 TTS、SRT 字幕

## 适用场景

- 编码 Agent 在仓库内将 Markdown 脚本一键转成视频并跑 QA
- 以确定性占位素材搭建可复现的视频流水线原型
- 通过 provider 扩展点接入 ComfyUI 或本地 TTS 生成媒体

## 场景标签

`视频生成` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: Built for Codex, Claude Code, Gemini CLI and other coding-agent workflows. v0.1 is local-first and deterministic: i
> L71: |✅ Available now|Codex Skill / AGENTS integration|AGENTS.md and skills/auto-video/SKILL.md|
> L108: > Turn examples/demo-script.md into a video and run QA. Use skills/auto-video/SKILL.md.

## 星数曲线

```mermaid
xychart-beta
    title "wangxin6x/AutoVideo-Agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-26"]
    y-axis "stars" 89 --> 92
    line [91, 90, 90]
```

2026-10-18 91 → 2026-10-26 90（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `5554edb02a95` · [字段定义](../../DATASET.md)*
