# InftyAI/AMRS

⭐ 24 · Rust · MIT · 推送 2026-01-04 · [GitHub](https://github.com/InftyAI/AMRS) · 组织维护

**自适应模型路由系统：按策略在多模型间选择最优**

Rust 核心带 Python 绑定的模型路由框架，基于 async-openai 提供 API 服务，目标是面向探索与利用场景选出最合适的模型。支持 Chat Completions 与 Responses 两类端点，路由策略含 Random（默认）、WRR 加权轮询，UCB1 与 Adaptive 策略标注为 coming soon。支持 OpenAI 兼容的 provider（OpenAI、DeepInfra 等），通过 Cargo 安装，运行前需在环境变量中设置 provider API key。项目自述仍处于活跃开发阶段。

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

- Rust 核心 + Python 绑定，基于 async-openai 提供 API 服务
- 路由策略：Random（默认）/WRR 加权轮询，UCB1 与 Adaptive 开发中
- 支持 Chat Completions 与 Responses 端点
- 支持 OpenAI 兼容 provider（OpenAI、DeepInfra 等）

## 适用场景

- 在多个模型间按权重或随机策略分发请求
- 构建需要模型选择能力的 LLM 服务
- 用 Rust 快速搭建 OpenAI 兼容的代理层

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: The Adaptive Model Routing System (AMRS) is a framework designed to select the best-fit model for exploration and ex
> L7: AMRS builds on top of async-openai to provide API services for quick setup. Thanks to open source 💙.

## 星数曲线

```mermaid
xychart-beta
    title "InftyAI/AMRS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-30 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7f71021a573a` · [字段定义](../../DATASET.md)*
