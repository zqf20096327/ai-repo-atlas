# memoryoss/memwire

⭐ 13 · Python · Apache-2.0 · 推送 2026-05-01 · [GitHub](https://github.com/memoryoss/memwire) · [官网](https://memwirelabs.ai/) · 组织维护

**自托管的 AI 记忆基础设施层：给 AI 应用持久化可审计记忆**

面向 AI 应用开发者的开源记忆基础设施：以结构化、可更新的事实形式存储记忆，基于图式记忆实现对话与知识的语义检索，支持文档摄取（PDF/Excel/CSV 等）与对话记忆联合召回。记忆条目可追溯并分类（事实/偏好/指令/事件/实体），带反馈回路强化有效记忆路径。可自托管于本地、私有云或离线环境；向量库与 LLM 提供方均可自选，支持多租户隔离。提供 pip 安装的 Python SDK 与基于 FastAPI 和 Qdrant 的自托管 REST API。

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

- 图式记忆与结构化可更新事实的持久存储
- 支持自选向量库与 LLM 提供方，可离线部署
- 文档摄取与对话记忆在查询时联合召回
- 记忆可审计可追溯，带反馈回路与边衰减机制

## 适用场景

- 给 AI agent 或助手加持久记忆，跨会话记住用户偏好与事实
- 在私有环境自托管记忆层并自选 LLM 和数据库
- 把企业文档与对话记忆统一召回为上下文

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: > Enterprise-grade, self-hosted AI memory infrastructure layer. Deploy persistent AI memory on-premise or in any clo
> L16: MemWire is **an open source & enterprise-ready** AI memory infrastructure layer. MemWire gives your AI applications

## 星数曲线

```mermaid
xychart-beta
    title "memoryoss/memwire 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b586650ec170` · [字段定义](../../DATASET.md)*
