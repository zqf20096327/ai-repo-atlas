# MemPalace/mempalace

⭐ 59,627 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/MemPalace/mempalace) · [官网](http://mempalaceofficial.com/) · 组织维护

**给 AI 编码代理提供本地化、可溯源的会话记忆存储与语义检索**

以逐字文本存储对话历史，不做摘要或改写，通过语义搜索检索；索引按 wing/room/drawer 层级结构化以支持范围化搜索。检索后端可插拔（默认 ChromaDB），支持 Milvus、Qdrant、pgvector、SQLite、Rust 原生引擎等六种。以 CLI 与 MCP 服务器形式提供，共 47 个 MCP 工具；含时间性知识图谱、多 agent 协作日志流，以及 Claude Code、Codex CLI、Cursor IDE 的自动保存 hooks。默认路径无需 API key 与云服务，数据默认留在本地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 19,146 位贡献者
- 涨星:近 1 天 **+19**(自 20261016 起算)
- 安装:npm 包 `skills` 月下载 23,786,800
- 平台:LINUX / ANDROID · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 逐字存储 + 语义检索，默认路径零 API 调用、零云端依赖
- 可插拔检索后端：ChromaDB 默认，另支持 Milvus/Qdrant/pgvector/SQLite/Rust 原生
- 47 个 MCP 工具与结构化 wing/room/drawer 索引
- LongMemEval 基准 96.6% R@5（原始语义检索，无 LLM）可复现

## 适用场景

- 让 Claude Code 等 MCP 客户端跨会话回忆历史对话内容
- 为多 agent 系统提供本地持久记忆与协调日志
- 在离线/隐私要求环境下存储与检索 AI 会话记录

## 场景标签

`语义搜索` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.
> L22: MemPalace stores your conversation history as verbatim text and retrieves
> L264: 47 MCP tools cover palace reads/writes, knowledge-graph operations,

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `7a801314b0cb` · [字段定义](../../DATASET.md)*
