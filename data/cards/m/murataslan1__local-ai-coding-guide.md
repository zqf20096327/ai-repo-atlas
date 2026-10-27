# murataslan1/local-ai-coding-guide

⭐ 31 · Python · MIT · 推送 2026-01-02 · [GitHub](https://github.com/murataslan1/local-ai-coding-guide) · 个人维护

**本地化 AI 编程助手搭建指南：模型选择、运行时与工作流**

一份面向开发者的教程型指南仓库，讲解如何用 Ollama 等本地运行时运行 Qwen2.5-Coder 等开源编码模型，替代云端 API。内容包括快速上手步骤、Ollama/llama.cpp/vLLM/SGLang 运行时对比表、模型与量化选择表、硬件需求与速度公式、Continue.dev/Cursor/Aider 的 IDE 集成配置、Aider+Ollama 的 agentic 工作流、防幻觉护栏策略（TDD/计划先行/范围限制）、CO-STAR 提示框架、成本分析与常见错误清单。本身不含可安装代码，配置片段与命令需用户自行执行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖安装到 agentic 工作流的完整本地编码助手搭建流程
- Ollama/llama.cpp/vLLM/SGLang 四种运行时的吞吐对比表
- 模型/量化/硬件三级选型表与速度估算公式（带宽÷模型体积）
- TDD 反馈循环、计划先行、范围限制三类防幻觉护栏策略

## 适用场景

- 我在自己的 GPU 上搭一套替代付费 API 的本地编码助手
- 我需要比较 Ollama、llama.cpp、vLLM 该选哪个
- 我想学习如何用提示工程和 TDD 约束本地模型的编码行为

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: **Run GPT-4 class AI coding assistants 100% locally. No API costs. No cloud. Total privacy.**
> L16: *Complete guide with agentic workflows, prompt engineering, runner comparison, and real-world examples*
> L59: - Docker Compose - One-command setup
> L84: ## 🚀 Quick Start

## 星数曲线

```mermaid
xychart-beta
    title "murataslan1/local-ai-coding-guide 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9384ea7c14c2` · [字段定义](../../DATASET.md)*
