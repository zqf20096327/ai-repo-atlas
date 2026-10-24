# hoangsonww/AI-RAG-Assistant-Chatbot

⭐ 50 · TypeScript · MIT · 推送 2026-09-27 · [GitHub](https://github.com/hoangsonww/AI-RAG-Assistant-Chatbot) · [官网](https://lumina-david.vercel.app) · 个人维护

**个人 AI 助手全栈应用：混合 RAG 问答与聊天**

名为 Lumina 的全栈 Web 聊天应用：用户可就作者个人信息及一般话题提问，获取基于 RAG 的流式回答。检索层并行使用 Pinecone 向量搜索与 Neo4j 图遍历并做双源融合评分，生成使用 Google Gemini（6 模型轮换），支持行内引用、话题感知全源增强与静态回退。附带 30+ 工具的 MCP 服务器与 LangGraph 多 agent 管线。功能含 JWT/Passkey 认证、会话分支编辑、会话搜索、访客模式。前端 React+Vite，后端 Express+MongoDB；自建需 npm 安装依赖并配置环境变量（JWT_SECRET 必填），已有 Vercel/Netlify 在线部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pinecone 向量 + Neo4j 图并行检索与双源融合的混合 RAG，带行内引用
- SSE 流式回答、会话分支编辑、AI 自动生成会话标题
- 30+ 工具的独立 MCP 服务器与 LangGraph 多 agent 管线
- JWT 与 Passkey（WebAuthn）双认证，支持访客模式

## 适用场景

- 搭建一个可回答个人知识库问题的聊天机器人
- 参考混合向量+图谱 RAG 与多 agent 管线的实现
- 直接在线体验作者部署的 AI 助手应用

## 场景标签

`聊天机器人` `RAG` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L3: **David Nguyen's Personal AI Assistant** - **Lumina** is a full-stack web application that allows users to ask quest
> L65: - **AI Chatbot:** Ask questions about David Nguyen and general topics; receive responses from an AI.
> L72: - **Grounded Knowledge Base:** RAG (Retrieval-Augmented Generation) with Pinecone vector search and Neo4j graph tra

## 星数曲线

```mermaid
xychart-beta
    title "hoangsonww/AI-RAG-Assistant-Chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-24 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `0dae3a4c6363` · [字段定义](../../DATASET.md)*
