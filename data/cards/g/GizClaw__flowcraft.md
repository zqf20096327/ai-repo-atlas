# GizClaw/flowcraft

⭐ 410 · Go · MIT · 推送 2026-11-26 · [GitHub](https://github.com/GizClaw/flowcraft) · [官网](https://gizclaw.github.io/flowcraft/) · 组织维护 · 中文 README

**Go 开发者构建 AI agent 的 SDK 平台：模型调用、工具、沙箱与声明式图**

由多个独立版本化 Go 模块组成的工作区：core 提供契约（消息、模型、工具、技能、权限）与按进程运行 host；inference 提供 5 家供应商适配包；sandbox 提供 local/remote 两种执行边界及 netpolicy；agent 提供 graph（可循环的前沿循环引擎、Starlark 脚本节点）、a2a 与 SQLite checkpoint。部署由两份 YAML 文档声明，权限由调用方在开启会话时通过 policy.Grant 声明。以库嵌入 Go 服务、以 daemon 运行，examples/forge 提供狼人杀多 agent 演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 两份 YAML 部署文档 + 实现注册表，未注册实现报加载错误
- 可循环的图引擎：ReAct 循环即边，节点类型含 model/tool/condition/script
- 沙箱边界支持 local/remote 后端、netpolicy 出口匹配与单次审批
- checkpoint 以投影 + append-only 事件日志持久化任务，支持指纹校验的恢复

## 适用场景

- 在自有 Go 服务中嵌入带长期记忆与检查点的 agent
- 用声明式 YAML 组装多模型路由与工具执行流程
- 在沙箱边界内受控执行 agent 工具命令
- 运行多 agent 自对弈场景（forge 狼人杀演示）

## 场景标签

`Agent 框架` `多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L10: FlowCraft is a Go workspace for building agent deployments without tying
> L28: - **`inference`** — the protocol families and provider adapters, one package per
> L33: - **`agent`** — the engines: `graph` (nodes, script kinds, Starlark), `a2a` (client

## 星数曲线

```mermaid
xychart-beta
    title "GizClaw/flowcraft 星数(近 7 点)"
    x-axis ["2026-10-25", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-20", "2026-11-28"]
    y-axis "stars" 409 --> 415
    line [414, 413, 414, 410, 411, 410, 410]
```

2026-10-25 414 → 2026-11-28 410（-4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `e8747da75d89` · [字段定义](../../DATASET.md)*
