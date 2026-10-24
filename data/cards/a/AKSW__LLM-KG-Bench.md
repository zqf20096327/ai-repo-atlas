# AKSW/LLM-KG-Bench

⭐ 60 · Python · MPL-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/AKSW/LLM-KG-Bench) · 组织维护

**评测 LLM 知识图谱任务能力的自动化基准框架与任务集**

面向 LLM 在知识图谱（RDF/SPARQL/Turtle 等）相关任务上的自动化评测框架：内置多类评测任务，通过配置文件指定任务、模型、规模与迭代次数执行基准测试，生成 JSON/YAML/TXT 格式结果与模型日志，并支持对已有结果文件重新评测。架构基于并大致兼容 Big Bench，扩展了迭代、任务参数与 prompt-answer-evaluate 循环。模型接入支持 OpenAI/Anthropic/Google API key、GPT4All 与 vLLM（后两者标注不再测试），依赖 uv 管理并需 Python 3.10 以上。配套多篇发表论文与公开结果仓库，明确要求测试集不得用于 LLM 训练。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动化基准执行：配置任务×模型×规模×迭代，产出多格式结果文件
- 支持对已有结果文件通过 --reeval 参数重新评测
- 架构基于并大致兼容 Big Bench，扩展迭代与任务参数机制
- 配套多篇论文与独立结果仓库，附公开排行榜计划

## 适用场景

- 评测不同 LLM 在 RDF/SPARQL 等知识图谱工程任务上的能力
- 复现已发布基准结果或对历史结果重新评测
- 为知识图谱相关研究选型模型提供量化依据

## 场景标签

`模型评测` `知识图谱` · 领域:评测与运维

## 证据(README 行号)

> L3: Framework and task collection for automated benchmarking of Large Language Modells (LLMs) on Knowledge Graph (KG) re
> L37: Copy the example configuration file from `LlmKgBench/configuration.dist.yml` to `LlmKgBench/configuration.yml` chec

## 星数曲线

```mermaid
xychart-beta
    title "AKSW/LLM-KG-Bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-24 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `f6aa07315e87` · [字段定义](../../DATASET.md)*
