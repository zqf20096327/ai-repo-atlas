# stepanogil/autonomous-hr-chatbot

⭐ 461 · Python · MIT · 推送 2026-04-29 · [GitHub](https://github.com/stepanogil/autonomous-hr-chatbot) · [官网](https://autonomous-hr-chatbot.vercel.app) · 个人维护

**自主 HR 问答 agent 原型：用工具回答人力资源查询**

企业 HR 助手原型应用：基于 LangChain agents/tools 构建的自主 agent，通过三类工具回答 HR 查询——考勤政策文档（OpenAI 嵌入存入 Pinecone 索引做检索）、员工数据 CSV（PythonAstREPLTool 操作 pandas）、计算器链。前端为 Streamlit。v2/ 目录提供基于 OpenAI Responses API 的现代化版本（无 LangChain/Pinecone，含推理摘要）。原实现依赖 ChatGPT/gpt-3.5-turbo，可选 Azure OpenAI 后端。自述为 prototype。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LangChain agent 调用政策检索、员工数据查询、计算器三类工具
- 政策文档用 text-embedding-ada-002 嵌入并存储于 Pinecone
- v2/ 目录提供基于 OpenAI Responses API 的新实现（无 LangChain/Pinecone）
- Streamlit 聊天前端，支持 Azure OpenAI 后端切换

## 适用场景

- 作为企业内部 HR 问答助手的原型参考
- 学习 LangChain agent 多工具编排的实现方式
- 了解 HR 场景下 RAG 与结构化数据工具结合的模式

## 场景标签

`RAG` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L8: This is a prototype enterprise application - an autonomous agent that is able to answer HR queries using the tools i
> L9: It was made using LangChain's agents and tools modules, using Pinecone as vector database and powered by ChatGPT or 

## 星数曲线

```mermaid
xychart-beta
    title "stepanogil/autonomous-hr-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 460 --> 462
    line [461, 461]
```

2026-10-18 461 → 2026-10-29 461（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `efc39926cb21` · [字段定义](../../DATASET.md)*
