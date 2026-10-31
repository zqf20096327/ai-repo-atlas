# pinecone-io/vercel-chatbot-template

⭐ 16 · TypeScript · Apache-2.0 · 推送 2026-09-13 · [GitHub](https://github.com/pinecone-io/vercel-chatbot-template) · 组织维护

**Next.js 聊天机器人示例模板，接入 OpenAI 与 Pinecone**

基于 Next.js 的聊天机器人示例工程：通过 API Routes（Edge runtime）以流式方式调用 OpenAI ChatGPT API 生成回答，使用 Pinecone 向量存储实现检索，索引不存在时自动创建。面向希望快速搭建或部署到 Vercel 的开发者，提供一键部署与 create-next-app 两种使用方式；运行需配置 OPENAI_API_KEY 与 PINECONE_API_KEY 环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI ChatGPT API 流式输出
- Pinecone 向量存储（索引自动创建）
- 支持 Vercel 一键部署与 create-next-app 脚手架
- 基于 Next.js API Routes（Edge runtime）

## 适用场景

- 快速搭建带 RAG 检索的对话机器人原型
- 学习 Next.js + OpenAI + Pinecone 的集成方式
- 一键部署到 Vercel 验证效果

## 场景标签

`聊天机器人` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3: This example shows how to implement a chat bot backed by Pinecone using Next.js, API Routes, and OpenAI ChatGPT API.
> L8: - OpenAI API (ChatGPT) - streaming
> L10: - Pinecone store

## 星数曲线

```mermaid
xychart-beta
    title "pinecone-io/vercel-chatbot-template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `76a55f3e1d3d` · [字段定义](../../DATASET.md)*
