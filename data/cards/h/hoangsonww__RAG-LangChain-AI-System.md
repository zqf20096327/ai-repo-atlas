# hoangsonww/RAG-LangChain-AI-System

⭐ 51 · Jupyter Notebook · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/RAG-LangChain-AI-System) · [官网](https://hoangsonww.github.io/RAG-LangChain-AI-System/) · 个人维护

**面向投资组合智能的代理式 RAG 全栈平台**

完整的 agentic RAG 应用栈：React 前端提供流式聊天与会话管理；Flask + LangChain 的 RAG 服务支持语义/混合/多查询/分解四种检索策略（Chroma 向量 + BM25 词法 + 可选 cross-encoder 重排）；Express + MongoDB 后端提供投资组合结构化数据供工具链调用。LLM 侧通过 LangChain Ollama / OpenAI 集成。附带 Docker、Kubernetes（滚动/金丝雀/蓝绿）、Terraform（AWS/OCI）部署资产。限制：会话/缓存/限流为进程内存态，后端认证默认为演示用静态 token，README 提示多租户生产前需加固。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四种检索策略（semantic/hybrid/multi_query/decomposed）+ 可选重排
- 代理式后端工具链（团队/投资/行业档案、咨询等 API enrichment）
- OpenAI 兼容端点 POST /api/chat/completions 与 Socket.IO 流式输出
- K8s 渐进交付（rolling/canary/blue-green）与 AWS/OCI Terraform 栈

## 适用场景

- 搭建基于自有文档与结构化数据的投资组合问答助手
- 以 OpenAI 兼容 API 形式对外提供 RAG 服务
- 作为 agentic RAG + 云部署的参考工程学习部署与发布流程

## 场景标签

`RAG` `金融量化` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: A comprehensive agentic RAG platform for portfolio intelligence, evidence-backed chat, and API-enriched responses.
> L7: - `rag-app` (`Flask + Socket.IO + LangChain`) for retrieval, orchestration, and response generation, with reranking 
> L43: - OpenAI-compatible endpoint:

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/RAG-LangChain-AI-System 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-24 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9b57ac8715e6` · [字段定义](../../DATASET.md)*
