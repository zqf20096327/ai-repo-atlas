# damiansire/cognitive-substrate

⭐ 28 · TypeScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/damiansire/cognitive-substrate) · 个人维护

**文件系统优先的本地 agentic 任务运行器，由 Gemini 驱动**

TypeScript 编写的本地任务执行引擎：给定工作区的 goal.md 后分解为任务队列，由沙箱化的工具调用 agent 执行文件读写与 shell 命令，经确定性检查（及 LLM 校验）后写入 runs/ 证据目录。全部状态为可编辑的 markdown 文件，无 API key 时以确定性仿真模式运行。提供 CLI、Ink TUI、Angular 网页面板与审批队列；支持多工作区并行守护进程与多机协调。原生终端模式不构成安全边界，容器隔离为可选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- goal.md 分解为任务队列，agent 沙箱化执行并写入 runs/ 证据
- 全部状态为磁盘上的 markdown 文件，可人工审计编辑
- 无 API key 时以确定性仿真模式运行
- CLI/TUI/Web 面板三界面 + 审批队列与审计日志

## 适用场景

- 让 agent 在本地工作区自主分解并执行任务目标
- 以文件形式审计 agent 每次运行的证据与决策
- 多工作区并行运行带治理预算的自动化任务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: A lightweight, local, **filesystem-first agentic task runner** built in TypeScript and
> L8: tasks, executes each one with a sandboxed tool-calling agent, **verifies the result and

## 星数曲线

```mermaid
xychart-beta
    title "damiansire/cognitive-substrate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `93b487c384d2` · [字段定义](../../DATASET.md)*
