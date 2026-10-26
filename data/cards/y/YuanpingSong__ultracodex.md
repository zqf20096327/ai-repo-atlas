# YuanpingSong/ultracodex

⭐ 65 · TypeScript · Apache-2.0 · 推送 2026-09-08 · [GitHub](https://github.com/YuanpingSong/ultracodex) · [官网](https://www.npmjs.com/package/ultracodex) · 个人维护

**让 Claude Code 工作流脚本跑在 Codex 等订阅上的编排运行时**

以 JavaScript 编写 Agent Script，像调用函数一样调用 agent()（支持 schema 结构化返回），同一脚本可不经修改运行在 Codex、Claude 或 OpenCode 三种后端，由配置中的 [route] 路由。三大支柱：工作流（并行 fleet、pipeline、预算上限）、cron 调度器、以及实验性的常驻 agent 组织（目录树 + 分层记忆摘要）。提供全屏 TUI 观察运行，附带教学 skill、九个示例脚本与 10 断言的后端一致性套件。需 Node ≥ 20 与已认证的 Codex CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent() 作为编程单元，一份脚本跨 Codex/Claude/OpenCode 三后端可移植运行
- cron 调度器与 token 预算上限（schedule add 无预算会警告）
- 实验性 Orgs：目录树组织的常驻 agent，分层记忆与逐条来源审计
- 结构化输出多级保障：后端原生 schema → 提示契约降级 → 引擎侧 ajv 校验与修复

## 适用场景

- 把任务扇出给并行 agent fleet 并拿回一份经验证的结果
- 用 cron 定时自动运行工作流（如每 30 分钟摘要、每日回顾）
- 让 Claude Code 代写工作流脚本，重活跑在 Codex 订阅上
- 搭建按目录组织、带记忆的研究型 agent 组织

## 场景标签

`多智能体` `工作流自动化` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: The idea underneath: the **agent is a unit of programming**. You write ordinary JavaScript and call an agent like a
> L41: Run from **your project's root** — agents work in your cwd. `--json` blocks and prints the result (the machine path

## 星数曲线

```mermaid
xychart-beta
    title "YuanpingSong/ultracodex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-26 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `3e9240a7eaf3` · [字段定义](../../DATASET.md)*
