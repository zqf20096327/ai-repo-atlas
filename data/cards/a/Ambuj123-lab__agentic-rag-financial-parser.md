# Ambuj123-lab/agentic-rag-financial-parser

⭐ 109 · Python · AGPL-3.0 · 推送 2026-09-30 · [GitHub](https://github.com/Ambuj123-lab/agentic-rag-financial-parser) · [官网](https://agentic-rag-financial-parser.onrender.com/) · 个人维护

**面向印度金融法律文档的 11 节点 Agentic RAG 问答系统**

基于 LangGraph StateGraph 构建的自主 RAG 管线，解析并问答印度政府金融与法律文档（联邦预算、财政法案、税法、PF/养老金计划、RBI KYC、印度宪法等）。查询依次经过意图分类、6 路路由、双路向量检索（Jina MRL 嵌入 + Pinecone + Cohere 重排）、生成、幻觉防护与后处理等 11 个节点；含 MongoDB 会话存储、Redis 语义缓存、Langfuse 追踪。后端 FastAPI + React 19 前端，Docker 多阶段构建部署于 Render（512MB RAM 约束）。AGPL-3.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 节点 LangGraph 状态机：分类→路由→检索→重排→生成→幻觉防护
- Jina MRL 256 维嵌入 + Pinecone（14,662 向量）+ Cohere 神经重排
- Tavily 网络搜索兜底（需 HITL 用户许可）与 Gemini 工具调用获取实时行情
- Redis 语义缓存（<100ms）+ pybreaker 熔断 + Langfuse 追踪

## 适用场景

- 查询印度预算、税法、养老金等政府文档获得带溯源的回答
- 作为低内存（512MB）环境下生产级 Agentic RAG 的参考实现
- 通过 WhatsApp 机器人进行实时金融文档问答

## 场景标签

`文档问答` `RAG` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L30: An **autonomous, 11-node Agentic RAG pipeline** that parses and queries complex Indian financial & legal documents 
> L60: |**8. Generator**|LLM synthesis|Gemini 3.5 Flash Lite (primary) with `pybreaker` circuit breakers|
> L61: |**9. HallucinationGuard**|Answer verification|LLM-as-Judge — advisory mode (appends disclaimer, doesn't block)|

## 星数曲线

```mermaid
xychart-beta
    title "Ambuj123-lab/agentic-rag-financial-parser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 108 --> 110
    line [109, 109]
```

2026-10-18 109 → 2026-10-23 109（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7337f5d90cff` · [字段定义](../../DATASET.md)*
