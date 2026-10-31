# 1firecracker/Agent-For-Exam

⭐ 15 · Python · Apache-2.0 · 推送 2026-05-10 · [GitHub](https://github.com/1firecracker/Agent-For-Exam) · 个人维护 · 中文 README

**面向备考的知识图谱问答、试题生成与自动批改 Web 应用**

基于 LightRAG 的考试辅助 Web 应用：上传 PPTX/PDF 讲义后自动抽取实体关系构建知识图谱（Cytoscape.js 可视化），提供 naive/local/global/mix 四种模式的引用来源问答，答案带页面级索引引用可跳转。多智能体流水线对历年试卷做题目到知识点与页码的映射分析，基于讲义生成模拟试题，并支持答卷上传（PDF/DOCX/TXT）、自动评分与薄弱知识点识别。内置基于 Function Calling 的 Agent 模式，可调用文档浏览、图谱问答、思维导图生成等工具。需在前端配置 OpenAI 兼容 API Key（主要支持硅基流动）方可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LightRAG 知识图谱构建与四种检索模式（naive/local/global/mix）
- 页面级引用来源，可点击跳转到对应讲义页
- 多智能体试题分析与基于讲义的模拟题生成、自动批改
- Function Calling Agent 模式：文档浏览/图谱问答/思维导图/按页阅读四类工具

## 适用场景

- 学生上传课程讲义后基于原文内容问答复习
- 用往年试卷分析考频与知识点分布
- 生成基于讲义内容的模拟题并自动批改答卷
- 按学科隔离管理多门课程的知识图谱与对话

## 场景标签

`知识图谱` `RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: agent for exam是一个基于 LightRAG 的智能考试助手系统，面向教育场景的知识图谱构建、页面级引用的智能问答、试题生成和自动批改的 Web 应用。支持 PPTX/PDF 文档上传、知识抽取、知识图谱可视化、智能对话
> L293: - **完整教学闭环**: 文档上传 → 知识抽取 → 试题生成 → 学生答题 → 自动批改 → 学习建议

## 星数曲线

```mermaid
xychart-beta
    title "1firecracker/Agent-For-Exam 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d4d9c3ffeb82` · [字段定义](../../DATASET.md)*
