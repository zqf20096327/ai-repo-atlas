# feather-store/feather

⭐ 11 · Python · MIT · 推送 2026-11-12 · [GitHub](https://github.com/feather-store/feather) · [官网](https://featherdb.si/) · 组织维护

**嵌入在 Agent 内部的单文件向量记忆库与上下文引擎**

以单个 .feather 文件运行的内嵌向量存储，无服务器、无守护进程、无网络调用，为 agent 提供记忆层：自适应衰减（按召回次数调整老化速度）、信任/置信度过滤、带预算的热集工作区、缺失必需约束时失败关闭的上下文包、按记录 ttl 过期。提供 Claude Desktop/Code 的 MCP 服务器、LangGraph BaseStore 集成、Cloud API（含 admin SPA）与多类嵌入服务接入。限制：无事务、无查询规划器、每文件单写入者，元数据预过滤仅支持等值匹配。

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

- 单文件嵌入式存储：无服务器、无守护进程、进程内运行
- 记忆语义：自适应衰减、信任/置信度、ttl 过期、上下文包失败关闭
- HNSW 持久化图与预过滤 ANN 搜索、int8 磁盘/内存量化
- MCP 服务器对接 Claude，LangGraph BaseStore 一行接入

## 适用场景

- 为 agent 提供跨线程的持久记忆存储
- 管理带时间语义（valid_at、time travel）的结构化 agent 记忆
- 自托管为下游团队的托管上下文引擎
- 在受限资源环境用 int8 量化降低内存与文件体积

## 场景标签

`Agent 记忆` `向量数据库` · 领域:Agent 开发

## 证据(README 行号)

> L20: Feather is the memory layer that runs **inside** your agent — not a database you
> L22: hop. It is an embedded vector store with the things a memory actually needs:
> L50: Integrations that already exist: an **MCP server** for Claude Desktop and Claude


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `4bff7a614e1e` · [字段定义](../../DATASET.md)*
