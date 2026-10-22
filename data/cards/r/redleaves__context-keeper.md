# redleaves/context-keeper

⭐ 155 · Go · MIT · 推送 2026-01-13 · [GitHub](https://github.com/redleaves/context-keeper) · 组织维护 · 中文 README

**面向开发者的 LLM 记忆与上下文管理系统，供 AI 助手持久记忆**

用 Go 编写的智能记忆与上下文管理服务：为 AI 编程助手提供跨会话记忆，采用长短期记忆分层（本地文件+向量库）、LLM 驱动的宽召回+精排序两阶段检索、语义+时间+知识图谱三维记忆，通过 MCP 协议接入 Cursor/VSCode 等 IDE。部署需向量数据库（阿里云 DashVector/京东云 Vearch）、TimescaleDB/PostgreSQL、Neo4j 和 LLM（本地 Ollama 或云端 DeepSeek/OpenAI/Claude/通义千问），提供 git clone 源码部署、Docker 与 docker-compose 方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 长短期记忆分层：本地文件短期记忆+向量库长期记忆，渐进式压缩
- LLM 驱动的宽召回+精排序两阶段检索（语义+时间+知识图谱）
- 通过 MCP 协议集成 Cursor/VSCode 等 IDE
- 支持本地 Ollama 模型与云端 LLM（DeepSeek/OpenAI/Claude 等）

## 适用场景

- 让 AI 编程助手记住历史架构决策与讨论上下文
- 团队沉淀项目知识，减少向 AI 重复解释背景
- 跨会话检索历史 Bug 修复经验与技术选型记录

## 场景标签

 · 领域:LLM 基础设施/AI 记忆管理

## 证据(README 行号)

> L5: **基于LLM驱动的智能记忆与上下文管理系统**
> L94: Context-Keeper基于**LLM驱动的智能上下文记忆管理系统**，在一期基础上实现了两个关键突破：
> L281: curl -X POST http://localhost:8088/mcp \

## 星数曲线

```mermaid
xychart-beta
    title "redleaves/context-keeper 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 153 --> 156
    line [155, 154, 155]
```

2026-10-18 155 → 2026-10-22 155（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `acbb8c0766ac` · [字段定义](../../DATASET.md)*
