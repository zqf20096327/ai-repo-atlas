# jishmisc28/autonmis-snowflake-agent-kit

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-16 · [GitHub](https://github.com/jishmisc28/autonmis-snowflake-agent-kit) · 个人维护

**为自主 AI agent 提供 Snowflake 连接池与前缀缓存稳定化**

面向多轮 Snowflake Text-to-SQL 场景的集成层 Python 库，解决两类运行问题：一是 agent 每轮注入时间戳等非确定内容导致 LLM 前缀缓存失效、重复计费，二是无状态执行器逐条开连接引发仓库并发与 credit 消耗。机制包括 SHA-256 配置键控的多租户连接池（每仓库并发上限 10）、流式结果回传、表/列规范排序保证前缀哈希一致，以及将易变上下文隔离到未缓存尾部。提供内置测试套件，采用 Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SHA-256 键控连接池，跨多租户会话安全共享且不泄露凭据
- 字节级规范化排序保证提示前缀哈希逐轮一致
- 易变尾部隔离：时间戳/UUID/重试载荷置于未缓存后缀
- 流式结果输出带背压处理，避免结果集占满内存

## 适用场景

- 让 LangGraph/AutoGen 等 agent 框架反复查询企业 Snowflake 数仓
- 降低多轮 Text-to-SQL 会话的 token 与 Snowflake credit 消耗
- 多 worker 并行查询时控制仓库连接数与自动扩容

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L8: Production-grade Snowflake integration layer for autonomous AI agents, combining **connection-pooled query streaming
> L14: When conversational LLM agents (LangGraph, AutoGen, CrewAI, PydanticAI) query enterprise Snowflake data warehouses,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `bee4d767243a` · [字段定义](../../DATASET.md)*
