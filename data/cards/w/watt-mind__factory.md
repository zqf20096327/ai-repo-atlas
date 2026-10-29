# watt-mind/factory

⭐ 19 · JavaScript · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/watt-mind/factory) · [官网](https://watt-mind.github.io/factory/) · 组织维护

**驱动编码 Agent 的自主开发循环运行时（自改进工厂）**

面向已在使用编码 Agent 的开发者，factory 提供围绕 Agent 的流程运行时：以任务追踪器为控制平面（Linear/GitHub Issues），git 为事实源，CI 加审查为合并门禁。每张工单在一个独立 worktree 中派给一个 Agent，完成后由 factory 重跑验证命令，测试通过且审查者批准才合并。支持 Claude Code、Codex、Gemini/Antigravity、Cursor、Pi 及经 ACP 接入的 Hermes Agent，并提供 Operator Web 控制台。自述为年轻软件，首个提交于 2026-08-03。运行需 Bun 1.3+、Git 2.40+ 与 GitHub CLI（macOS 13+/Linux x64/arm64）。采用 Apache-2.0 开放内核，ee/ 目录预留企业扩展位置（当前仅文档）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一工单一 worktree 单 Agent 的滚动派发，验证命令由 factory 自行重跑
- 控制平面适配器支持 Linear、GitHub Issues 与内存模式
- 7 种编码 Agent 框架的原生 harness 打包（SKILL.md 共享工作流格式）
- Web Operator UI 展示运行时事件图与工单旅程

## 适用场景

- 让已有的编码 Agent 在受控流程中自主认领并完成工单
- 通过 CI 与审查门禁约束 Agent 产出，防止未经验证的合并
- 以 starter 脚手架 fork 组织自己的 factory 实例并跟踪共享内核

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12: A runtime for self-improving agentic loops. Code is the first product line.
> L19: factory drives the coding agents you already use — Claude Code, Codex, Gemini
> L20: / Antigravity, Cursor, Pi, and Hermes Agent via ACP. The tracker is the control

## 星数曲线

```mermaid
xychart-beta
    title "watt-mind/factory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b86a288fdf9f` · [字段定义](../../DATASET.md)*
