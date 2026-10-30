# chusimin/vibe-motion-video

⭐ 15 · JavaScript · Apache-2.0 · 推送 2026-06-08 · [GitHub](https://github.com/chusimin/vibe-motion-video) · 个人维护 · 中文 README

**给 Claude Code 的自动出片 skill：AI 写分镜，Remotion 渲染视频**

一个面向 Claude Code / Codex 的 AI Agent skill，把链接、视频、代码目录、文章或一句话想法自动转化为成片视频。创意侧由 AI 产出渲染器无关的 JSON 中间表示（brief/config/分镜表），机械侧由 vibemotion CLI 完成抓取转写、TTS 与词级时间戳对齐、Remotion 按 15s 分段渲染、ffmpeg 合成与响度归一、ffprobe 体检和导出；③概念④分镜⑥渲染三道审批门需人工确认。依赖 Node 18+ 与 ffmpeg，可选 yt-dlp、whisper-cli 与 TTS key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 步流水线（ingest→export），③④⑥ 三道人工审批门
- AI 写 JSON 中间表示，CLI（Remotion+ffmpeg）确定性渲染
- 类型×风格×平台×时长正交维度，Resolver 合并为 RenderSpec
- 字幕来自真实配音时间戳，素材只用真实文件不编占位

## 适用场景

- 把产品链接或代码目录自动做成 showreel 宣传片
- 把文章或想法转成知识科普/口播视频
- 改文案或时长后只重渲受影响的 15s 分段

## 场景标签

`视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L19: `vibe-motion-video` 是一个 **AI Agent skill**（给 Claude Code / Codex 用），把"做视频"这件事拆成两半：
> L10: 创意由 AI 写 JSON，机械活交给 `vibemotion` CLI（Remotion 渲染）。

## 星数曲线

```mermaid
xychart-beta
    title "chusimin/vibe-motion-video 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `266be2b31f00` · [字段定义](../../DATASET.md)*
