# openai/model_spec_evals

⭐ 22 · Python · MIT · 推送 2026-03-24 · [GitHub](https://github.com/openai/model_spec_evals) · 组织维护

**评测模型对 OpenAI Model Spec 合规度的套件**

评估套件，用于测量候选模型对 OpenAI Model Spec 全部条文的遵守程度：包含一套评测提示词集与基于 Inspect AI 框架运行的代码。需要配套的 Model Spec Eval Dataset 仓库提供数据集。默认以 openai/gpt-4o-mini 为候选模型、openai/gpt-5 为评分模型，输出各章节及全量合规率与 token 用量；支持多轮采样取均值/中位数、按章节与 focus id 过滤，并可用 inspect view 查看结果。运行需 Python 3.10+ 与 OPENAI_API_KEY。部分提示在仅支持新模型的 developer messages 的 API 下会被跳过，绝对分数可能不完全可复现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 评测候选模型对完整 Model Spec 的遵守度，按章节输出合规率
- 基于 Inspect AI 框架，可配置候选模型与 grader 模型
- 支持多轮采样（epochs 取均值、grader 取中位数）与章节/focus 过滤
- 提供 Inspect 日志 web 查看器

## 适用场景

- 测量自家模型与 OpenAI Model Spec 的合规度
- 对比不同模型在 Model Spec 各章节的合规率差异
- 复现博客文章中的评测设置（20 epochs、5 grader 样本）

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L4: The Model Spec Evals is an evaluation suite consisting of:
> L6: - code to run the evaluations using the Inspect AI framework.

## 星数曲线

```mermaid
xychart-beta
    title "openai/model_spec_evals 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-31 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `abdc571e99fb` · [字段定义](../../DATASET.md)*
