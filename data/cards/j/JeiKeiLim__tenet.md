# JeiKeiLim/tenet

⭐ 94 · TypeScript · 推送 2026-10-19 · [GitHub](https://github.com/JeiKeiLim/tenet) · 个人维护

**面向 12+ 小时自主开发周期的跨平台 AI agent 编排框架**

Tenet 是包裹在 AI 编码 agent（Claude Code、OpenCode、Codex）外层的 harness：通过访谈生成规格说明，将工作分解为依赖图（DAG），按模型能力分级（frontier/local）调整计划粒度，逐个执行任务并用独立批评者（3 个内置 + 可自定义）评估后推进，支持 12+ 小时长时运行、崩溃恢复与中途重定向。项目知识（.tenet/project/）在运行间自我更新。以 npm 全局安装提供 CLI 与 MCP Server（19 个工具）。升级到 26.6.0 之后版本含一次性的破坏性迁移。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 访谈→规格→DAG 分解→执行→独立批评者评估的自主循环
- 按 model_tier（frontier/local）自适应调整计划粒度
- grounded/ungrounded 双类独立批评者及可配置自定义批评者
- 12+ 小时自治、server-ID 崩溃恢复、心跳停滞检测

## 适用场景

- 让 AI 编码 agent 长时间自主完成多任务特性开发
- 对 AI 产出代码做独立于实现者的规格符合性评审
- 在项目中途通过 steer 消息调整 agent 工作优先级

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: AI coding agents are powerful but short-lived — they lose context, drift off-spec, skip tests, and can't hold a mult
> L26: - **Agent-agnostic.** Claude Code, OpenCode, and Codex. Switch agents mid-project without losing state.
> L120: Four layers: **Core** (DAG execution, heartbeat stall detection, retry, server-ID crash recovery) · **Adapters** (

## 星数曲线

```mermaid
xychart-beta
    title "JeiKeiLim/tenet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 93 --> 96
    line [95, 94, 94]
```

2026-10-18 95 → 2026-10-25 94（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7b479f06dfbe` · [字段定义](../../DATASET.md)*
