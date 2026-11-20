# KutalVolkan/ai_recruiter

⭐ 12 · Python · 推送 2026-06-16 · [GitHub](https://github.com/KutalVolkan/ai_recruiter) · 个人维护

**演示 RAG 简历匹配系统 XPIA 漏洞的测试管线**

一个概念验证项目：用 GPT-4o、PDF 解析与 ChromaDB 语义检索构建简历—职位匹配的 RAG 管线，然后演示通过在 PDF 简历中注入隐藏指令（XPIA）操纵评分与排序。支持手动注入（隐藏文字、微型字体、背景同色文字）与 PyRIT XPIA Orchestrator 自动化注入两种方式，并记录实验发现： blatant keyword stuffing 被 GPT-4o 打 0 分但仍按语义距离排名第一，contextual 变体可获得 8-10 分。声明仅限研究教育用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 简历匹配管线：PDF 提取 + ChromaDB 嵌入检索 + GPT-4o 打分（1-10）
- PyRIT XPIA Orchestrator 自动化间接提示注入攻击
- 记录注入实验发现：keyword stuffing 得 0 分但语义排名第一
- 配套 Docker 部署指南与扩展实验（L0-L3 防御分级）

## 适用场景

- 测试自家 RAG 系统对间接提示注入的抵抗力
- 安全研究：复现 PDF 注入操纵 AI 招聘评估的攻击场景
- AI 红队工作流的教学演示

## 场景标签

`RAG` `网络安全` · 领域:知识与检索

## 证据(README 行号)

> L3: Welcome to the AI Recruiter, a pipeline designed to match résumés with job descriptions using GPT-4o, while also pro
> L11: Manual injection of manipulative text, including invisible instructions and crafted language, is used to explore AI


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `a2de6175741d` · [字段定义](../../DATASET.md)*
