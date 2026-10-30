# seko99/AgentWeaver

⭐ 17 · TypeScript · MIT · 推送 2026-05-27 · [GitHub](https://github.com/seko99/AgentWeaver) · [官网](https://agentweaver.site/) · 个人维护

**面向编码 agent 的工作流编排 CLI：声明式流程+可恢复执行**

TypeScript/Node.js 命令行工具，用于围绕编码 agent 做工程化封装：以 JSON 声明式 flow spec 定义阶段与步骤，运行时节点用 TypeScript 实现。提供计划→实现→审查→修复的内置流程，各阶段产出结构化 JSON 与 markdown 工件落盘，使执行可检查、可恢复、可重启。支持 Codex、OpenCode、shell、Jira、GitLab、Telegram 等执行后端，提供 TUI/Web UI/CLI 三种界面、项目本地 playbook 与插件 SDK。面向希望把 agent 工作当作可版本化工程系统来运维的团队。

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

- JSON 声明式 flow spec + 类型化运行时节点的双层模型
- 工件落盘为阶段间契约，支持 resume/continue/restart 语义
- 多执行后端：Codex、OpenCode、shell、Jira、GitLab、Telegram
- TUI/Web UI/CLI 三种界面共用同一工作流模型，含插件 SDK 与 doctor 诊断

## 适用场景

- 把 agent 的计划、实现、审查、修复组织为可审计的流水线
- 长任务中断后从指定阶段恢复执行
- 在团队仓库内沉淀项目规范供 agent 运行时引用

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: `AgentWeaver` is a TypeScript/Node.js CLI for engineering durable workflows around coding agents.
> L27: - **Multiple execution backends**: Codex, OpenCode, shell/process checks, Jira, GitLab, Git commit, and Telegram no
> L98: - `implement` — runs LLM-backed implementation based on previously approved design and plan artifacts; executes cod

## 星数曲线

```mermaid
xychart-beta
    title "seko99/AgentWeaver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `94b5ae65d756` · [字段定义](../../DATASET.md)*
