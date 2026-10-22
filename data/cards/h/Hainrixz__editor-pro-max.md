# Hainrixz/editor-pro-max

⭐ 275 · TypeScript · NOASSERTION · 推送 2026-03-26 · [GitHub](https://github.com/Hainrixz/editor-pro-max) · [官网](https://www.tododeia.com) · 个人维护

**用自然语言让 Claude Code 生成视频的本地视频编辑器**

基于 Remotion + Claude Code 的视频创作工具：用户以自然语言描述需求，Claude Code 编写 React 合成代码，由 Remotion 本地渲染为 MP4。提供 25 个组件、10 个模板（TikTok/YouTube/演示等）、7 个 AI 技能与 5 个流水线脚本（含 Whisper.cpp 词级字幕转录、静音检测、背景移除）。全程本地运行，无需 API key。要求 Node.js 20+ 与 Claude Code CLI，无图形界面，面向熟悉命令行的内容创作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言驱动：Claude Code 编写合成代码，Remotion 渲染 MP4
- 25 个组件、10 个平台模板、9 种平台尺寸预设
- Whisper.cpp 本地词级字幕转录与静音检测流水线
- 无需 API key，全部本地运行

## 适用场景

- 用一句话生成 TikTok/YouTube 短视频或幻灯片
- 给口播视频自动加字幕、剪掉静音段
- 将素材自动剪辑并按平台尺寸导出 MP4

## 场景标签

`视频生成` `语音识别` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L15: Editor Pro Max turns Claude Code into a professional video editor. Instead of dragging clips on a timeline, you des
> L61: "Make me a TikTok"  ──>  Writes React composition  ──>  Renders to MP4
> L78:  - `npx tsx scripts/transcribe.ts` — Whisper AI generates word-level captions

## 星数曲线

```mermaid
xychart-beta
    title "Hainrixz/editor-pro-max 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 272 --> 275
    line [273, 274, 274]
```

2026-10-18 273 → 2026-10-22 274（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `90c853073c54` · [字段定义](../../DATASET.md)*
