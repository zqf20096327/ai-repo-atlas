# CodNoob100/null-drift

⭐ 23 · Python · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/CodNoob100/null-drift) · 个人维护

**自托管的 AI agent 记忆状态服务：超维表示存储与召回**

实验性、自托管的记忆状态服务，面向 AI agent 开发者：由 Rust HTTP 网关（FastEmbed 嵌入 AllMiniLML6V2）、Rust 状态守护进程 nulld 与 Python 客户端原型组成。核心机制是把嵌入经随机投影映射为 10,000 维 ±1 双极向量，按 salience 加权叠加，salience≥0.90 时存入 append-only 吸引子列表，召回时用 Hamming 距离做最近匹配。提供 /inject、/recall、snapshot/restore API 与 Docker Compose 部署。README 明确声明不提供无限无损记忆、已证实的成本节省或生产安全边界；两个服务均无内置认证，基准数据为存档测量而非独立复现结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 10,000 维 HRSA 状态：确定性高斯投影、循环旋转、salience 加权叠加
- Hamming 距离吸引子匹配召回（可配 CLEANUP_THRESHOLD），可选 steps_ago 逆旋转
- 支持外部嵌入直发守护进程 /inject 的 embedding 字段
- Docker Compose 一键部署，快照/恢复用 Postcard 序列化文件

## 适用场景

- 为 AI agent 提供按 thread 隔离的自托管记忆存储与召回
- 实验超维计算（HDC）风格的状态表示与吸引子匹配
- 在可信网络内为 agent 原型挂接记忆后端

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Experimental, self-hosted memory-state service for AI agents.** The repository combines a Rust HTTP gateway, a Rus
> L12: |`nulld`|Per-thread 10,000-dimensional HRSA state, attractor matching, `/inject`, `/recall`, snapshot/restore, heal
> L14: |`nulldrift_agents.py`|Prototype synchronous/async clients using CrewAI/LangGraph-inspired interfaces; not verified

## 星数曲线

```mermaid
xychart-beta
    title "CodNoob100/null-drift 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a6207b0dde2d` · [字段定义](../../DATASET.md)*
