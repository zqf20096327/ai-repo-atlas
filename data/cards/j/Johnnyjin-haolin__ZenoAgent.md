# Johnnyjin-haolin/ZenoAgent

⭐ 30 · Java · MIT · 推送 2026-03-27 · [GitHub](https://github.com/Johnnyjin-haolin/ZenoAgent) · [官网](http://1.94.53.50) · 个人维护 · 中文 README

**面向企业的服务端 AI Agent 平台：自定义 Agent+双模式 MCP+RAG**

基于 Spring Boot 2.7.18 与 LangChain4j 1.11.0 构建的服务端 toB AI Agent 平台，前端为 Vue 3 + Ant Design Vue。每个 Agent 可独立配置提示词、工具集、知识库与 Skill 目录树；GLOBAL/PERSONAL 双模式 MCP 区分服务端企业工具与浏览器端用户私有工具（密钥存 localStorage）；通过工具渐进式加载与 Skill 渐进式注入应对上下文窗口限制；RAG 基于 PostgreSQL+pgvector，人工确认基于 Redis 阻塞队列。运行依赖 Java 17、Redis、MySQL，提供 Docker Compose 启动方式，已部署线上体验实例（qwen3:8b）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GLOBAL/PERSONAL 双模式 MCP：服务端企业工具与浏览器端用户私有工具（密钥不离开浏览器）
- 工具渐进式加载与 Skill 渐进式注入，Agent 可绑定上百个工具
- RAG 知识检索（PostgreSQL+pgvector，Tika 解析 PDF/Word/TXT/Markdown）
- 基于 Redisson 阻塞队列的分布式 Human-in-the-loop 人工确认

## 适用场景

- 企业搭建统一管控的服务端 Agent 平台，沉淀业务 Skill 与知识库
- 让员工接入 GitHub、Notion 等私有工具且密钥不上传服务端
- 关键操作需人工确认的生产环境 Agent 部署

## 场景标签

`RAG` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L16: Zeno Agent 是一个面向企业（toB）的服务端 AI Agent 平台，基于 Spring Boot + LangChain4j 1.11.0 构建。平台的核心能力在于：每个 Agent 可以独立配置自己的工具集、知识库和
> L24: - **多维度配置**: 每个 Agent 独立配置系统提示词、工具集（GLOBAL MCP / PERSONAL MCP / 系统工具）、知识库、Skill 目录树
> L90: - **LangChain4j 1.11.0** - LLM 抽象层和 MCP 工具集成

## 星数曲线

```mermaid
xychart-beta
    title "Johnnyjin-haolin/ZenoAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2a8ec9214fef` · [字段定义](../../DATASET.md)*
