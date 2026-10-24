# microsoft/ParrotServe

⭐ 228 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/microsoft/ParrotServe) · 组织维护 · 中文 README

**面向 LLM 应用的多租户分布式 serving 系统（OSDI'24 原型）**

Parrot 是微软开源的 LLM 应用 serving 系统研究原型，通过 Semantic Variable 抽象在 OpenAI 风格 API 基础上向后台引擎暴露应用级信息（LLM 计算图 DAG、prompt 结构），支持请求自动并行化与批处理、DAG 感知调度、prompt 前缀共享与上下文感知调度；提供 Python 前端 pfunc 编程。README 明确声明该项目为研究原型、不再积极维护；已做安全热修复（禁用动态注册、要求 bearer token），旧版本存在任意代码执行等漏洞，不可暴露于不可信网络。面向 LLM 应用开发者与系统研究者。

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

- Semantic Variable 抽象暴露应用级信息给后台引擎
- 自动并行化/批处理 LLM 请求与 DAG 感知调度
- prompt 前缀共享与上下文感知调度
- 提供 Python 前端 pfunc 与 OpenAI 风格 API

## 适用场景

- 运行包含多轮 LLM 调用 DAG 的 agent 应用并复用公共前缀
- 研究 LLM 应用级 serving 调度机制（OSDI'24 论文原型）
- 基于 OpenAI 风格 API 改造现有 LLM 应用的部署方式

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L39: Parrot is a distributed, multi-tenant serving system for **LLM-based Applications**. With the Semantic Variable abs
> L57: Parrot is designed to serve these LLM-based applications efficiently by adding `Semantic Variable` in current OpenA

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/ParrotServe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 227 --> 229
    line [228, 228]
```

2026-10-18 228 → 2026-10-24 228（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `89c6f2e23812` · [字段定义](../../DATASET.md)*
