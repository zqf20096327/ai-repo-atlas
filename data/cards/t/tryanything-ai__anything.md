# tryanything-ai/anything

⭐ 313 · Rust · 推送 2026-06-04 · [GitHub](https://github.com/tryanything-ai/anything) · [官网](https://tryanything.xyz) · 组织维护

**Rust 编写的全栈 AI 自动化工作流框架，面向用户**

Anything 是用 Rust 编写的全栈 AI 自动化框架，提供拖拽式 Workflow Studio（ReactFlow 编辑器、json-schema 配置）、基于 Axum 的 Workflow REST API、持久化任务队列处理（支持 Cron 触发）、用户与团队认证计费（Supabase + Postgrest），以及工作流/动作模板市场。动作类型由 WASM 插件定义，可用任意可编译到 WASM 的语言编写。架构目标包括以人类可读介质存储状态与日志以支持低成本 LLM 自主编写。安装方式为 git clone 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拖拽式工作流编辑器（ReactFlow + json-schema-form）
- WASM 插件体系定义动作类型，支持社区插件
- Supabase/Postgrest 驱动的 API、任务队列与认证计费
- 工作流与动作模板市场

## 适用场景

- 搭建带 AI 能力的自动化工作流并按计划触发执行
- 通过模板市场复用社区工作流
- 用任意语言编写 WASM 插件扩展动作类型

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3:  If Posthog built Zapier. Feature complete, Fullstack, AI Automation framework written in Rust made for users.
> L70: - An architecture that lends itself towards the <ins>incremental adoption of new AI</ins> no matter which "shape" i

## 星数曲线

```mermaid
xychart-beta
    title "tryanything-ai/anything 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 312 --> 314
    line [313, 313]
```

2026-10-18 313 → 2026-10-27 313（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c371402c53ca` · [字段定义](../../DATASET.md)*
