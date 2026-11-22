# marcus-beauregard/agent-runner

⭐ 11 · Go · GPL-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/marcus-beauregard/agent-runner) · 个人维护

**面向开发者的最小自主 agent 运行时（Go CLI）**

用 Go 编写的极简自主 agent 运行时，提供工具注册表、步数上限与运行记录（transcript）。面向仓库维护者场景：指向 issue 或 pull request，代理执行任务、运行仓库自身的检查门槛并留下可审查的运行报告。当前状态标注为 early：循环、工具注册表与命令执行器已可用，worker 大部分未实现，planner 为确定性 mock，尚未调用模型；默认入口可离线复现运行。行为规范以 PRD.md 为准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 循环：plan/act/observe/reflect
- 工具注册表与仅限 argv 的命令执行器
- 步数上限与运行记录/报告输出
- 默认 mock planner，可离线复现运行

## 适用场景

- 让 agent 处理仓库的 issue 或 PR 并留下可审查记录
- 在本地离线复现 agent 运行流程
- 作为 Go 实现的 agent 运行时进行开发与测试

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: **Status: early.** The loop, the tool registry and the command runner work. The worker is specified and mostly unbui
> L18: internal/agent/       the loop: plan, act, observe, reflect
> L29: go build -o agent-runner ./cmd/agent-runner


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `e62754588800` · [字段定义](../../DATASET.md)*
