# diegovasquez-ai/claude-reels-studio

⭐ — · [GitHub]() · 个人维护

**给内容创作者的 reels 自动化工作室：转录、按个人风格剪辑、发布与 DM 自动交付**

基于 Claude Code 与 Remotion 的 reels 制作流水线：用户上传手机拍摄的竖版视频，系统用 Whisper 转录（可本地或经 OpenRouter）、按 `/configurar` 从历史 reels 学习的个人风格指南进行剪辑、生成字幕与封面、用 Claude + Drive 产出赠品 PDF，并通过 Zernio 发布到 Instagram/YouTube、对评论关键词自动回复 DM 交付资源。用户在本地 Estudio 界面确认文本与草稿后批准发布。要求 Claude Code（Pro/Max 或 API）、Node.js 20+、FFmpeg、Chrome、Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从用户已有 reels 学习风格并逐次累积修正的风格指南机制
- 转录文本先经用户确认、术语进 glossary 再剪辑
- 评论关键词→自动 DM 交付资源的完整发布链路
- 可选 Higgsfield MCP：生成 B-roll、封面、留.analysis 预测与多语言配音

## 适用场景

- 单人创作者把录好的视频一键生成成片并发布到 Instagram 和 YouTube
- 用关键词评论自动给粉丝 DM 发送 PDF 指南
- 只需字幕或单条剪辑时用 `/subtitulos`、`/editar-clip` 单独处理

## 场景标签

`语音识别` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Grabas un reel con el celular. Claude Code hace el resto:**
> L20: - **Aprende TU estilo.** Con `/configurar`, Claude analiza los reels que te funcionaron y escribe tu guía de estilo

## 星数曲线

```mermaid
xychart-beta
    title "diegovasquez-ai/claude-reels-studio 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-25 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `1a1b7b052bd0` · [字段定义](../../DATASET.md)*
