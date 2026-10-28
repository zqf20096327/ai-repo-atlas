# maim010/openclaw-video-vision

⭐ 20 · JavaScript · MIT · 推送 2026-03-23 · [GitHub](https://github.com/maim010/openclaw-video-vision) · [官网](https://maim010.github.io/openclaw-video-vision/) · 个人维护 · 中文 README

**给 AI agent 用户的视频理解技能：URL 进、结构化摘要出**

作为 OpenClaw 技能运行的视频理解工具：输入 YouTube、Bilibili 或任意含视频页面的 URL，经 yt-dlp+FFmpeg 或 Playwright 浏览器（支持 Browserless/Browserbase/Steel 云浏览器）提取关键帧，可选本地 whisper.cpp 转录音频，再通过任意 OpenAI 兼容视觉端点（GPT-4o、Claude、Gemini、本地模型）生成带时间戳、关键时刻与话题标签的结构化摘要。以 npm 包（GitHub Packages）安装，依赖 Node.js >= 18、FFmpeg 与视觉 API key；支持代理、Cookies 登录受限内容；低配置机器可跳过转录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- yt-dlp+FFmpeg 与 Playwright 双提取路径，自动回退，支持三家云浏览器
- 任意 OpenAI 兼容视觉端点（GPT-4o/Claude/Gemini/本地模型）
- 本地 whisper.cpp 音频转录并注入视觉提示词
- 低资源模式：CPU 少于 12 核或内存少于 14GB 时可关闭转录

## 适用场景

- 让我的 OpenClaw agent 直接总结 YouTube/Bilibili 视频并给出可跳转的时间戳
- 看不懂外语教程视频时获取结构化中文摘要
- 在服务器或低配机器上批量提取视频要点

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L5: Give it a URL — YouTube, Bilibili, or any page with a video — and get back a structured summary with key moments, ti
> L99: |**Vision AI**|Any OpenAI-compatible endpoint — GPT-4o, Claude, Gemini, local models|

## 星数曲线

```mermaid
xychart-beta
    title "maim010/openclaw-video-vision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `b1ed389e9846` · [字段定义](../../DATASET.md)*
