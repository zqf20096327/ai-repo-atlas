# shihabcodes/Cogniflow_AI

⭐ 27 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/shihabcodes/Cogniflow_AI) · [官网](https://cogniflow-ai-eight.vercel.app) · 个人维护

**浏览器内 RAG 应用：对视频/播客/PDF 提问并给出带引用的回答**

基于 Next.js 15 与 Gemini 的浏览器端 RAG 应用：用户添加 YouTube 视频（转录带时间戳）、播客音频（Gemini 转录）、PDF（浏览器内解析不上传）或粘贴文本作为来源，切块与嵌入向量存于浏览器 IndexedDB；提问时做混合检索（向量+BM25，倒数排名融合），由 Gemini 生成回答，每条声明带 [n] 引用标签并可深链到视频精确秒数。无需账号，自带密钥即可使用；支持笔记本分类管理与流式回答。

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

- 四类来源：YouTube 时间戳转录、浏览器内 PDF 解析、Gemini 音频转录、粘贴文本
- 混合检索：段落感知切块 + 向量相似度 + BM25，以 RRF 融合
- 引用标签深链至视频精确秒数（&t=）
- 来源、切块与向量全部存于浏览器 IndexedDB，仅发送 top-6 片段给模型

## 适用场景

- 向长视频或播客提问并定位到具体时间点
- 在不上传 PDF 的前提下本地问答并引用原文
- 为不同主题维护多个来源集合（笔记本）

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **Retrieval-augmented generation (RAG), in your browser.** Add YouTube videos, podcasts, PDFs, or pasted notes as so
> L8: ask ──► embed question ──► cosine top-k ──► grounded Gemini answer ─┘
> L16: - **Cited answers** — the model must ground every claim in `[n]` citations; chips link to the source, and for YouTu

## 星数曲线

```mermaid
xychart-beta
    title "shihabcodes/Cogniflow_AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0700e01cb667` · [字段定义](../../DATASET.md)*
