# perso-ai/perso-dubbing-plugin

⭐ 40 · JavaScript · MIT · 推送 2026-10-15 · [GitHub](https://github.com/perso-ai/perso-dubbing-plugin) · [官网](https://perso.ai/dubbing) · 组织维护

**供编程 Agent 使用的视频配音/字幕/剪辑技能插件**

面向 Claude Code、Cursor、Codex、Antigravity 等编程 Agent 的插件（Agent Skills）：通过对话指令调用 Perso Dubbing API 完成视频多语言配音、唇形同步、人声/伴奏分离、语音转字幕、字幕翻译与烧录、短视频剪辑。字幕样式烧录、SRT 翻译、按时间码剪辑在本地（ffmpeg）免费运行；配音、唇形同步、人声分离、STT 在 Perso 服务器按秒计费。需 Node.js 18+，支持 npx 或 skills.sh 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视频多语言配音与唇形同步（服务器端，按秒计费）
- 人声/背景分离，多人场景每人一轨
- 字幕本地免费处理：12 种样式烧录、SRT 翻译保留时间轴
- 支持文件、文件夹与 YouTube/TikTok URL 输入

## 适用场景

- 在编程 Agent 里一句话给视频配音成其他语言
- 给无字幕视频生成 SRT 并翻译成多种语言
- 从长视频按时间码或 AI 选段生成 9:16 竖屏短片

## 场景标签

`语音合成` `视频生成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L3: **Every video, every language. Dub, subtitle, and clip right from your coding agent.**
> L44: **Codex · Antigravity · anything else**: `npx perso-dubbing` detects your hosts and installs into each — or, cross-
> L84: **MIT, free and open-source.** Everything that runs on your machine costs nothing and needs no account: styling and

## 星数曲线

```mermaid
xychart-beta
    title "perso-ai/perso-dubbing-plugin 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-25 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8955491091f8` · [字段定义](../../DATASET.md)*
