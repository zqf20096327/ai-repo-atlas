# Kanvis-chen/kanvis-video

⭐ 51 · TypeScript · MIT · 推送 2026-08-12 · [GitHub](https://github.com/Kanvis-chen/kanvis-video) · [官网](https://kanvis-chen.github.io/kanvis-homepage/open/?tab=workbench) · 个人维护 · 中文 README

**把中文长文重新导演成可发布视频的 Codex Skill 流水线**

MIT 开源的 Codex 编排 Skill 与本地 Kanvis Studio 基础工作台：首个工作流 kanvis-article-to-video 从中文长文、公众号文章、Markdown 出发，执行原文保真、口播改写、语义分镜、信息图、字幕、多语种配音、渲染与发布门禁，支持真人增强/无人出镜/数字分身三种生产模式。声音与数字人环节通过可替换适配器接入 HeyGen、ElevenLabs、MiniMax 或本地 CosyVoice，付费动作受 off/confirm/auto 策略与成本上限控制。需 Codex 兼容环境、Node.js 20+、ffmpeg/ffprobe，渲染需 HyperFrames。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文章到视频的完整流水线：改写、语义分镜、信息图、字幕、发布质检
- 供应商可替换适配器（HeyGen/ElevenLabs/MiniMax/本地 CosyVoice）
- off/confirm/auto 三种付费策略 + 成本上限 + 任务缓存，默认禁用隐式付费触发
- 内置 Kanvis Studio 基础工作台：可视化画布、多轨时间轴、本地渲染

## 适用场景

- 把公众号文章或课程稿批量转成有画面结构的视频
- 内容团队对成片做分辨率、时长、授权与人工审核的发布门禁
- 在本地工作台检查并微调 Agent 生成的视频项目

## 场景标签

`工作流自动化` `视频生成` `语音合成` · 领域:效率与自动化

## 证据(README 行号)

> L25: Kanvis Video 是 Kanvis System 中开源的视频制作能力层：用 Codex Skill 把长文、课程稿和知识库内容变成可导演、可检查、可发布的视频项目，再交给 Kanvis Studio 本地检查和编辑。
> L27: 当前内置的首个 workflow 是 `kanvis-article-to-video`：从原文保真、口播改写和语义分镜，到真人增强、无人出镜、数字分身、信息图、字幕、多语种配音路径、音频、渲染与发布门禁。
> L47: 普通数字人工具通常从“已有脚本”开始，最终输出一段人物口播。Kanvis Video 从文章开始，先判断讲什么、怎么讲、什么时候应该让数字人退到画面一角，再把内容编排成可检查、可恢复、可替换供应商的视频项目。

## 星数曲线

```mermaid
xychart-beta
    title "Kanvis-chen/kanvis-video 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1495b48c5f67` · [字段定义](../../DATASET.md)*
