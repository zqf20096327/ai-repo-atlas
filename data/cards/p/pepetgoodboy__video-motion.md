# pepetgoodboy/video-motion

⭐ 3 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/pepetgoodboy/video-motion) · 个人维护

**把 markdown brief 渲染成 9:16 竖屏短视频的 agent 流水线**

由 markdown 说明与 shell 命令组成的短视频生成流水线：从一份 brief .md 出发，经 HyperFrames 以 HTML+CSS+GSAP 时间线排版动画，再渲染为 1080×1920@60fps 的 H.264+AAC MP4。要求 Node ≥22、ffmpeg 与 Chromium，由 Claude Code、Codex CLI、Gemini CLI 等任意编码 agent 驱动执行。强制每个 brief 声明 21 类视觉类型之一并按 STYLE-LEDGER 轮换；voiceover、BGM 依赖 Cartesia/HeyGen/Gemini 可选 API key，无 key 也可运行无声模式。示例 brief 随仓库提交，渲染结果不入库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- brief .md → HyperFrames(HTML+GSAP) → MP4 的全自动渲染管线，无需时间线编辑器
- 强制 V1–V21 视觉类型声明与 STYLE-LEDGER 轮换规则避免重复风格
- 多个 QA 工具：naskah-check 文案门禁、qa-video MP4 规格门禁、qa-variety 防单调门禁
- Cartesia 印尼语多角色 TTS、HeyGen 音乐目录，无 key 时走本地 MusicGen/无声路径

## 适用场景

- 给 Reels/TikTok 批量产出无脸科普竖屏视频
- 只写 markdown brief 让编码 agent 代为生成动画短片
- 没有配音 API 时生成纯字幕+BGM+音效的短视频

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L13: > **English TL;DR** — A brief-markdown → vertical-video pipeline. HyperFrames renders HTML+GSAP
> L72: |**Agent / LLM**|wajib|Claude Code, Codex CLI, Gemini CLI, OpenCode, atau model murah lain — lihat §6|
> L16: > markdown instructions plus shell commands.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `169d80836ef1` · [字段定义](../../DATASET.md)*
