# tavily-ai/tavily-chat

⭐ 79 · TypeScript · MIT · 推送 2026-09-17 · [GitHub](https://github.com/tavily-ai/tavily-chat) · [官网](https://chat.tavily.com/) · 组织维护

**基于 Tavily 搜索/抽取/爬取的联网对话 agent 示例应用**

Tavily 官方提供的对话式 agent 示例仓库：用 LangGraph 构建 ReAct 架构的聊天 agent，在基础模型知识与 Tavily 实时 search/extract/crawl 之间路由问题，附对话记忆、引用来源、Markdown 输出与子步骤流式展示。后端为 FastAPI，前端为 React，需配置 TAVILY/OPENAI/GROQ 等 API key，本地分别启动 Python 后端与 npm 前端。README 声明可扩展接入私有数据、修改聊天架构与替换 LLM。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在基础知识与 Tavily search/extract/crawl 之间做问题路由
- LangGraph ReAct agent 架构与对话记忆
- FastAPI 后端 + React 前端，流式返回 agent 子步骤
- 网页结果附引用来源，Weave 可观测性

## 适用场景

- 搭建可访问实时网页信息的对话 agent
- 在其基础上扩展私有数据接入或替换 LLM
- 学习 search/extract/crawl 与聊天 agent 的集成方式

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: This repository provides a simple yet powerful example of building a conversational agent with real-time web access,
> L16: - 🔍 Intelligent question routing between base knowledge and tavily search, extract, and crawl.
> L17: - 🧠 Conversational memory with LangGraph

## 星数曲线

```mermaid
xychart-beta
    title "tavily-ai/tavily-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-27 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `56e475de246c` · [字段定义](../../DATASET.md)*
