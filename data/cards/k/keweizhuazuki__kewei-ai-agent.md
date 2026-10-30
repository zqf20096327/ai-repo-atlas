# keweizhuazuki/kewei-ai-agent

⭐ 21 · Java · 推送 2026-10-10 · [GitHub](https://github.com/keweizhuazuki/kewei-ai-agent) · 个人维护 · 中文 README

**Spring Boot + Spring AI + Vue 的 AI Agent 实践项目：聊天/RAG/工具/记忆**

面向学习、扩展与本地演示的 AI Agent 全栈项目：Java 21 + Spring Boot 4 + Spring AI 后端，Vue 3 前端。包含 LoveApp 上下文聊天（同步/SSE、会话记忆、图片问答）与 Manus 多步工具调用（TodoWrite 进度、AskUserQuestion 问答续跑）、RAG（Markdown 加载、pgvector 向量、检索过滤）、文件/MySQL/Redis 记忆、文件与 PDF/PPT/邮件等工具、MCP 扩展。默认模型提供方为 Ollama，启动需 PostgreSQL+pgvector 与已配置的 MCP 服务；认证、限流与审计未完成，不可直接公网暴露。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LoveApp 同步/SSE 聊天与会话记忆、图片问答
- Manus 多步工具调用：TodoWrite 进度与 AskUserQuestion 续跑
- RAG：Markdown 加载 + pgvector 向量存储 + 检索过滤
- 文件/MySQL/Redis 聊天记忆与独立 Markdown 长期记忆工具

## 适用场景

- 学习 Spring AI 的聊天、RAG、工具调用与 MCP 集成实践
- 本地演示带前端 UI 的多步 Agent（计划→提问→续跑）流程
- 在自家环境扩展对话记忆、工具与 MCP 服务做二次开发

## 场景标签

`RAG` `Agent 记忆` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L5: A hands-on AI Agent project built with **Spring Boot + Spring AI + Vue 3**. Explore contextual chat, streaming repli
> L47: **Stack:** Java 21, Spring Boot 4, Spring AI 2.0.0-M2, Maven, Vue 3, Vite 7, Pinia, Ollama, PostgreSQL / pgvector.

## 星数曲线

```mermaid
xychart-beta
    title "keweizhuazuki/kewei-ai-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `a1bd3288c365` · [字段定义](../../DATASET.md)*
