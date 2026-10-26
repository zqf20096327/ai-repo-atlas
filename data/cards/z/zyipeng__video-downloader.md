# zyipeng/video-downloader

⭐ 27 · Shell · MIT · 推送 2026-06-02 · [GitHub](https://github.com/zyipeng/video-downloader) · 个人维护 · 中文 README

**让 AI Agent 从 9 个视频平台下载视频的通用 Skill**

面向 Codex、Claude Code、Cursor、Cline 等 Agent 的视频下载技能：本体为 SKILL.md 与若干 bash 脚本，基于 yt-dlp，对抖音、快手提供自研 SSR 分享页解析器作为 yt-dlp 失效时的替代后端。支持解析后选档，提供质量/速度/兼容三档画质策略，aria2c 16 路并行加速，macOS 下 Chrome cookies 一次导出后 24 小时复用以避免钥匙串反复弹窗。脚本也可脱离 AI 直接运行；依赖 yt-dlp、ffmpeg、aria2 需自行安装；不处理 DRM 与付费内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 YouTube/B站/抖音/小红书/快手/微博/Twitter/Vimeo/TikTok 9 个平台
- 抖音/快手走自研 SSR 分享页解析器，不依赖内置 extractor
- 三档画质策略（最高 4K/8K AV1、≤480p、1080p H.264 兼容档）
- aria2c 16 路并行分片下载与 macOS cookies 24 小时缓存

## 适用场景

- 让 Claude Code/Cursor 等 AI 助手按对话指令下载视频并选画质
- 先解析视频档位与大小再决定下载哪一档
- 在 macOS 上下载 B 站/小红书等需登录态的视频且避免反复弹钥匙串

## 场景标签

 · 领域:工具/AI Agent 技能

## 证据(README 行号)

> L3: > 一个**通用的 AI Agent Skill**，让 AI 助手帮你从 9 个主流视频平台下载视频到本地。基于 `yt-dlp` + 自研脚本，主打 **解析后选档**、**画质透明**、**多线程加速**。
> L5: > ✅ **跨平台 Agent 通用**：兼容 Codex、Claude Code、Cursor、Cline、以及任何支持 Markdown skill 加载的 AI Agent。本质上只是一个 `SKILL.md` + 几个 ba
> L31: # Cursor / Cline / Codex / 其他 — 放到该 Agent 的 skills 或 knowledge 目录即可

## 星数曲线

```mermaid
xychart-beta
    title "zyipeng/video-downloader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d70835c7586e` · [字段定义](../../DATASET.md)*
