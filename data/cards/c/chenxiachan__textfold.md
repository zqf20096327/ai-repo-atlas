# chenxiachan/textfold

⭐ 1,318 · Python · Apache-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/chenxiachan/textfold) · [官网](https://chenxiachan.github.io/textfold/) · 个人维护 · 中文 README

**本地运行的文献/网页五级折叠阅读器，逐级缩放原文**

桌面/本地 Web 应用，把论文、网页、文件和 AI 回复折叠成五个细节层级（全文→逐段要点→段落主旨→章节主线→主题地图），每个层级可缩放回作者原文。读取 arXiv、PubMed Central、bioRxiv 等链接和 PDF/Word/EPUB 等文件，支持逐句翻译、高亮笔记、提问与思维导图。文本保存在本机；折叠与提问由用户已有的模型或 API key 驱动，无需注册账号。提供 macOS/Windows 安装包、pip 包与浏览器扩展（Chrome/Edge/Brave）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五级折叠：每段在作者原句与 AI 概述之间逐级缩放，可回溯原文
- 支持 arXiv/PMC/bioRxiv/medRxiv/维基/GitHub 链接与 PDF/Word/EPUB/CSV 等文件
- 可接入 Claude Code、ChatGPT 订阅、OpenRouter 或多家 API key，含 Ollama 本地模型
- Zotero 文献库读取、Obsidian 笔记桥接、浏览器一键抓取当前页面

## 适用场景

- 分层阅读长论文，从主题地图逐级展开到原文
- 折叠 Claude Code/Pi 等 agent 的长回复，逐层查看要点
- 逐句翻译外文文献并保留公式排版
- 配合 Zotero 与 Obsidian 管理本地文献阅读流

## 场景标签

`科研工具` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5:  Fold it, instead of summarizing it. AI decides what each level leaves out. Every paragraph opens back to the author
> L32: |**3**|**Key**|its point and the reason for it|AI, resting on the Brief sentences|
> L106: Open `http://localhost:3017`. The first time, connect a model; then paste a link or drop a file, and pick a langua

## 星数曲线

```mermaid
xychart-beta
    title "chenxiachan/textfold 星数(近 28 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 314 --> 1409
    line [405, 430, 467, 516, 668, 732, 770, 787, 796, 819, 838, 857, 516, 959, 984, 1004, 1025, 1037, 1046, 1070, 1199, 1239, 1266, 1280, 1300, 1310, 1318, 1318]
```

2026-10-22 405 → 2026-11-24 1,318（+913）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `72ff5af4f753` · [字段定义](../../DATASET.md)*
