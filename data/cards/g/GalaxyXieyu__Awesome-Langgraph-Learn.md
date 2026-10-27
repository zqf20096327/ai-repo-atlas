# GalaxyXieyu/Awesome-Langgraph-Learn

⭐ 78 · HTML · MIT · 推送 2026-07-16 · [GitHub](https://github.com/GalaxyXieyu/Awesome-Langgraph-Learn) · [官网](https://aigalaxy.top/) · 个人维护 · 中文 README

**LangGraph 中文教程仓库：从入门图构建到生产部署的完整路径**

面向有 Python 基础的开发者的 LangGraph 系统学习仓库：提供 11 节渐进式教程（讲义 md + 可运行 notebook），覆盖图构建、人机协作、记忆持久化（Postgres/Redis）、并行子图、多智能体（Supervisor/Swarm）、流式输出、Docker 部署与 Langfuse 监控；另附 6 个可独立运行的示例项目（上下文裁剪、Redis 记忆、Celery 异步队列等）。提供三档启动方式：本地 venv、精简 Docker（PG+pgvector+Redis）、完整观测环境。需配置 OPENAI_API_KEY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 节渐进式教程，每节含讲义与可运行 notebook
- 6 个独立示例项目：多智能体 Handoff、Redis 记忆、Celery 异步任务等
- 三档环境：本地 venv / 精简 Docker / Langfuse 完整观测环境
- 覆盖 Checkpoint/Store、Send/Map-Reduce、Prompt 版本管理等生产机制

## 适用场景

- 系统学习 LangGraph 从基础到多智能体与生产部署
- 参考多智能体架构（Supervisor/Swarm/Handoff）的对比实现
- 搭建带记忆、审批与全链路监控的 Agent 服务

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L44: ### 11 节渐进式教程（turtorial/）
> L62: ### 6 个独立示例项目（examples/）

## 星数曲线

```mermaid
xychart-beta
    title "GalaxyXieyu/Awesome-Langgraph-Learn 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-27 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `09a245af5d03` · [字段定义](../../DATASET.md)*
