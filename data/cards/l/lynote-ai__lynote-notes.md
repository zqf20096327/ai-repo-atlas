# lynote-ai/lynote-notes

⭐ 13 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/lynote-ai/lynote-notes) · 组织维护 · 中文 README

**本地优先的双语 AI 笔记工具：把文档音视频转成可溯源笔记**

面向个人用户的本地优先 AI 笔记应用（CLI 与 Python API）：将 Markdown、PDF、DOCX、网页、YouTube 字幕、音视频等来源切分为可检索 chunk，生成结构化笔记（Overview/Key points/Open questions），每条要点附来源引用，音视频带时间戳；另提供带引用的问答、Markdown 与 Anki TSV 导出。默认内置抽取式 provider，零依赖、离线运行；可选接入任意 OpenAI 兼容 LLM（Ollama、vLLM 等）生成更流畅笔记，失败时自动回退抽取式。英文与中文分词（CJK 一元+二元）。检索为 BM25 词法匹配，嵌入检索在路线图中；不支持实时会议采集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条笔记要点默认附带指向源 chunk 的引用（音视频含时间戳）
- 默认抽取式 provider 零依赖离线运行，可回退
- 可接入任意 OpenAI 兼容端点（Ollama/vLLM/OpenAI）
- 中英双语分词，支持 Anki TSV 导出

## 适用场景

- 把讲义、论文、视频整理成可核查引用的结构化笔记
- 对自己的资料库做带出处的问答
- 将笔记导出为 Anki 卡片用于记忆复习

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **Source-grounded, bilingual, local-first AI note taker.** Turn documents, web
> L4: pages, recordings, videos and YouTube links into structured notes where every
> L5: bullet cites the exact source chunk it came from — so you can verify, edit and
> L39: - **Source-grounded Q&A**: ask questions, get answers with references to the

## 星数曲线

```mermaid
xychart-beta
    title "lynote-ai/lynote-notes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `fa8bb032454f` · [字段定义](../../DATASET.md)*
