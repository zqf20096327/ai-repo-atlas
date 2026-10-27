# msmahdinejad/SourceLens

⭐ 39 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/msmahdinejad/SourceLens) · 个人维护

**自托管多语言循证研究工作台：文献转对话、播客、幻灯片与视频**

面向希望保留证据可溯性的研究者与写作者的自托管研究工作台：用户导入 PDF、文本、图像、音视频、笔记与网页，系统经自适应抽取（含选择性 OCR 与视觉分析）建立分页感知索引，采用 Chroma 向量检索与 SQLite FTS5 融合的 agentic RAG 提供带引文的对话；Studio 提供 13 种工作流，生成可编辑 PowerPoint、有声播客、视频概览、报告、闪卡等产物。界面支持英语与波斯语 RTL。本地数据全部留在主机。安装包/CLI 名为 paperlens，需 Python 3.12、uv、Node 20+ 与 FFmpeg，通过 API key 接入 Gemini/Groq/Mistral 等外部模型服务。本地版不含认证、HTTPS 等部署保障，需自行承担。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Chroma 向量检索与 SQLite FTS5 混合融合，支持英语/波斯语
- agentic RAG：模型可规划多次检索、选过滤器与证据预算
- Studio 13 种工作流生成播客、可编辑 PowerPoint、视频概览、报告等
- 本地优先：工作区、索引、对话与产物留存主机

## 适用场景

- 研究者把文献建成带引文的知识工作区并提问
- 把资料转成播客、幻灯片、视频等可交付格式
- 以波斯语/英语双语界面开展循证研究

## 场景标签

`科研工具` `文档问答` `视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L16: SourceLens is a self-hosted research workspace for people who want the convenience of an AI
> L27: |Grounded conversation|Source selection, page and segment citations, an evidence drawer, and explicit abstention wh
> L28: |Agentic RAG|The model can plan multiple searches, choose filters and evidence budgets, and repair invalid tool cal

## 星数曲线

```mermaid
xychart-beta
    title "msmahdinejad/SourceLens 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4441c0e974de` · [字段定义](../../DATASET.md)*
