# BusyBee3333/sol-governed-codex

⭐ 40 · Shell · MIT · 推送 2026-08-01 · [GitHub](https://github.com/BusyBee3333/sol-governed-codex) · 个人维护

**OpenAI Codex 插件：Sol 顾问门控的多智能体编码与审查工作流**

面向 OpenAI Codex 的可安装工具包，定义 Terra 根代理、Terra/Luna 工作代理与 Sol 顾问三种角色：Luna 处理机械编辑、Terra 处理需判断的有界任务、Sol 仅在涉及架构/安全/计费等风险场景做计划评审与最终证据审查，返回 PASS/REVISE/BLOCKED 机器可扫描裁决。配置模板限制委托层级为 1 层、并发 3 线程；提供全局安装器、项目契约安装与离线校验脚本，支持 gpt-5.6 系列模型并可自定义。限制：仅为本地配置与校验器，非托管编排服务，不保证正确性或更低开销。

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

- Terra/Luna 工作代理经 Sol 证据门控的路由架构（深度 1、并发 3）
- Sol 输出 PASS/REVISE/BLOCKED 结构化裁决
- v1.1 将核心指令从 1,502 词减至 893 词并设 1,100 词上限
- 提供全局安装器、项目契约安装与 validate_setup.sh 校验脚本

## 适用场景

- 在 Codex 中按任务复杂度路由不同模型以控制 LLM 成本
- 对架构、安全、计费等高风险改动引入结构化 AI 代码审查门
- 以多代理分工处理可分界的编码任务

## 场景标签

`多智能体` `编码 Agent` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L8: Get stronger review where it matters without running the most capable model for every edit. Sol-Governed Codex is an
> L25: Requirements: Git, Bash, Python 3.11 or later, and an OpenAI Codex installation with access to the configured model
> L135: The agent TOML files define `sol_advisor`, `terra_worker`, and `luna_worker`. Both named profiles set `max_depth =

## 星数曲线

```mermaid
xychart-beta
    title "BusyBee3333/sol-governed-codex 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-28 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `40815041b07e` · [字段定义](../../DATASET.md)*
