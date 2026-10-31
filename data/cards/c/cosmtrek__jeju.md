# cosmtrek/jeju

⭐ 27 · Go · MIT · 推送 2026-07-31 · [GitHub](https://github.com/cosmtrek/jeju) · [官网](https://jeju.rickoyu.com) · 个人维护

**有界 AI agent 的声明式本地运行时：一份 manifest 定义并运行 agent**

用单个 YAML manifest 声明 agent 的模型提供方、指令、运行循环、工作区、工具、权限、上下文预算与评估器，运行时加载校验并编译为 CompiledAgent 后无头执行，每次工具调用经过策略门，全部效应追加记录到 trajectory.jsonl 并可派生 report.html 查看。支持内容寻址的 agent 包分发、lead-worker 的 AgentTeam 模式，以及基于任务集评分的 jeju evolve 配置空间搜索（pareto/hillclimb 两种策略，HotpotQA 上有 +3.6pp F1 结果）。面向需要可审计、可复用 agent 的开发者，以 Go 实现的 CLI 提供，README 自述实验性、Windows 未保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 manifest 声明 agent 全契约，无头运行并强制工作区/工具/权限/沙箱边界
- canonical 追加式 trajectory.jsonl 记录全部运行效应并派生 report.html
- jeju evolve 基于评估证据做配置空间搜索改进 agent
- 内容寻址 agent 包与 AgentTeam lead-worker 协作模式

## 适用场景

- 把高频本地任务（代码审查、bug 修复）封装为可复现的有界 agent
- 为 agent 实验与评测搭建带权限边界和完整轨迹记录的 harness
- 打包并分发可被其他 agent 按稳定引用调用的专用 agent

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L10: Jeju is to an AI agent what a Kubernetes manifest is to a deployment: you
> L17: Jeju is **not** an interactive coding assistant and **not** a Python agent
> L18: framework. It is the layer below those: a way to capture a workflow as a

## 星数曲线

```mermaid
xychart-beta
    title "cosmtrek/jeju 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-31 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `2b374a89690e` · [字段定义](../../DATASET.md)*
