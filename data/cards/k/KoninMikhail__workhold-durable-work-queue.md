# KoninMikhail/workhold-durable-work-queue

⭐ 11 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/KoninMikhail/workhold-durable-work-queue) · 个人维护

**给多副本应用提供持久化后台任务队列与运维能力**

以 PostgreSQL 为存储的每应用持久化任务队列服务，覆盖命名队列、幂等入队、fenced 租约、重试与死信、complete+spawn 原子后续任务、暂停/排空/检查等运维功能。服务以容器镜像分发，按 api/migrate/maintain/relay/apply 角色部署；应用侧按生产者/消费者/管理者三种 Python 客户端接入，依赖 Python 3.13+ 与 PostgreSQL 18。明确声明 at-least-once 而非 exactly-once 语义。

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

- fenced 可续期租约下的多副本安全争抢任务
- complete 与 spawn 后续任务在同一事务提交
- 版本化重试策略、结构化失败码与死信状态
- 按角色拆分的 Python 客户端（producer/consumer/admin）

## 适用场景

- 把 CPU/IO 密集的后台任务安全分发到多个副本
- 多阶段处理中原子地生成下一阶段任务
- 无自有数据库的应用直接入队获得持久存储
- 检查任务历史、重放死信、暂停或排空队列

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: **A durable Work Queue for applications that run across multiple replicas.**
> L22: message bus. It combines idempotent intake, fenced leases, retries, follow-up
> L178: Workers process tasks **at least once**. If a lease is lost, another worker may


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `27a1a731a71c` · [字段定义](../../DATASET.md)*
