# codenamekt/hexus

⭐ 14 · Python · BSD-3-Clause · 推送 2026-09-06 · [GitHub](https://github.com/codenamekt/hexus) · 个人维护

**基于 Postgres+pgvector 的 agent 向量记忆层与 MCP 服务器**

为多 agent 协作提供集中式记忆存储：以 Postgres+pgvector 为后端，本地 BERT 模型生成嵌入（无云端调用、无 LLM 在热路径）。提供两条接入路径：作为 hermes-agent 的 pip 插件，或作为独立 MCP 服务器供 Claude Desktop、Cursor 等客户端使用。支持按主题（theme）隔离记忆、shared/strict 两种读隔离模式、BM25+向量混合检索、时间衰减、TTL 与实体标签。运行依赖已启用 pgvector 的 PostgreSQL，可在纯 CPU 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 BERT 嵌入，无云端调用、无 LLM 在热路径
- 双路径接入：Hermes 插件或独立 MCP 服务器（stdio/http）
- shared/strict 多 agent 记忆读隔离与按主题作用域
- 混合检索（BM25+向量）、时间衰减、TTL、实体标签、对话摘要

## 适用场景

- 为 agent 队伍提供集中、可检索的共享记忆库
- 让 Claude Desktop / Cursor 等 MCP 客户端获得持久向量记忆
- 避免多 agent 共用本地 markdown 记忆文件互相覆盖

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Postgres + hexus memory substrate for hermes-agent AND a standalone Model Context Protocol (MCP) server for any cl
> L20: * **Ditch the Cloud Monoliths ☁️**: Other memory providers require paid cloud services and route every read/write t
> L108: * **Two Integration Paths, One Shared Store**: Use it as a Hermes plugin, OR run it as a standalone Model Context 

## 星数曲线

```mermaid
xychart-beta
    title "codenamekt/hexus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9e8ccaae8bd8` · [字段定义](../../DATASET.md)*
