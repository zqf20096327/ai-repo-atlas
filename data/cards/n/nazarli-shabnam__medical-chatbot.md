# nazarli-shabnam/medical-chatbot

⭐ 10 · Jupyter Notebook · Apache-2.0 · 推送 2025-12-12 · [GitHub](https://github.com/nazarli-shabnam/medical-chatbot) · 个人维护

**带来源引用的医学文档问答聊天机器人（RAG）**

基于 Flask、Gemini、Pinecone 和 PostgreSQL 构建的医学聊天机器人应用。用户注册登录后可上传 PDF 文档，通过 RAG 检索获得流式回答，每条回答附带文档名、页码与内容预览的可点击引用；支持查询改写与多跳推理（Advanced RAG 开关）、按用户的持久会话历史及点赞/点踩反馈。通过 docker-compose 一键部署，提供完整的 API 端点、pytest 测试与 GitHub Actions CI/CD。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档 RAG 问答，回答附文档名/页码/内容预览的可点击引用
- 查询改写与多跳推理，可通过聊天界面 Advanced RAG 开关启用
- 多用户认证、会话历史与上传文档管理
- docker-compose 部署，含 pytest 测试与 GitHub Actions CI/CD

## 适用场景

- 上传自己的 PDF 医学资料进行带出处的问答
- 搭建带用户系统和引用溯源的 RAG 问答应用
- 作为 RAG + 引用机制的工程参考实现

## 场景标签

`聊天机器人` `文档问答` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3: A comprehensive medical chatbot application built with Flask, Gemini AI, Pinecone, and PostgreSQL. Features real-tim
> L44: - ✅ **Advanced RAG** - Query rewriting and multi-hop reasoning

## 星数曲线

```mermaid
xychart-beta
    title "nazarli-shabnam/medical-chatbot 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `3e67ee833365` · [字段定义](../../DATASET.md)*
