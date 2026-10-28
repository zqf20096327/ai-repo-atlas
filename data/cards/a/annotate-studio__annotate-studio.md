# annotate-studio/annotate-studio

⭐ 24 · TypeScript · NOASSERTION · 推送 2026-10-19 · [GitHub](https://github.com/annotate-studio/annotate-studio) · 个人维护

**本地优先的学习工作室：阅读、标注、AI 助手、闪卡与考试一体**

面向学生的本地优先学习应用，用 Tauri + Rust 与 Next.js 构建，把 PDF/Markdown/LaTeX 阅读、标注、AI 助手、间隔重复闪卡、练习考试与番茄钟整合到一个工作区。AI 助手可作为 agent 在整个工作区检索、读写笔记与闪卡，支持 OCR、公式推理、Lean 证明转自然语言等；AI 提供方灵活，可用本地 Ollama 或 OpenAI、Gemini 等外部 API。预编译二进制通过 GitHub Actions 产物分发，开发需 npm 与 Tauri CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工作区级 AI agent：自动检索阅读、创建编辑笔记/闪卡/考试，改动可撤销
- 本地优先设计，本地模型与本地数据可用，亦可接入外部云 AI
- 间隔重复闪卡与 AI 生成闪卡/练习考试
- 支持 Markdown/LaTeX（公式编号、宏、.tex 一键编译 PDF）与波斯语等 RTL 文本排版

## 适用场景

- 在一个地方读文献、做笔记并让 AI 按材料解答问题
- 生成并按间隔重复复习闪卡、练习考试
- 把扫描 PDF OCR 成文字、把多个文件整理成结构化学习手册

## 场景标签

`AI 助手` `知识库管理` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L7: It combines reading, annotation, AI assistance, flashcards, exams, focused study sessions, and personal study suppor
> L53: The assistant can work as an agent over your whole workspace. It decides what to search and read, and it can create
> L83: ### AI Providers

## 星数曲线

```mermaid
xychart-beta
    title "annotate-studio/annotate-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4dd40bbb0ffd` · [字段定义](../../DATASET.md)*
