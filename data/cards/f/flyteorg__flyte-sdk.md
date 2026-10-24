# flyteorg/flyte-sdk

⭐ 129 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/flyteorg/flyte-sdk) · [官网](https://flyte.org/) · 组织维护

**纯 Python 的 ML 流水线与 agent 分布式编排 SDK**

Flyte 2 SDK 用 async/await 语法在纯 Python 中定义和运行类型安全的分布式 ML 流水线、模型与 agent 编排任务，提供 flyte CLI、可安装的 TUI 本地开发界面，以及基于 docker 和 k3s 的本地 Devbox 环境；支持通过 FastAPI 示例提供模型 serving。另含实验性的 Rust 远程控制器实现，以可选依赖 flyte_controller_base 分发，经 maturin/pyo3 暴露给 Python。SDK 默认发送崩溃报告与使用计数遥测，可通过环境变量关闭。面向构建与运维 ML 工作流的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- async/await 纯 Python 定义类型安全的分布式任务与流水线
- flyte run / flyte serve CLI 与可安装 TUI 本地开发界面
- docker/k3s 本地 Devbox 开发环境
- 实验性 Rust 控制器（maturin/pyo3，可选 wheel 分发）

## 适用场景

- 编写并本地调试分布式 ML 流水线
- 将训练好的模型以服务形式部署运行
- 在本地 Devbox 中模拟 Flyte 2 的运行环境

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L13: **Reliably orchestrate ML pipelines, models, and agents at scale — in pure Python.**
> L142: The Rust controller is an alternative implementation of the remote controller written in Rust and exposed

## 星数曲线

```mermaid
xychart-beta
    title "flyteorg/flyte-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 128 --> 130
    line [129, 129]
```

2026-10-18 129 → 2026-10-24 129（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f5d6a9a1e0df` · [字段定义](../../DATASET.md)*
