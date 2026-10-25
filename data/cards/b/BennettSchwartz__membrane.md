# BennettSchwartz/membrane

⭐ 95 · Go · MIT · 推送 2026-09-05 · [GitHub](https://github.com/BennettSchwartz/membrane) · [官网](https://membrane.gustycube.com/) · 个人维护

**给 LLM agent 提供持久化、可修订结构化记忆的存储层**

Membrane 为 LLM agent 提供持久、结构化的记忆基底：以 Go 库嵌入或 gRPC daemon 方式接入（含 TypeScript/Python SDK 与 OpenClaw 插件）。记忆分为情景、工作、语义、能力、计划图五层，通过实体链接连接，检索返回有界的关联图。支持事实修订（取代/质疑/分叉/撤回并保留审计历史）、强化与衰减机制、按范围与敏感度策略的读写控制。必需 PostgreSQL + pgvector；嵌入与 LLM provider 为可选，无模型 API key 时结构化捕获、图检索、修订与访问控制仍可用。

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

- 五层类型化记忆（情景/工作/语义/能力/计划图）经实体链接互连，检索返回有界图
- 知识可修订：取代、质疑、分叉、撤回并保留审计历史
- 强化、衰减与整合机制影响后续记忆与检索
- 作用域与敏感度策略控制读写，受限响应按权限脱敏
- Go 嵌入库 / gRPC daemon / TS、Python SDK / OpenClaw 插件多种接入方式

## 适用场景

- 让跨会话工作的 agent 保留并连接历史上下文
- 维护会变化的事实并在情况改变时纠正知识
- 复用以往成功的过程性经验（competence 记忆）
- 解释某条回答由哪些记忆支撑

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L16: Membrane gives LLM agents persistent, structured memory. An agent can remember
> L61: |**Go**|Embed the library in your process|Go guide · Package reference|

## 星数曲线

```mermaid
xychart-beta
    title "BennettSchwartz/membrane 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-25 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `901f5008f40e` · [字段定义](../../DATASET.md)*
