# MakiDevelop/VirtualMe

⭐ 28 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/MakiDevelop/VirtualMe) · 个人维护 · 中文 README

**把一個人萃取成 AI 代理人：8 週治療師式訪談取代填表**

以 therapist-style 深度訪談（8 週 × 30 分鐘，R1–R5 追問規則 + 三角校驗）從受訪者萃取人格，產出 8 個本地 markdown 檔（SOUL/VOICE/SKILL/PEOPLE/HISTORY/JOURNAL/BOUNDARIES/STATE），可餵給任何 LLM 使用。訪談對話不出本機，記憶預設 SQLite，可搭配 memory-hall（SQLite + sqlite-vec + Ollama）做反思層。基於 Stanford arXiv:2411.10109 訪談式萃取研究，需求 Python 3.11+ 與 Anthropic API key，提供 LINE dogfood 與本機 export/blind test 流程；明言非 chatbot 平台、非 fine-tune、所有外送訊息需人工 review，公開倉部分功能（L3/L4、語音蒐集）屬 roadmap 未實作。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 週多輪訪談萃取，R1–R5 追問與三角校驗機制
- 產出 8 個自擁有的 persona markdown 檔 + manifest
- 四層 memory 架構，預設 SQLite 零依賴，可搭配 memory-hall
- Week 5 / Week 8 盲評 gate 與 draft→review→ship 流程

## 适用场景

- 花 8 週被訪談萃取出自己的 AI 人格檔案
- 用自己的語氣起草訊息並由本人審核後發送
- 技術人員為非技術親友代跑萃取 pipeline

## 场景标签

`提示工程` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L64: - Bot 每次問一題，等你完整回答，**追問 rationale**
> L99: - **Raw archive**：`python -m virtualme.export` 產生 8 個 dimension markdown、入口檔與 manifest。
> L118: - ❌ 這不是 chatbot 平台。是「萃取你」的 pipeline，產出檔案後你可以餵給任何 LLM。

## 星数曲线

```mermaid
xychart-beta
    title "MakiDevelop/VirtualMe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `371fb6889011` · [字段定义](../../DATASET.md)*
