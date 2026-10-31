# AbdulRehman393/youtube-qa-assistant

⭐ 19 · Python · MIT · 推送 2026-09-25 · [GitHub](https://github.com/AbdulRehman393/youtube-qa-assistant) · 个人维护

**对 YouTube 视频字幕做问答、摘要与语义搜索的 RAG 应用**

Streamlit 网页应用：粘贴 YouTube 链接后抓取视频字幕（含自动生成字幕，多语言回退），切分为重叠文本块并用 HuggingFace MiniLM 嵌入，存入 ChromaDB 向量库；提问时检索 top-k 相关片段，经 OpenRouter 网关调用 LLM（默认 Gemini，可选 GPT/Claude/Llama 等）仅基于字幕上下文作答。另提供自动摘要、要点提取、主题发现。限制：仅适用于有字幕的公开视频，无字幕时处理失败；换视频时向量库重建。本地运行需配置 OpenRouter API key。

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

- 字幕抽取→分块→MiniLM 嵌入→ChromaDB→检索的 RAG 流水线
- LLM 仅基于检索到的字幕片段作答
- 支持多语言字幕（英语/乌尔都语/印地语/阿拉伯语等回退）
- 侧栏可切换 OpenRouter 上的多种模型

## 适用场景

- 向长视频提问而不用完整观看
- 快速获得视频摘要与要点清单
- 在视频内容中做语义搜索定位片段

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L25: **YouTube URL → Transcript Extraction → Chunking → Embeddings → Chroma Vector DB → Retrieval → LLM Answer**
> L40: - **OpenRouter** — LLM provider gateway (Gemini / GPT / Claude / Llama / etc.)

## 星数曲线

```mermaid
xychart-beta
    title "AbdulRehman393/youtube-qa-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c7884ea93202` · [字段定义](../../DATASET.md)*
