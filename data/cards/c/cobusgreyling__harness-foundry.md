# cobusgreyling/harness-foundry

⭐ 14 · TypeScript · MIT · 推送 2026-08-20 · [GitHub](https://github.com/cobusgreyling/harness-foundry) · [官网](https://cobusgreyling.github.io/harness-foundry/) · 个人维护

**面向生产 agent 的可组合 harness 运行时与 CLI 框架**

位于模型与可靠行为之间的运行时层：以声明式原语（≥25 个）组合 harness，提供四层包结构（接口层含 mock/anthropic/openai/grok 适配器、组合层、执行层含 turn loop 与沙箱、可靠性层含 trace/evolve/evidence）。提供 foundry CLI：init 脚手架、run 执行会话并写 trace、evolve 基于真实运行报告提出 stack diff（需人工审核）、host integrate 接入 Cursor / Claude Code。MIT 许可，v0.5.1，npm 安装，含 CI GitHub Action 与 devcontainer。

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

- 声明式、版本化、可替换的 harness 原语组合机制
- 四层 monorepo 包结构：interface/compose/runtime/trace-evolve
- trace 驱动的演进：evolve report→proposal，人工审核后才应用
- Cursor / Claude Code host 集成与 GitHub Action CI 门禁

## 适用场景

- 为生产 agent 搭建可复现、可追踪的执行 harness
- 从真实运行 trace 出发迭代 agent 栈配置
- 在 CI 中以 foundry-gate 运行 agent 会话做门禁

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L27: |**harness-foundry**|Execute composable harness primitives|
> L35: Model  →  Primitives  →  Runtime  →  Trace  →  Evidence
> L99: |**L3 Execution**|`runtime`|Turn loop, sandbox, control|

## 星数曲线

```mermaid
xychart-beta
    title "cobusgreyling/harness-foundry 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5b776217f74f` · [字段定义](../../DATASET.md)*
