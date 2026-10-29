# PacificAI/langtest

⭐ 561 · Python · Apache-2.0 · 推送 2026-08-28 · [GitHub](https://github.com/PacificAI/langtest) · [官网](http://langtest.org/) · 组织维护

**LLM/NLP 模型安全与质量评测库，60+ 类测试一行代码执行**

Python 评测库 LangTest，面向数据科学家与 NLP 从业者：对 NLP 模型（Spark NLP、Hugging Face Transformers）与 LLM（OpenAI、Cohere、AI21、Azure-OpenAI 等）执行鲁棒性、偏见、公平性、准确性、毒性、事实性、谄媚性等 60 余类测试，并附带覆盖多任务的基准数据集；支持基于测试结果的训练数据自动增强（限部分模型）与模型排名榜单。以 pip 安装，由 John Snow Labs 全职团队维护，Apache 2.0 许可，自称早期阶段社区项目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一行代码生成并执行 60 余类测试
- 测试鲁棒性、偏见、公平性、代表性、准确性等模型质量维度
- 支持 Spark NLP、Hugging Face、OpenAI、Cohere、AI21、Azure-OpenAI 等框架与 LLM
- 内置多场景基准数据集，支持基于测试结果的训练数据自动增强

## 适用场景

- 上线前对 LLM 做毒性、事实性、偏见等安全测试
- 对 NER、翻译、文本分类模型做鲁棒性评测
- 用 Wino Bias、StereoSet 等数据集检测模型刻板印象偏见
- 基于测试结果自动增强训练数据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L50: - Generate and execute more than 60 distinct types of tests only with 1 line of code
> L54: - Support for testing LLMS ( OpenAI, Cohere, AI21, Hugging Face Inference API and Azure-OpenAI LLMs) for question a

## 星数曲线

```mermaid
xychart-beta
    title "PacificAI/langtest 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 560 --> 562
    line [561, 561]
```

2026-10-18 561 → 2026-10-29 561（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `925ff53002ff` · [字段定义](../../DATASET.md)*
