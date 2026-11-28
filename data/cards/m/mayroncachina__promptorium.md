# mayroncachina/promptorium

⭐ 4 · Dart · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/mayroncachina/promptorium) · 个人维护

**为 Claude Code/Codex 用户提供 spec 驱动的桌面 IDE，隔离运行与审查 agent 任务**

基于 Flutter 的 Linux 桌面 IDE，围绕 Claude Code CLI 与 Codex CLI 工作，本身不调用任何 API，而是以子进程方式运行用户已登录的 CLI，沿用其订阅配额。工作流以 Markdown spec 为单位：规划、审批后在独立 git worktree（pr/<slug> 分支）中逐步执行，步骤间有测试/lint 门禁与检查点，应用内完成 diff 审查、评论回传 agent、本地合并或 GitHub PR。含看板、Autopilot 并行调度、配额监控与跨提供商切换。Windows 版为实验性无官方支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条 spec 一个 git worktree，多任务并行互不干扰
- 不调用 API，直接运行已安装的 Claude Code/Codex CLI 进程
- 步骤间门禁（测试/lint/验收标准）与检查点回退
- 配额用尽时编排器自动将步骤切换到另一提供商

## 适用场景

- 在终端使用 Claude Code 的开发者想把多任务 agent 工作集中管理
- 用 spec 驱动流程约束 agent 只执行已批准的计划
- 并行推进多条 spec 并在应用内完成审查与合并

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L26: O Promptorium é uma IDE desktop, feita em Flutter, para trabalhar com o **Claude Code CLI** e, desde a 0.23, também
> L68: O Promptorium não chama nenhuma API. Cada execução é um processo do CLI do provedor, e por isso ele usa a assinatur


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `50119c62bbb1` · [字段定义](../../DATASET.md)*
