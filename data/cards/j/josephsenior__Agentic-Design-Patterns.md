# josephsenior/Agentic-Design-Patterns

⭐ 41 · Python · MIT · 推送 2026-08-28 · [GitHub](https://github.com/josephsenior/Agentic-Design-Patterns) · 个人维护

**21 种 LLM Agent 设计模式的可运行参考实现库**

教育性参考实现库，将 21 种常见 agent 编排模式（Prompt Chaining、Routing、Planning、Tool Use、Multi-Agent、RAG、Guardrails 等）各隔离在独立目录中，每个目录包含实现、示例、README 与依赖文件。目标是让单个编排思想便于检视、运行、比较与组合，而非提供统一框架。示例部分调用 Gemini 等外部模型 API，需自行配置 API key；CI 仅校验仓库结构与 Python 语法，不端到端运行。面向学习 agent 编排的工程师与学生。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 21 种模式各自独立目录，含实现与可运行示例
- 提供模式组合建议（如 Routing+Tool Use、Planning+Evaluation）
- README 明确定位为教育参考实现而非生产系统

## 适用场景

- 学习对比常见 LLM-agent 编排模式
- 在集成到更大系统前查阅小型参考实现
- 理解模式间的组合关系（如 RAG+Tool Use）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: > 21 runnable reference implementations for understanding common LLM-agent workflow patterns.
> L11: This repository is a clean-room educational reference library containing runnable implementations of 21 agent desig
> L15: > **Project status:** educational reference implementations. CI verifies repository structure and Python syntax; ex

## 星数曲线

```mermaid
xychart-beta
    title "josephsenior/Agentic-Design-Patterns 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-31 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9853a58fe0ad` · [字段定义](../../DATASET.md)*
