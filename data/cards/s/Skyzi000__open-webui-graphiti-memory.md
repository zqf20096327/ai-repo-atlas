# Skyzi000/open-webui-graphiti-memory

⭐ 30 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/Skyzi000/open-webui-graphiti-memory) · 个人维护 · 中文 README

**为 Open WebUI 提供基于 Graphiti 的时序知识图谱记忆扩展**

一组部署在 Open WebUI 内的扩展组件：核心 Filter 在每轮对话前检索相关记忆注入 LLM 上下文、对话后自动抽取实体/关系/事件存入知识图谱；另有手动保存的 Action 按钮与 AI 可调用的记忆管理/只读搜索工具，并支持从 Open WebUI 内置记忆迁移。依赖 Graphiti 与 Neo4j（推荐）或 FalkorDB 后端，LLM 端点须支持 JSON 结构化输出。支持按用户隔离记忆、Redis 多实例部署与三种检索策略。

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

- Filter 自动检索记忆注入 LLM 上下文并在对话后自动保存
- 实体/关系（含时间有效性）/事件三类记忆结构
- 内置记忆迁移工具（幂等、可中断、支持 dry-run）
- 按用户隔离记忆与 Redis 多实例去重

## 适用场景

- 给自托管的 Open WebUI 加上长期记忆与历史问答
- 多用户共享知识库且按用户隔离记忆空间
- 从 Open WebUI 内置记忆迁移到知识图谱

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L7: This extension provides **temporal knowledge graph-based memory** for Open WebUI, powered by Graphiti. The core impl
> L27: 1. **Before LLM Processing**: Automatically searches for relevant memories based on the current conversation
> L133: - OpenAI-compatible LLM endpoint with JSON structured output support

## 星数曲线

```mermaid
xychart-beta
    title "Skyzi000/open-webui-graphiti-memory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-29 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c678d22ab628` · [字段定义](../../DATASET.md)*
