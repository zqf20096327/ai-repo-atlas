# tuvl-io/tuvl

⭐ 7 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/tuvl-io/tuvl) · [官网](https://tuvl.org) · 组织维护

**为 AI agent 提供 YAML 声明式工作流引擎与运行时**

以 YAML 声明由 agent 组成的图式工作流，每个 agent 带类型化契约（inputs/outputs/signals），由 code/tool/decide/llm/loop/map/parallel/human 等引擎实现。提供静态 lint 检查契约、数据流、类型与策略，并输出确定性与最坏 token 成本；运行可持久化、可恢复、可暂停、可回放为零 token 测试固件。通过 REST/SSE/MCP 暴露工作流，附带 Insight 开发控制台、CLI、Ed25519 JWT 认证与可选 Postgres 多租户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 类型化契约与静态 lint，零 token 检查工作流
- 可持久化、可 journaled 的运行时，支持暂停/步进/回放
- 通过 MCP 暴露工作流并可为 coding agent 提供操作接口
- CLI、Insight 控制台、REST/SSE/T TypeScript 客户端多面呈现

## 适用场景

- 用 YAML 编排多 agent 工作流并加入人工审批环节
- 让 coding agent 按契约生成代码并通过 CI 门禁验证
- 需要可恢复、可审计的长时 agent 任务运行时

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L16: A tuvl workflow is a graph of **agents**. Each agent has a typed contract — `inputs`, `outputs`, the
> L31: Signals route to the next agent or a named end. `tuvl lint project` checks contracts, data flow, types
> L51: `tuvl` alone is the engine and the production CLI: it parses the YAML, talks to the database and serves the API
> L106: - **REST + SSE:** each workflow's route, `POST /api/workflows/{name}/runs`, runs, journal events,

## 星数曲线

```mermaid
xychart-beta
    title "tuvl-io/tuvl 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 6 --> 8
    line [7, 7]
```

2026-11-08 7 → 2026-11-28 7（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `7b3040bb77d7` · [字段定义](../../DATASET.md)*
