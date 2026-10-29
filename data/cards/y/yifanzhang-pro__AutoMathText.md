# yifanzhang-pro/AutoMathText

⭐ 93 · Python · CC-BY-4.0 · 推送 2025-11-23 · [GitHub](https://github.com/yifanzhang-pro/AutoMathText) · [官网](https://auto-data-selection.github.io) · 组织维护

**约 200GB 数学文本数据集，Qwen-72B 打分筛选**

ACL 2025 Findings 论文 Autonomous Data Selection 的官方实现，同时发布约 200 GB 的数学文本数据集 AutoMathText。数据汇集自 OpenWebMath、RedPajama、Algebraic Stack 等来源（网站、arXiv、GitHub），由 Qwen-72B 以零样本生成式分类器方式自主打分，每条文本附带 [0,1] 区间的 lm_q1q2_score 分数。README 给出按分数区间划分的加载配置，并通过 Huggingface datasets API（load_dataset）使用，另附论文的三段 Meta Prompt 示例。定位是面向数学-AI 交叉研究的预训练/微调数据资源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 200 GB 数学文本，来源含 OpenWebMath、RedPajama、Algebraic Stack
- 每条文本由 Qwen-72B 零样本打分（lm_q1q2_score ∈ [0,1]）
- 提供按分数区间（如 web-0.50-to-1.00）划分的数据集配置
- 附论文三段数据选择 Meta Prompt 示例

## 适用场景

- 为面向数学推理的 LLM 预训练/微调提供筛选过的语料
- 研究数学与 AI 交叉领域的数据选择方法
- 按质量分数阈值取用不同规模的数据子集

## 场景标签

 · 领域:数学/LLM 预训练数据

## 证据(README 行号)

> L14: **AutoMathText** is an extensive and carefully curated dataset encompassing around **200 GB** of mathematical texts
> L85: - **Volume**: Approximately 200 GB of text data (in natural language and programming language).

## 星数曲线

```mermaid
xychart-beta
    title "yifanzhang-pro/AutoMathText 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-29 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4177cbfaa6c9` · [字段定义](../../DATASET.md)*
