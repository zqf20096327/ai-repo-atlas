# haodehaode378/ai-paper-coach

⭐ 43 · Python · 推送 2026-07-29 · [GitHub](https://github.com/haodehaode378/ai-paper-coach) · 个人维护 · 中文 README

**给学生和研究者的 AI 论文阅读与复现助手**

Web 应用（Vue 3 前端 + FastAPI 后端）：输入 arXiv/PDF 链接或上传 PDF，经 ingest→analyze→review→finalize→report 流水线自动生成结构化报告，含七问框架解读、复现指导与字数阈值校验（摘要≥800 字、复现指导≥1000 字、七问每题≥700 字）。支持基于论文原文的跨语言 RAG 问答、报告与 PDF 原文对照阅读、Markdown/PDF 导出、历史记录管理与 trace 回放。模型 key 通过 .env 配置，支持双模型协作与模型校验；v0.2 进行中（异步架构、LangSmith 追踪）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ingest→analyze→review→finalize→report 全自动流水线（异步 + SSE 进度）
- 七问框架结构化输出与字数阈值校验
- 基于论文原文的跨语言 RAG 问答（中文问英文论文）
- trace 记录、历史管理与 Markdown/PDF 报告导出

## 适用场景

- 上课或组会前快速理解一篇论文并准备汇报
- 根据复现指导形成实验 TODO 清单
- 对照 PDF 原文对生成的解读提问并溯源
- 长期积累个人论文阅读档案

## 场景标签

`科研工具` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L34: AI Paper Coach 是一个面向学生和研究者的论文阅读与复现助手。
> L35: 输入 arXiv/PDF 链接或直接上传 PDF，就能自动生成结构化报告，并支持后续问答与历史追踪。
> L46: - RAG 问答：基于论文原文的检索增强问答，支持跨语言查询（中文问英文论文）

## 星数曲线

```mermaid
xychart-beta
    title "haodehaode378/ai-paper-coach 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ee4f2a38bbf6` · [字段定义](../../DATASET.md)*
