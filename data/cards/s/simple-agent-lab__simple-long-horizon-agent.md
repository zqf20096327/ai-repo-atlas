# simple-agent-lab/simple-long-horizon-agent

⭐ 34 · Python · Apache-2.0 · 推送 2026-08-03 · [GitHub](https://github.com/simple-agent-lab/simple-long-horizon-agent) · [官网](https://simpleagentlab.com/) · 组织维护 · 中文 README

**面向长程任务的可学习 Agent 框架，供实验与基准评测**

一个代码量小、可自行阅读修改的 Python agent 项目，面向需要跨多轮模型调用完成的工作：规划、调用工具、校验结果并迭代。项目定位为学习、实验与小团队适配的基础，不依赖大型框架；提供可运行的确定性 demo（无需 API key）、OpenAI 兼容模型接入配置、评测套件与基准集成（SWE-bench Pro、Terminal-Bench 2.1、PostTrainBench 结果表）。自述为早期阶段、面向研究而非生产基础设施。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 紧凑代码库，无需先采用大型框架即可阅读与修改
- 支持工具调用、真实环境交互与多步长程迭代
- 提供无需 API key 的确定性演示与 OpenAI 兼容端点配置
- 内置评测套件与基准集成，结果表含模型、分数与成本

## 适用场景

- 通过运行和修改完整示例学习 agent 行为
- 为编码、研究或内部流程构建定制 agent
- 在可重复任务下对比提示词、模型与 agent 策略
- 在小型实验或既有基准上评测 agent 行为

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L33: Simple Long Horizon Agent is small enough to understand and change, while capable
> L38: Long-horizon work cannot be completed in a single response. It requires
> L53: - **Built to be evaluated** — runnable examples and benchmark integrations make

## 星数曲线

```mermaid
xychart-beta
    title "simple-agent-lab/simple-long-horizon-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c6c2d77935d6` · [字段定义](../../DATASET.md)*
