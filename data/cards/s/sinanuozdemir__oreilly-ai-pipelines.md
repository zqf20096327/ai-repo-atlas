# sinanuozdemir/oreilly-ai-pipelines

⭐ 44 · Jupyter Notebook · 推送 2026-06-26 · [GitHub](https://github.com/sinanuozdemir/oreilly-ai-pipelines) · [官网](https://learning.oreilly.com/live-events/designing-and-deploying-llm-pipelines/0642572014796) · 个人维护

**O'Reilly LLM 流水线课程配套代码：原型到生产的训练材料**

O'Reilly Live Online Training《Designing and Deploying LLM Pipelines》课程的代码仓库，面向机器学习工程师与软件开发者，内容覆盖 LangGraph/CrewAI/OpenAI Agents/SmolAgents 的 agent 与工作流 notebook、BERT 微调与 FastAPI 部署、LLM 提供商推理、量化与蒸馏（bitsandbytes、llama.cpp/GGUF）等。附一个加载 DistilBERT 的最小 FastAPI 推理服务（含 Dockerfile）与 Streamlit CrewAI 演示应用。需 Python 3.11 虚拟环境，部分示例需 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph/CrewAI/OpenAI Agents/SmolAgents 等 agent notebook 集合
- 加载 DistilBERT 的 FastAPI 推理服务（/predict 端点，含 Docker 构建）
- 量化 notebook：bitsandbytes 动态量化 Llama-3、llama.cpp/GGUF 有无 GPU 对比
- Streamlit CrewAI agent 演示应用

## 适用场景

- 跟随课程学习 LLM 原型到生产部署的流程
- 参考 FastAPI 推理服务与 Docker 化部署示例
- 学习 LangGraph 等 agent 框架的使用方式

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: This repository contains code for the O'Reilly Live Online Training for Designing and Deploying LLM Pipelines
> L7: In this comprehensive course, machine learning engineers and software developers learn how to transition large langu

## 星数曲线

```mermaid
xychart-beta
    title "sinanuozdemir/oreilly-ai-pipelines 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c5800f5b4baa` · [字段定义](../../DATASET.md)*
