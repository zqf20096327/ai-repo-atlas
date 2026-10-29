# BuffaloTechRider/Autodidact

⭐ 20 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/BuffaloTechRider/Autodidact) · [官网](https://pypi.org/project/autodidact/) · 个人维护

**本地优先的自学习 AI agent：本地回答、不确定时升级云端并沉淀知识**

命令行 AI agent：先查本地记忆与检索结果，置信时由本地模型作答，不确定时升级到云端模型（或 Google 搜索），随后从升级结果中抽取知识存入本地记忆，下次同类问题直接从记忆回答。支持 5 种部署模式（本地+云、纯云、双本地、自定义 OpenAI 兼容服务、纯本地），通过 pip 安装，`autodidact learn` 可摄取文档与代码（tree-sitter AST 切分、BM25+向量混合检索），全部状态存于单个 SQLite 文件，含成本追踪。v1.0 尚无工具执行、代理模式与 MCP（计划 v1.5/v2.0）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 置信度路由：GSA 预筛 + logprob 不确定性 + 拒答检测，决定本地或升级云端
- 从云端回答中抽取结构化知识并去重存储，0.80+ 相似度直接命中记忆作答
- tree-sitter AST 代码切分 + BM25(FTS5)与向量检索经 RRF 融合的混合检索
- 全部状态存于单个可移植 SQLite 文件，设置后可离线运行

## 适用场景

- 用本地 agent 回答代码库和文档相关问题，减少云端 API 开销
- 让 agent 摄取内部文档后离线答疑
- 观察每次回答的本地/云端/记忆命中路径与累计节省成本

## 场景标签

`RAG` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L4: Autodidact is an AI agent with a local brain that works like a human. When asked a question or given a task, it thin
> L20: autodidact chat                    # start talking to the agent
> L122: - **Local-first.** All state in one portable SQLite file (`~/.autodidact/memory.db`). Works offline after setup.

## 星数曲线

```mermaid
xychart-beta
    title "BuffaloTechRider/Autodidact 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e3b4dc5a037f` · [字段定义](../../DATASET.md)*
