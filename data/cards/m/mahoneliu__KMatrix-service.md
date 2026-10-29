# mahoneliu/KMatrix-service

⭐ 27 · Java · NOASSERTION · 推送 2026-05-20 · [GitHub](https://github.com/mahoneliu/KMatrix-service) · [官网](http://kmatrix.kykms.cn) · 个人维护 · 中文 README

**面向企业的 RAG 知识库与 LLM 工作流平台，可搭建问答助手**

基于 RuoYi-Vue-Plus（Spring Boot 3 + JDK 17）与 LangChain4j/LangGraph4j 构建的企业知识库工作流平台。提供 RAG 检索（pgvector 向量 + GIN 全文 + RRF 混合检索 + BGE-Reranker 重排）、父子分块、多格式文档解析（PDF/Word/PPT/Excel/Markdown）、基于 Vue Flow 的可视化工作流编排，以及一行脚本嵌入第三方系统的问答助手。支持接入本地模型（DeepSeek R1/Llama 3/Qwen 2）与公有云模型。提供 Docker 一键部署与源码构建两种方式，后端需 JDK 17+、PostgreSQL（pgvector/pgroonga）与 Redis。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- pgvector 向量检索 + GIN 全文检索 + RRF 混合检索 + BGE-Reranker 重排
- 基于 Vue Flow 的可视化工作流编排，支持节点拖拽
- 一行脚本将问答助手嵌入第三方业务系统
- 支持本地私有模型（DeepSeek R1/Llama 3/Qwen 2）与公有云模型接入

## 适用场景

- 企业将存量文档转为可问答的知识库
- 搭建智能客服、文档分析等 AI 应用
- 通过拖拽工作流编排 AI 业务流程
- 本地私有化部署保障知识资产安全

## 场景标签

`RAG` `知识库管理` `文档问答` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L27: KMatrix is not just a document repository; it is an **AI Agent Incubation Platform**. Users can easily build intell
> L34: - **🧠 Powerful AI Engine**: Deeply integrated with **LangChain4j** and **LangGraph4j**, providing the strongest AI 

## 星数曲线

```mermaid
xychart-beta
    title "mahoneliu/KMatrix-service 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `7d4bf2201555` · [字段定义](../../DATASET.md)*
