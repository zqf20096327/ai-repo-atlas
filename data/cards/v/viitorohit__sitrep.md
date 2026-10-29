# viitorohit/sitrep

⭐ 19 · HTML · MIT · 推送 2026-07-17 · [GitHub](https://github.com/viitorohit/sitrep) · [官网](https://getsitrep.dev) · 个人维护

**给 AI 编码工具的项目状态与成本跟踪层：续接、记账、提示**

以仓库内 markdown、JSON 与零依赖 CLI 形式存在的连续性/成本/提示层，供 Claude Code、Codex、Cursor 等工具共用：会话开始读取项目所处阶段与进度，会话结束记录 token、成本、决策并提交到 git；Git 即数据库，无需额外服务或账号。通过 npx getsitrep init 向导配置计划来源（本地/Jira/OpenSpec/Spec Kit）与钩子，自动触发会话跟踪；另提供成本归因报告与自包含 HTML 仪表盘。Copilot/VS Code 尚未覆盖。

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

- 会话级 token/成本/决策记录，按阶段、票据、模型归因（report 命令）
- 适配 Claude Code/Cursor/Codex 的 SessionStart/SessionEnd 钩子自动触发
- 零依赖 Node.js CLI，8 个命令可在终端/CI/任意工具中运行
- 生成自包含 HTML 仪表盘（进度、成本、会话、决策、风险等 10 个板块）

## 适用场景

- 在多个 AI 编码工具间切换时保留项目进度与上下文
- 查看每个功能特性在 token 与美元成本上的实际开销
- 向同事或下一个 AI 会话交接上下文（/handoff）
- 向干系人输出可视化项目仪表盘

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L5: **The continuity, cost, and nudge layer for agentic AI coding — works with Claude Code, Codex, Cursor, or any tool t
> L15: **sitrep** lives inside your repo as plain markdown, a small JSON file, and a zero-dependency CLI. Whichever AI too
> L61: as callable functions — usable from a bare terminal, a CI job, or any AI

## 星数曲线

```mermaid
xychart-beta
    title "viitorohit/sitrep 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7ef858027614` · [字段定义](../../DATASET.md)*
