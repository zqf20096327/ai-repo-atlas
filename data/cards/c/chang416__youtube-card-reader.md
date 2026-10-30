# chang416/youtube-card-reader

⭐ 31 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/chang416/youtube-card-reader) · 个人维护 · 中文 README

**本机阅读工具：把 YouTube 影片与文章整理成带时间戳的知识卡并可产出实作档案**

local-first 的开源阅读工具：贴上 YouTube 影片或网页文章，整理成可翻阅的知识卡，卡片保留时间戳可跳回原片段，并支持针对整支影片问答、单卡深入解析与写入 Obsidian vault。转录采用字幕→Gemini 深视觉→本机 Whisper 的降级链。新版加入「把它做出來」流程：侦测本机 Codex CLI 或 Claude Code，将整支影片交给 coding agent，在本机产出可跑的专案、操作引导 guide.html、教学 study.html 或练习题库 drill.html；也可走纯 API 单次生成（标示为未查证）。无账号系统、遥测或自有后端。需 Python 3.10+ 与 Node.js 18+，脚本启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 知识卡保留时间戳与原话，点击可跳回影片对应位置
- 字幕→深视觉→本机 Whisper 的三级转录降级链
- 交给本机 Codex CLI／Claude Code 产出专案、引导页、教学页或题库四类实体档案
- 免金钥可用 OpenCode Zen 免费模型整理有字幕影片

## 适用场景

- 把教学影片整理成可翻阅、可跳转的笔记卡片
- 从教学影片直接生成本机专案、操作引导或练习题库
- 将精选卡片存入 Obsidian 做知识管理

## 场景标签

`知识库管理` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: YouTube Card Reader 是一個在本機執行的開源閱讀工具。貼上 YouTube 影片或文章，它會整理成可以翻閱的知識卡；YouTube 卡片保留時間戳，點一下就能跳回原片段。
> L44: - **讀得到畫面**：開啟「深視覺」後，Gemini 會讀取投影片、白板與畫面中的程式碼；若同時有字幕，語音時間軸仍以字幕為準。
> L194: YouTube Card Reader is a local-first, open-source reader that turns YouTube videos and web articles into navigable

## 星数曲线

```mermaid
xychart-beta
    title "chang416/youtube-card-reader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `146d5cc878bb` · [字段定义](../../DATASET.md)*
