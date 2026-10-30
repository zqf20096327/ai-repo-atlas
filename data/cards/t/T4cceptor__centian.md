# T4cceptor/centian

⭐ 16 · Go · Apache-2.0 · 推送 2026-07-03 · [GitHub](https://github.com/T4cceptor/centian) · [官网](https://centian.ai) · 个人维护

**面向生产 AI agent 的 MCP 控制平面：审计、防护与执行验证**

构建于 MCP 协议之上的 agent 控制平面，部署在 agent 与其访问的文件系统/API/数据库之间。提供四类机制：全量工具调用审计（含任务关联的事件持久化与只读检查 UI）、进出双向的运行时上下文与动作防护（含提示注入检测）、基于冻结执行契约的流程验证、按阶段工具白名单与不可逆操作门控的爆炸半径管理。另有 MCP 网关聚合、项目级隔离、可编程 processor 链与 API key 鉴权。面向将 agent 部署到生产并需审计合规的工程师；pre-1.0，任务运行状态仅内存保存、UI 只读等限制已列明。以 shell 脚本、二进制、go install、Docker 方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 全量工具调用捕获并关联到任务，支持 SQLite/PostgreSQL 持久化与回放检查
- 运行时双向防护：管住进入上下文的输入与离开上下文的破坏性调用
- 冻结执行契约 + 按阶段工具白名单与不可逆操作门控
- MCP 网关聚合、项目级隔离与可编程 processor 链

## 适用场景

- 生产环境 agent 的动作审计与合规取证
- 阻止 agent 调用未批准或破坏性工具
- 按预定义契约验证 agent 执行是否偏离计划

## 场景标签

`LLM 可观测性` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L20: Centian is the layer that sits between your agents and the systems they touch — capturing every action, enforcing w
> L160: - MCP proxy with gateway aggregation and tool namespacing

## 星数曲线

```mermaid
xychart-beta
    title "T4cceptor/centian 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a40f07694930` · [字段定义](../../DATASET.md)*
