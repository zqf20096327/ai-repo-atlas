# deepducks/spec

⭐ 16 · Shell · MIT · 推送 2026-08-04 · [GitHub](https://github.com/deepducks/spec) · [官网](https://duckflux.openvibes.tech/) · 个人维护

**面向 AI agent 工作流编排的声明式 YAML DSL 规范**

duckflux 是一个声明式、基于 YAML 的 DSL 及其规范，用于编排工作流：用户描述应发生什么及顺序，由遵循规范的运行时负责执行，不绑定 SDK 与厂商。规范运行时无关，任何符合规范的实现均可执行工作流；当前提供一份用 TypeScript 编写的 JavaScript 运行时实现。规范文档版本为 v0.7，附 JSON Schema、更新日志与路线图。README 未给出具体安装命令或使用示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 YAML DSL 描述工作流的步骤与顺序
- 运行时无关：任何遵循规范的实现均可执行
- 提供 TypeScript 编写的 JavaScript 运行时实现
- 规范 v0.7 附 JSON Schema 与变更路线

## 适用场景

- 用 YAML 声明多 agent 工作流而不写编排代码
- 为自建运行时提供可对接的工作流规范
- 以 JSON Schema 校验工作流定义文件

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L2: Duckflux is a declarative, YAML-based DSL for orchestrating workflows. You describe **what** should happen and in wh
> L15: Duckflux is runtime-agnostic. Any implementation that adheres to the spec can execute workflows. Currently, we have

## 星数曲线

```mermaid
xychart-beta
    title "deepducks/spec 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9005aaaaa476` · [字段定义](../../DATASET.md)*
