# streetrace-ai/streetrace

⭐ 38 · Python · MIT · 推送 2026-04-13 · [GitHub](https://github.com/streetrace-ai/streetrace) · [官网](https://streetrace.ai/) · 组织维护

**用 DSL 定义与运行结构化多智能体系统的开源运行时**

Python 实现的开源运行时加 DSL：以显式定义与受控交互的方式编排多智能体系统，可在本地、Docker 或 CI/CD（如 GitHub Actions）中运行。提供约束处理器做执行防护、内置文件系统/CLI/搜索等沙箱化工具，DSL 中绑定模型（如 anthropic、openai）。面向开发者与平台工程师构建结构化 agent 系统和自动化工作流。README 声明暂不包含评估框架、agent 生命周期版本管理与集中策略面，属路线图项；约束处理为进行中但可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- DSL + Python 抽象定义 agent，执行语义显式
- 本地、Docker、CI/CD（GitHub Actions）多种运行环境
- 约束处理器提供执行防护（进行中但可用）
- 内置工具均在工�作目录沙箱内运行

## 适用场景

- 在 CI/CD 流水线中运行自定义 agent 完成自动化任务
- 以显式 DSL 构建受控交互的多智能体工作流
- 本地开发流程中交互式运行 agent

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Open runtime and DSL for structured multi-agent systems**
> L5: Streetrace is an open-source runtime that lets you define and execute structured multi-agent systems anywhere Python
> L11: * **Explicit agent definitions** via a simple DSL and Python abstractions

## 星数曲线

```mermaid
xychart-beta
    title "streetrace-ai/streetrace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `183c9c74b9e7` · [字段定义](../../DATASET.md)*
