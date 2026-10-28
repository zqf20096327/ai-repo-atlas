# orzcls/PersonaLingo

⭐ 33 · Python · MIT · 推送 2026-06-18 · [GitHub](https://github.com/orzcls/PersonaLingo) · 个人维护

**面向雅思口语学习者的个性化语料库生成器（Agent 技能+后端）**

通过 LLM 生成个性化雅思口语语料库：7 阶段蒸馏管线（画像问卷→对话→深度研究→能力框架→Anchor/Bridge→词汇→模式模板），输出经 schema 校验的 corpus.json 与静态个人画像站点。提供两种交付方式：install-only 技能（npx 一行安装到 Claude/Cursor 等 agent，零后端）与可运行后端（FastAPI+Vue 3+SQLite，QMD 三层检索：查询扩展+BM25/TF-IDF 双通道+LLM 重排，不依赖向量库）。支持 OpenAI 与 Anthropic 双模型切换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 阶段蒸馏管线生成 schema 校验的 corpus.json 与静态站点
- QMD RAG：查询扩展+BM25/TF-IDF+RRF 融合+LLM 重排，无向量库依赖
- npx skills add 一行安装为 agent 技能，零后端运行
- 支持 OpenAI/Anthropic 双模型切换，按 6.0–7.5+ 分段差异化输出

## 适用场景

- 我想让 AI 根据我的个人经历定制雅思口语语料
- 把个性化语料库作为技能安装到 Claude/Cursor 等 agent 中使用
- 长期学习中通过对话维护和更新语料库

## 场景标签

 · 领域:语言学习/教育工具

## 证据(README 行号)

> L3: > AI-Powered Personalized IELTS Speaking Corpus Generator with RAG & Memory System
> L7: - **Smart Corpus Generation** — 5-step LLM-driven pipeline (Persona → Anchors → Bridges → Vocabulary → Patterns)
> L74: One-line install to any skill-compatible agent (Claude / Qoder / Cursor / Cline / ...). No project code, no server.

## 星数曲线

```mermaid
xychart-beta
    title "orzcls/PersonaLingo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `4e556f7069a0` · [字段定义](../../DATASET.md)*
