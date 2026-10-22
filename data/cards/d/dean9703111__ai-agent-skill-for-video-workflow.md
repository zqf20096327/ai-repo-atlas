# dean9703111/ai-agent-skill-for-video-workflow

⭐ 220 · Python · 推送 2026-01-28 · [GitHub](https://github.com/dean9703111/ai-agent-skill-for-video-workflow) · [官网](https://youtu.be/xe00zJEtuMo) · 个人维护 · 中文 README

**影片字幕处理 AI Agent Skills 集合：转字幕、优化、字卡、社群摘要**

面向 AI Agent（如 Cursor/Antigravity 类编码代理）的字幕处理技能集合，含 4 个 skill：音訊轉 SRT（Python + Whisper API，可自訂每行字數上限、自動合併短間隔）、比對 origin.md 原稿優化字幕、在字幕中按四種類型標註參考字卡、依平台（Facebook/Thread/YouTube）生成社群貼文摘要，並提供 /gen-video-srt-card-des 指令依序執行全部步驟。以技能目錄（.agent/skills/）形式提供，需搭配支援 Agent Skills 的代理環境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 個字幕處理 skill 覆蓋轉檔、優化、字卡、摘要全流程
- 单一指令 /gen-video-srt-card-des 依序執行全部步驟
- 字幕優化與字卡標註依賴 AI 判斷，音訊轉字幕用 Python + Whisper API
- 字卡分金色重點/白色提醒/紅色警告/藍色列點四類型

## 适用场景

- 为影片制作流程自動生成與優化 SRT 字幕
- 在字幕中加入分類參考字卡提升資訊傳達
- 從字幕一键生成多平台社群貼文

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: 這是一個專為影片字幕處理設計的 AI Agent Skills 集合，提供從音訊轉字幕、優化字幕、設計字卡到生成社群媒體摘要的完整工作流程。
> L112: .agent/

## 星数曲线

```mermaid
xychart-beta
    title "dean9703111/ai-agent-skill-for-video-workflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 218 --> 221
    line [219, 220]
```

2026-10-18 219 → 2026-10-22 220（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a8be1922322e` · [字段定义](../../DATASET.md)*
