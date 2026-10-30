# Erick-Bryan-Cubas/green-deck

⭐ 15 · Vue · MIT · 推送 2026-08-25 · [GitHub](https://github.com/Erick-Bryan-Cubas/green-deck) · 个人维护 · 中文 README

**面向 Anki 用户的 AI 抽认卡生成器：从文本/文档自动生成卡片**

开源 Web 应用（FastAPI + Vue 3 + DuckDB），用 LLM 从粘贴文本或文档（PDF/Office/图片 OCR，经 Docling 提取）生成 Basic 与 Cloze 抽认卡，经来源校验、相关性过滤、质量评分、语言检测多阶段管线后，通过 AnkiConnect 直接同步到 Anki 牌组。支持 Ollama 本地模型（默认 qwen-flashcard + nomic-embed-text）及 OpenAI/Perplexity 云端 API，可完全离线运行。提供 Docker Compose 部署（含可选 Ollama 容器）与本地开发流程。

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

- LLM 生成 Basic/Cloze 卡片，多阶段质量管线（来源校验/相关性/评分/语言检测）
- 多 LLM 提供方：Ollama 本地、OpenAI、Perplexity
- Docling 多格式文档提取（PDF/Office/HTML/Markdown/图片 OCR）
- 经 AnkiConnect 直连 Anki：添加/更新/迁移/翻译卡片

## 适用场景

- 把讲义或 PDF 一键转成 Anki 抽认卡
- 离线用本地 Ollama 模型生成学习卡片
- 对已有卡片做 AI 改写（压缩/简化/拆分）或翻译

## 场景标签

 · 领域:教育/学习工具

## 证据(README 行号)

> L28: Green Deck is an open-source AI-powered flashcard generator that automatically creates high-quality study cards fro
> L34: - **Local-First**: Run entirely offline with Ollama, or use cloud providers (OpenAI, Perplexity)

## 星数曲线

```mermaid
xychart-beta
    title "Erick-Bryan-Cubas/green-deck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3a68400d79d4` · [字段定义](../../DATASET.md)*
