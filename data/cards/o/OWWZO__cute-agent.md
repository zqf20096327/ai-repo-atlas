# OWWZO/cute-agent

⭐ 207 · Java · 推送 2026-10-24 · [GitHub](https://github.com/OWWZO/cute-agent) · 组织维护 · 中文 README

**云端多智能体研究与分析平台：全网采集情报并生成报告**

面向全网研究与复杂数据分析的多 Agent 应用：从 Reddit、X、YouTube、BiliBili、小红书、Hacker News 等十余个公开渠道并行采集，结合多模态 RAG 处理私有文档，经 E2B 沙箱代码执行、NL2SQL、交叉核验形成带出处的分析，以 GenUI 画布和 PDF/Word/PPT/HTML 报告交付。架构为 Java（Spring Boot/Spring AI）运行时 + Python 工具服务 + React 工作台，需 MySQL、JDK 21、Node.js 20+、Python 3.11+ 与 OpenAI-compatible LLM API，Qdrant、Elasticsearch、E2B 为可选。给需要跨平台情报聚合、数据分析与报告产出的用户使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DeepResearch 多轮检索，支持 DuckDuckGo/Exa/Tavily/Brave 等 10+ 信息渠道
- 多模态 RAG + NL2SQL（Table RAG）+ E2B 沙箱代码执行
- GenUI 画布、3D 展示与 PDF/DOCX/PPTX/HTML/Excel 多格式报告生成
- 多 Agent 协作、Human-in-the-loop 审批、长期记忆与 Skill/MCP 工具体系

## 适用场景

- 跨社媒平台做话题调研、竞品研究与舆情分析
- 把私有文档与公网情报放进同一条证据链做研究
- 自然语言问业务数据库并生成可视化分析
- 生成 PDF/Word/PPT 格式的研究报告

## 场景标签

`多智能体` `RAG` `数据分析` `网页抓取` · 领域:Agent 开发

## 证据(README 行号)

> L7:  一个面向全网研究与复杂数据分析的云端智能体，能在公开网络、YouTube、BiliBili、X、小红书、Hacker News上研究任何主题
> L216: - **DeepResearch公域信息检索**：查询拆解、多轮 `extend/search/report` 阶段、并发检索、正文抓取、去重、摘要和 SSE 流式进度，支持 DuckDuckGo、Exa、Tavily、Brav


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `781ce07042e9` · [字段定义](../../DATASET.md)*
