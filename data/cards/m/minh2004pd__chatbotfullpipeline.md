# minh2004pd/chatbotfullpipeline

⭐ 18 · Python · 推送 2026-04-22 · [GitHub](https://github.com/minh2004pd/chatbotfullpipeline) · [官网](https://d3qrt08bgfyl3d.cloudfront.net/) · 个人维护

**多模态 AI 研究助手：RAG、长期记忆、实时转录与 Wiki 知识库**

基于 Google ADK 与 Gemini 构建的多模态 AI agent 应用，前后端分离（FastAPI + React/TypeScript）。功能包括 SSE 流式聊天、PDF 上传后 chunk/embed/语义检索的 RAG、基于 mem0 的长期记忆、Soniox 实时语音转录（60+ 语言）以及由 LLM 从文档与会议记录自动合成的 Wiki 知识图谱。后端基础设施用 Terraform 部署到 AWS（ECS/S3/DynamoDB/RDS/ElastiCache/CloudFront），本地通过 Docker Compose 运行，需配置 GEMINI_API_KEY。MIT 许可。

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

- PDF 上传→chunk→embed→语义检索的 RAG 流程，带引用
- mem0 长期记忆 + Soniox 实时转录（60+ 语言）自动入 RAG
- LLM 自动合成 Wiki 知识图谱并以 React Flow 可视化
- Terraform 管理 AWS 全套基础设施，GitHub Actions CI/CD

## 适用场景

- 上传 PDF 文档做带引用的问答研究助手
- 记录会议并自动转录、沉淀为个人知识库
- 需要长期记忆跨会话记住用户信息的对话助手

## 场景标签

`RAG` `知识图谱` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: **Multimodal AI Research Assistant** được xây dựng trên **Google Agent Development Kit (ADK)**
> L36: |🚀 **Realtime Chat Streaming**|SSE token-by-token, phản hồi tức thì|
> L38: |🧠 **Long-term Memory**|Tích hợp **mem0** ghi nhớ thông tin cá nhân xuyên phiên|

## 星数曲线

```mermaid
xychart-beta
    title "minh2004pd/chatbotfullpipeline 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `b945c9fd2ab2` · [字段定义](../../DATASET.md)*
