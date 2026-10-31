# margelo/ai-chat-demo

⭐ 193 · TypeScript · 推送 2026-08-05 · [GitHub](https://github.com/margelo/ai-chat-demo) · [官网](https://margelo.com/blog/building-native-llm-chat-app-with-rag) · 组织维护

**React Native 的 ChatGPT 式移动聊天 demo，带 Margelo 知识库 RAG**

Margelo 出品的移动端聊天应用示例：基于 OpenAI Responses API，通过 WebSocket 流式输出回复与推理摘要，用 previous_response_id 串联多轮对话。针对 Margelo 相关问题调用检索工具，从 Pinecone 向量索引（服务端集成 embedding）中查询事实并仅据检索结果回答。支持图片附件（base64 发送）、原生 markdown 流式渲染、iOS 26+ Liquid Glass 界面。限制：需自备 OpenAI API key 与 Pinecone 索引，README 声明密钥打包在应用内、不适用于生产。

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

- OpenAI Responses API 经 WebSocket 流式输出，回复与推理摘要逐 token 呈现
- RAG 工具 search_margelo_kb 查询 Pinecone 索引，Margelo 问题仅据检索结果回答
- 图片附件以 base64 数据 URL 发送并显示缩略图
- iOS 26+ Liquid Glass 界面，旧系统与 Android 回退为普通圆角样式

## 适用场景

- 参考其实现构建带 RAG 的 React Native 聊天应用
- 学习 WebSocket 流式 LLM 对话与多轮上下文串联
- 了解移动端检索工具调用与向量库接入的做法

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L5: A ChatGPT-style mobile chat app with a twist: it knows about **Margelo**. You talk to a streaming AI assistant that 
> L15: - **Knowledge base (RAG)** - the model can call a `search_margelo_kb` tool, which queries a Pinecone index (integra

## 星数曲线

```mermaid
xychart-beta
    title "margelo/ai-chat-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 192 --> 194
    line [193, 193]
```

2026-10-18 193 → 2026-10-31 193（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0843ec496d8d` · [字段定义](../../DATASET.md)*
