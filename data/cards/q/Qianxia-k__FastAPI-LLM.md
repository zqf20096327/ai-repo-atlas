# Qianxia-k/FastAPI-LLM

⭐ 19 · Python · 推送 2026-08-30 · [GitHub](https://github.com/Qianxia-k/FastAPI-LLM) · 个人维护 · 中文 README

**基于 FastAPI 的新闻问答平台：LLM 流式对话 + RAG**

个人学习项目，在新闻类 FastAPI 后端课程基础上扩展大模型能力：接入通义千问（DashScope API Key），以 SSE 实现流式对话；提供用户注册登录、多会话管理与上下文持久化，通过会话摘要与缓存压缩长对话历史。基于 LangChain 封装 RAG 流程，用 Chroma 构建本地向量库，从系统数据库真实新闻中检索增强。附带 Vue 3 + Pinia 前端。适合 FastAPI 与 Prompt 工程入门实践参考。

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

- SSE 流式对话响应与多会话上下文持久化
- 会话摘要与对话缓存压缩长对话 Token 消耗
- LangChain + Chroma 的 RAG 流程，检索源限于库内真实新闻
- JWT 鉴权、新闻分类/收藏/阅读历史等 RESTful 业务模块

## 适用场景

- 学习 FastAPI 异步后端与 LLM 工程化接入
- 实践 Prompt 工程与 RAG 检索增强问答
- 作为新闻领域问答应用的入门参考实现

## 场景标签

`RAG` `聊天机器人` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L12: - ** 大模型接入 (AI Chat)**：深度集成通义千问提供的 LLM 能力，应用 `Server-Sent Events (SSE)` 技术实现极低延迟的流式 (Streaming) 对话响应，提供如同 ChatGPT 般
> L19: ## 基于 LangChain 架构的检索增强生成（RAG）

## 星数曲线

```mermaid
xychart-beta
    title "Qianxia-k/FastAPI-LLM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-29 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a672b73618ea` · [字段定义](../../DATASET.md)*
