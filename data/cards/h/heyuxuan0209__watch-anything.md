# heyuxuan0209/watch-anything

⭐ 25 · JavaScript · MIT · 推送 2026-08-16 · [GitHub](https://github.com/heyuxuan0209/watch-anything) · 个人维护 · 中文 README

**丢视频链接给 AI agent，产出中文卡片式视频解读与全文中译**

面向 Claude Code / Codex / Cursor 等编码 agent 的技能包：用户丢入 X / YouTube / B站视频链接，agent 抓取内容、在无字幕时经降级链转写音频（平台字幕 → Groq 云端 whisper → 本地 faster-whisper），再按模板生成三层中文产出（卡片摘要 + 深度解读 + 全文中译），以 markdown 落地到本地知识库并可追问。支持 8 种解读模板、Feishu 推送集成，以及一键入队的浏览器扩展触发器。限制：不解析画面内容，仅覆盖'说了什么'。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无字幕视频的三级转写降级链（字幕→Groq whisper→本地 faster-whisper）
- 三层输出：卡片/深读/全文中译，8 种可选模板可自行增改
- 核心逻辑在 PLAYBOOK.md + scripts/，不依赖 Claude 专属特性，适配多种 agent
- 可选 Feishu 群卡片与云文档推送集成

## 适用场景

- 收藏了没时间看的英文技术演讲/视频，几分钟拿到中文卡片判断是否值得看
- 无字幕的 B站/长视频自动转写并生成中文解读
- 播客/访谈按发言人拆分解读，沉淀为自己的 markdown 知识库

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L30: watch-anything is a **Claude Code / Agent skill**: drop in a video link, it first fetches the
> L31: content, transcribes the audio track into text (if there are no captions), then has your AI produce
> L49: Video captions (fast, accurate)  →  Groq cloud whisper (tens of seconds, nearly free)  →  local faster-whisper (zer

## 星数曲线

```mermaid
xychart-beta
    title "heyuxuan0209/watch-anything 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `e2a40bb5c5ac` · [字段定义](../../DATASET.md)*
