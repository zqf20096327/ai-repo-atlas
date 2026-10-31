# omarTBakr/notebookllm-minus

⭐ 14 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/omarTBakr/notebookllm-minus) · 个人维护

**本地优先的开源 NotebookLM 替代：带精确引用的文档问答**

基于 FastAPI 的 RAG 应用：添加 PDF、文章、YouTube 视频、公开 Google Sheet 或 CSV/XLSX 作为来源，问答回答附引用并可定位到页、视频时刻或表格行；另生成思维导图、闪卡和测验并各自打开出处。UI 支持英语与阿拉伯语，针对阿拉伯语文本提供模型修复与可选 OCR。生成、嵌入、文档库、向量库后端均可从 .env 切换，可用本地 Ollama 离线运行，也支持 OpenRouter、OpenAI、Anthropic、Google、NVIDIA、Cohere。通过 Docker Compose 或 uv 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 引用可打开 PDF 页并高亮、视频定位到时刻、表格定位到行
- 表格按行分块，引用格式如 Sheet1 · row 12
- 阿拉伯语文本抽取损伤的模型修复流程与可选 qalam/Tesseract OCR
- 生成/嵌入/文档库/向量库后端均可从 .env 切换，支持本地 Ollama 离线运行

## 适用场景

- 把自己的 PDF、文章、视频放进笔记本做带出处的问答
- 学习时生成闪卡、测验和思维导图并核对其来源
- 阿拉伯语文档的检索与问答
- 不依赖云端 API、用本地 Ollama 离线运行整套问答栈

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L13: Add documents or links (PDFs, articles, YouTube videos, public Google Sheets), ask questions, get
> L18: store — and the whole stack runs **offline against a local Ollama** if you want it to. Models

## 星数曲线

```mermaid
xychart-beta
    title "omarTBakr/notebookllm-minus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `23a251e55c7e` · [字段定义](../../DATASET.md)*
