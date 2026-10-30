# hieuchaydi/DecisionGraph

⭐ 16 · Python · 推送 2026-04-25 · [GitHub](https://github.com/hieuchaydi/DecisionGraph) · [官网](https://docs-decisongraph-01.vercel.app/) · 个人维护

**工程决策记忆系统：留存变更理由证据，供 CLI/API/MCP 查询**

面向软件团队的决策记录与查询系统：从本地文件、Git 历史、GitHub PR/Issue、Slack/Jira 导出、JSONL 流摄取证据，构建带溯源的决策库；支持 why/who/when 查询（附置信度与警告）、supersede/merge 决策演进流程、矛盾检测、基于实时指标的过期假设检测与告警、治理模式与变更前 guardrail。同一决策记忆通过 CLI、FastAPI HTTP API 与 stdio MCP server 三种方式暴露，可作为 MCP 工具接入 agent；另含 docs 前端（npm 运行）与可选 Groq 模型集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多源证据摄取（文件/Git/GitHub/Slack/Jira/JSONL）
- 决策查询附置信度、矛盾检测与证据质量评分
- CLI + HTTP API + MCP stdio 三种暴露方式
- 假设看护与变更前 guardrail 检查

## 适用场景

- 团队留存并追溯架构决策的 why 证据链
- 高风险重构前跑 guardrail 检查历史决策冲突
- 通过 MCP 让 agent 查询团队决策记忆
- 监测决策所依据的假设是否随指标过期

## 场景标签

`知识库管理` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Engineering Decision Memory System with `CLI + API + MCP`, plus a docs frontend in `docs`.
> L138: ## MCP Server (stdio)
> L341: ## MCP Tooling

## 星数曲线

```mermaid
xychart-beta
    title "hieuchaydi/DecisionGraph 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `65b311dd0dc8` · [字段定义](../../DATASET.md)*
