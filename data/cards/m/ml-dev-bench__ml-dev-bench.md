# ml-dev-bench/ml-dev-bench

⭐ 44 · Python · MIT · 推送 2026-03-10 · [GitHub](https://github.com/ml-dev-bench/ml-dev-bench) · 组织维护

**评测 AI agent 在 ML 开发任务上表现的基准**

ML-Dev-Bench 是一个评测基准，用于衡量 AI agent 在真实机器学习开发任务上的表现，含 30 个任务，覆盖数据集处理、模型训练、调试、模型实现、API 集成与性能提升 6 类。配套 Calipers 评测框架，提供指标跟踪、Hydra 配置、多轮评测与参数扫描，并集成 LiteLLM 与 LangChain。已评测 ReAct、OpenHands、AIDE 三种 agent 搭配 Claude 3.5 Sonnet、GPT-4o、Gemini 2.0 Flash。要求 Python 3.12+、Poetry 1.8+，通过 git clone 与 make 安装，agent 以两级 Docker 镜像方式构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 个任务覆盖 ML 开发 6 个类别
- Calipers 框架：指标跟踪、Hydra 配置、多轮评测与参数扫描
- 已评测 3 种 agent 与 3 种模型的组合结果
- agent 通过两级 Docker 镜像（base+agent 专属）构建

## 适用场景

- 评测自研 agent 在 ML 开发任务上的完成率
- 对比不同 agent/模型在调试、训练等任务的表现
- 复用框架添加自定义评测任务与新 agent

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: ML-Dev-Bench is a benchmark for evaluating AI agents on real world ML development tasks.
> L9: We also introduce Calipers, a framework for evaluating AI agents, providing tools and infrastructure for systematic 

## 星数曲线

```mermaid
xychart-beta
    title "ml-dev-bench/ml-dev-bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `be0f3cba3b42` · [字段定义](../../DATASET.md)*
