# cRED-f/QuestGen-AI-Agent

⭐ 23 · Python · MIT · 推送 2026-10-13 · [GitHub](https://github.com/cRED-f/QuestGen-AI-Agent) · 组织维护

**面向教授的 AI 课程出题工作台：资料问答、拟题、审阅、导出试卷**

基于课程材料的应用：教授可上传 PDF/DOCX/PPTX 等资料，通过 SQLite FTS5 检索进行带引用的流式问答；Agent 模式讨论出题目标、检索课程或网络资料、经批准的计划后生成并可逐题修改的草稿；Exam 模式直接或导入草稿组卷，批准后导出学生卷（不含答案）与教师卷（含答案与解析）的 PDF/DOCX。所有 AI 生成内容在人工批准前均为草稿。支持 OpenAI/Anthropic/OpenRouter/Ollama 等模型连接，本地部署需 Node.js 20.9+ 与 Python 3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 课程资料问答与 Agent 出题双模式，人工批准为强制环节
- SQLite FTS5 课程级检索，可选 Ollama embeddings，含页码/幻灯片引用
- 支持 PDF/DOCX/PPTX/TXT/Markdown 及图片上传，PPTX 渲染可用 LibreOffice
- 导出学生卷与教师卷 PDF/DOCX，连接 OpenAI/Anthropic/OpenRouter/Ollama

## 适用场景

- 基于自己的课件和讲义让 AI 起草试题并逐题修改
- 整理课程资料并向 AI 助手提问获得带出处的回答
- 组卷后导出可打印的学生卷和教师卷

## 场景标签

`文档问答` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L4:  An AI-powered, course-grounded assessment workspace for professors.
> L14: - **Chat Mode** — Ask questions about course materials, receive cited, streamed answers, and revisit saved conversa
> L15: - **Agent Mode** — Discuss assessment goals, research course or web sources when needed, approve a proposed plan, t
> L16: - **Exam Mode** — Generate an exam directly or import selected Agent Mode drafts, organize the paper, approve it, a

## 星数曲线

```mermaid
xychart-beta
    title "cRED-f/QuestGen-AI-Agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `ecd13d9c6525` · [字段定义](../../DATASET.md)*
