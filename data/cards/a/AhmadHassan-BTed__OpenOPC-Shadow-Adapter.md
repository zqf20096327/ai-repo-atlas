# AhmadHassan-BTed/OpenOPC-Shadow-Adapter

⭐ — · [GitHub]() · 个人维护

**为 OpenOPC agent DAG 提供非阻塞人工审批与 BYOC 远程算力的适配器**

面向 OpenOPC agentic DAG 运行时的零核心修改扩展：以 <50ms 拦截任务并写入隔离 SQLite WAL 数据库返回 AWAITING_HUMAN，释放执行线程避免引擎超时；提供 React 19 审批门户（shadow-serve）、JWT 多用户鉴权、最多 5 文件/50MB 附件的交付物提交与不可变审计日志，交付后直接恢复 OpenOPC 原生 store.db 状态机。另含 shadow-worker 守护进程，允许远程 GPU 节点用本地模型（如 Ollama）或自有 API key 执行角色任务（BYOC），并集中登记交付物做层级上下文继承。以 PyPI 包提供，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- <50ms 非阻塞拦截，任务驻留独立 SQLite WAL 库，避免引擎超时
- shadow-worker 支持远程 GPU 节点自带模型/API key 执行角色（BYOC）
- 交付物集中登记（SHA-256 校验）与层级上下文注入
- 零核心修改接入 OpenOPC 外部 agent 注册表

## 适用场景

- OpenOPC DAG 中需要人工签核的节点异步审批而不阻塞并行分支
- 把远程 GPU 机器接入为按角色执行推理的算力节点
- 满足 SOC 2 / GDPR 等要求的人工签核审计留痕

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L21: `openopc-shadow-adapter` is a high-concurrency **Temporal Bridge** for OpenOPC. It allows OpenOPC agentic DAGs to p
> L27: 5. **Symbiotic Architecture**: Functions as an independent, non-invasive extension that plugs into OpenOPC's extern

## 星数曲线

```mermaid
xychart-beta
    title "AhmadHassan-BTed/OpenOPC-Shadow-Adapter 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 189 --> 1920
    line [333, 1776, 1776]
```

2026-10-18 333 → 2026-10-21 1,776（+1,443）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5c646ad16355` · [字段定义](../../DATASET.md)*
