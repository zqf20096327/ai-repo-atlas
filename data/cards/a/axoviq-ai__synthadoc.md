# axoviq-ai/synthadoc

⭐ 2,003 · Python · AGPL-3.0 · 推送 2026-11-23 · [GitHub](https://github.com/axoviq-ai/synthadoc) · [官网](https://axoviq.com/resources/synthadoc) · 组织维护

**把原始文档编译为本地结构化 wiki 的 LLM 知识引擎**

Synthadoc 读取 PDF、表格、PPT、网页、图片、视频、Word、TXT 与 AI 会话记录等源文档，在摄取阶段用 LLM 将其合成为持久化的结构化 wiki：自动构建交叉引用、检测矛盾、标记孤儿页，每条声明带 ^[file:L-L] 行级引用，输出为本地 Markdown，可在 Obsidian 或任何 wiki 生态中打开。内置审计日志（audit.db）、成本软警告/硬阈值、三层缓存、九个对话式维护工作流（预览 diff、确认后写入、可回滚）、REST API 与 12 工具 MCP server。面向个人、小团队与企业；AGPL-3.0 许可，本地优先、仅绑定 localhost。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 摄取时编译：新来源丰富并交叉链接整个语料，而非追加 chunk
- 每条声明带 ^[file:L-L] 行级引用，支持按引用行核验
- 九个对话式维护工作流：矛盾/孤儿/断链/内容健康解析，可回滚
- 不可变 audit.db 审计日志记录每次摄取、查询与成本事件

## 适用场景

- 把研究资料和文档积累成可维护的个人 wiki
- 搭建需要本地留存和审计的部门知识库
- 跨多个 wiki 做一次提问并得到带出处的回答

## 场景标签

`知识库管理` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L27: **An LLM wiki you can trust and operate: compiled at ingest, cited to the source line, governed by an audit trail a
> L33: Synthadoc reads your raw source documents — PDFs, spreadsheets, PPTs, web pages, images, videos, Word files, TXTs, 
> L109: |Provider choice|LLM backends including free-tier Gemini and Groq, paid Anthropic/OpenAI/DeepSeek/MiniMax/Qwen (Da

## 星数曲线

```mermaid
xychart-beta
    title "axoviq-ai/synthadoc 星数(近 24 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25"]
    y-axis "stars" 1521 --> 2079
    line [1594, 1595, 1567, 1568, 1574, 1577, 1578, 1615, 1650, 1688, 1725, 1567, 1957, 1997, 2018, 2031, 2030, 2031, 2032, 2033, 2002, 1999, 2001, 2003]
```

2026-10-23 1,594 → 2026-11-25 2,003（+409）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `85c24f7ea735` · [字段定义](../../DATASET.md)*
