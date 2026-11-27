# matrixarkai/TemporalStore

⭐ 212 · Rust · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/matrixarkai/TemporalStore) · [官网](https://github.com/matrixarkai/TemporalStore) · 组织维护

**Rust 存储引擎：为 LLM 上下文与在线特征提供统一服务**

用 Rust 编写的存储引擎，将特征服务与 LLM 上下文作为一等工作负载：支持最新值查询、长序列与高基数聚合、WindowReduce 特征、频次上限、风控状态，以及会话/实体记忆的上下文摄取、检索、排序与按 token 预算打包。提供 Feast 原生 provider（在线存储与物化目标，不含离线训练存储与向量检索），并可作为 LMCache 的 L2 存储层配合 vLLM 复用 KV 块。通过数据节点运行，附 Python 集成与 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Feast 原生在线存储 provider，支持最新值、TTL、历史保留与 teardown 跟踪
- 作为 LMCache 的 L2 存储层，跨 vLLM worker 复用 prompt KV 块
- LLM 上下文管理：检索、排序与 token 预算打包
- 控制状态、频次上限与风控判定等在线状态操作

## 适用场景

- 为推荐、搜索、广告系统提供在线特征查询
- 给 agent 与 LLM 应用管理会话记忆并组装上下文
- 配合 Feast 做特征物化与在线读取
- 为 vLLM 部署提供跨请求的 KV 缓存二级存储

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Open-source Rust storage for online features, LLM context, and control state.**
> L43: |**LLM context and agent memory**|Conversations, resources, entities, reusable memory, retrieval, and token-budgete
> L49: TemporalStore provides an L2 storage tier for LMCache. vLLM's

## 星数曲线

```mermaid
xychart-beta
    title "matrixarkai/TemporalStore 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 211 --> 213
    line [212, 212]
```

2026-10-25 212 → 2026-11-27 212（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `f0cc8bf95f45` · [字段定义](../../DATASET.md)*
