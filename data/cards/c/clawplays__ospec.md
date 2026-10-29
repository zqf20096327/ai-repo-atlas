# clawplays/ospec

⭐ 391 · JavaScript · MIT · 推送 2026-08-26 · [GitHub](https://github.com/clawplays/ospec) · [官网](https://ospec.ai) · 组织维护 · 中文 README

**面向 AI 编码代理的规格驱动工作流框架**

以 npm 包 @clawplays/ospec-cli 分发的 CLI 工具，将需求转化为仓库内的持久化工件（proposal、plan、tasks、review、verification evidence），形成 plan → act → verify 的可验证目标循环。支持 Claude Code、Codex、Gemini、OpenCode 及纯 CLI 工作流；提供轻量 change 流与带代理控制器层的 goal 流（并行 worker 调度、评审门禁、心跳与恢复）。要求 Node.js 18+ 与 npm 8+，生成的文档语言可选 en-US/zh-CN/ja-JP/ar。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 需求转为仓库持久化工件（proposal/plan/tasks/review/verification）
- ospec change 轻量流与 ospec goal 带控制器层的 goal 流
- 多代理适配：Codex spawn_agent、Claude Code Task 轮询、Gemini @generalist、OpenCode @mention
- ospec loop 系列命令管理并发、心跳、恢复与证据提交

## 适用场景

- 让 AI 编码助手按可审计的规格流程交付需求
- 跨会话/跨助手续接未完成的工作（上下文存于仓库）
- 对高风险需求运行带独立评审与验证证据的完整 goal 流程

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: The official OSpec CLI package is `@clawplays/ospec-cli`, and the official command is `ospec`. OSpec is a spec-driv
> L31: - **Spec-driven work, saved to your repo** — OSpec turns a request into files (proposal, design, plan, tasks, revie

## 星数曲线

```mermaid
xychart-beta
    title "clawplays/ospec 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-29"]
    y-axis "stars" 390 --> 397
    line [396, 391, 391]
```

2026-10-18 396 → 2026-10-29 391（-5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b0142e281fdf` · [字段定义](../../DATASET.md)*
