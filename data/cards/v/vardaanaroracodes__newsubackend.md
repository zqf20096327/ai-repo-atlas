# vardaanaroracodes/newsubackend

⭐ 10 · Python · 推送 2025-12-25 · [GitHub](https://github.com/vardaanaroracodes/newsubackend) · [官网](https://www.newsu.live/) · 个人维护

**按兴趣回答新闻问题的 AI 新闻聚合后端服务**

基于 Flask、LangChain 与 Google Gemini API 构建的新闻问答后端：用户提交查询后，AI 提取关键词，经 Serper API 检索新闻，再由 Gemini 生成摘要回答，并保留对话历史。提供单次问答与多会话（MongoDB 持久化、按用户隔离、可增删查清）两组 REST 端点，用 API key 与 Clerk JWT 鉴权。README 标注尚未更新完毕。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Gemini 提取关键词→Serper 检索→摘要生成的多步 Agent 工作流
- MongoDB 持久化的多会话管理（每用户隔离、可恢复历史）
- API key 鉴权与 Clerk JWT 校验
- 支持追问的对话记忆机制

## 适用场景

- 用自然语言询问近期新闻并获取摘要和相关文章
- 为已有前端接入新闻问答后端 API
- 维护按用户隔离的多轮对话式新闻查询会话

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L5: This project is a **Conversational AI-powered News Aggregation System** built using **Flask**, **LangChain**, and **
> L253: 1️⃣ **User submits a prompt** via the frontend. 2️⃣ **Backend authenticates the request** (checks API key & JWT fr
> L257: LangChain plays a vital role in: ✔ **Managing AI decision-making** (ReAct agents) ✔ **Integrating third-party APIs

## 星数曲线

```mermaid
xychart-beta
    title "vardaanaroracodes/newsubackend 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-19"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-19 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `5d4cefab6d9d` · [字段定义](../../DATASET.md)*
