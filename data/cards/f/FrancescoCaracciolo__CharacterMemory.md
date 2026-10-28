# FrancescoCaracciolo/CharacterMemory

⭐ 26 · Python · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/FrancescoCaracciolo/CharacterMemory) · 个人维护

**为 LLM 角色提供类人记忆（记住/遗忘/情感）的库与服务器**

面向角色扮演与陪伴型 LLM 应用的记忆系统，提供 pip 库、FastAPI 服务器、MCP 端点、HTTP API 与 Web 界面四种接入方式。内置 10 类可开关的记忆系统（事实、情节、情感、世界状态、日程、用户摘要等），召回基于 Embeddings+BM25 并叠加情感强度、位置、新旧与频率；每 5-10 轮由 LLM 抽取记忆并去重，另有知识图谱检索（Self/Person/Episode/Fact/Location/Entity 节点）。通过 OpenAI 兼容 /v1 端点连接任意聊天与嵌入模型；知识图谱需额外 LLM 调用。WebUI 与服务器代码声明为 AI 生成并经人工审阅，核心代码为人工编写。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 10 类内置记忆系统，含情感跟踪与世界状态（位置/作息/饥饿/精力）
- Embeddings+BM25 召回叠加情感强度、位置、新旧与回忆频率
- 知识图谱检索（6 类节点，边映射情感与关系）
- 提供 pip 库 / MCP server / HTTP API / WebUI 四种使用方式

## 适用场景

- 为角色扮演或陪伴型聊天 AI 添加长期记忆与遗忘机制
- 通过 MCP 客户端（Claude Desktop、Cursor 等）读写角色记忆
- 在 Web 界面创建角色、浏览记忆并探索知识图谱

## 场景标签

`Agent 记忆` `知识图谱` · 领域:Agent 开发

## 证据(README 行号)

> L69: **Character Memory is both a library for developers and a ready-to-integrate tool for third party applications**
> L72: - MCP server, to integrate tools to read and edit memory into Agents

## 星数曲线

```mermaid
xychart-beta
    title "FrancescoCaracciolo/CharacterMemory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-28 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9a8cebfde4fa` · [字段定义](../../DATASET.md)*
