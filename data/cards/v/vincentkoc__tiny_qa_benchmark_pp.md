# vincentkoc/tiny_qa_benchmark_pp

⭐ 18 · Python · Apache-2.0 · 推送 2026-04-30 · [GitHub](https://github.com/vincentkoc/tiny_qa_benchmark_pp) · 个人维护 · 中文 README

**52 题微型 QA 基准与多语言合成生成器，用于 LLM 快速回归测试**

面向 LLMOps 的超轻量评测套件：包含 52 题人工编写的英文黄金 QA 数据集（core_en）、按需生成多语言/多主题微基准的合成生成器 CLI（基于 LiteLLM，支持 OpenAI、OpenRouter、Ollama 等提供商），以及可接入 CI/CD 流水线的评测工具。预置英/法/西/葡/德/中/日/土/阿/俄等语言包，附带 arXiv 论文与 Croissant 元数据。代码与核心数据集为 Apache-2.0，合成数据包采用单独的仅限评测许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 52 题人工编写的英文黄金 QA 数据集用于确定性回归测试
- CLI 按需生成任意语言/主题/难度的合成微基准（基于 LiteLLM）
- 预置 10 种语言的多语言数据包，支持跨语言漂移检测
- 可编码为 OpenAI Evals YAML 或 Opik 数据集接入 CI/CD

## 适用场景

- CI/CD 流水线中对 LLM 服务做快速冒烟测试与回归拦截
- 提示词或 agent 迭代时获得快速反馈
- 用多语言包监测本地化回归与微调过程中的知识流失

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L19: **Tiny QA Benchmark++ (TQB++)** is an ultra-lightweight evaluation suite and python package designed to expose crit
> L33: * **LLMOps Alignment:** Designed for easy integration into CI/CD pipelines, prompt-engineering workflows, cross-lin

## 星数曲线

```mermaid
xychart-beta
    title "vincentkoc/tiny_qa_benchmark_pp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2b9553cf74b1` · [字段定义](../../DATASET.md)*
