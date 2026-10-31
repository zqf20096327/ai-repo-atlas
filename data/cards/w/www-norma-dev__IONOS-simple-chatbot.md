# www-norma-dev/IONOS-simple-chatbot

⭐ 15 · Python · MIT · 推送 2026-01-15 · [GitHub](https://github.com/www-norma-dev/IONOS-simple-chatbot) · [官网](https://www-norma-dev.github.io/IONOS-simple-chatbot/) · 组织维护

**基于 IONOS AI 的全栈对话机器人起步包（ReAct agent）**

全栈 AI 聊天应用起步包：后端为 FastAPI + LangGraph ReAct agent，集成 Tavily 实时网页搜索与工具调用；模型接入 IONOS AI Model Hub（推理模型）与 IONOS AI Model Studio（微调模型），支持流式输出、多轮上下文与模型路由。前端提供 Streamlit（推荐）与 Next.js 两种实现。附带 GitHub Actions 标签触发的 Docker 镜像构建与 IONOS Kubernetes 部署流水线。运行需配置 IONOS 与 Tavily API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph ReAct agent 支持工具调用与 Tavily 实时网页搜索
- 双模型接入：IONOS Hub 推理模型 + Studio 微调模型
- Streamlit 与 Next.js 两种前端可选，支持流式输出
- 标签触发的 CI/CD：Docker 构建并部署到 Kubernetes

## 适用场景

- 快速搭建接入 IONOS AI 模型的对话应用
- 在聊天中使用带实时联网搜索的 ReAct agent
- 将自己的微调模型接入对话界面使用

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: This repository contains a **full-stack AI chatbot powered by IONOS AI**, featuring a ReAct agent with real-time web
> L9: - **Backend**: FastAPI service with LangGraph ReAct agent that uses Tavily for web search and integrates with both I

## 星数曲线

```mermaid
xychart-beta
    title "www-norma-dev/IONOS-simple-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `de072fbdad39` · [字段定义](../../DATASET.md)*
