# lupantech/MathVista

⭐ 367 · Jupyter Notebook · CC-BY-SA-4.0 · 推送 2026-07-27 · [GitHub](https://github.com/lupantech/MathVista) · [官网](https://mathvista.github.io/) · 组织维护

**评测视觉语境数学推理的基准数据集与评测代码（6,141 例）**

ICLR 2024 论文的配套仓库：MathVista 基准由 28 个既有 多模态数据集与 3 个新构建数据集（IQTest、FunctionQA、PaperQA）共 6,141 个样本组成，考察模型对数学与视觉交叉任务的理解与推理。仓库提供数据集下载（Huggingface）、可视化工具、评测流水线与脚本，并维护公开排行榜（testmini 1,000 例/test 全集），支持通过邮件提交结果。2023 年 10 月对 12 个基础模型的评测显示 GPT-4V 以 49.9% 居首。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6,141 个样本，源自 28 个既有数据集与 3 个新构建数据集
- testmini（1,000 例）与 test 子集的公开排行榜及提交模板
- 提供评测流水线、评测脚本与数据可视化工具
- 数据集发布于 Huggingface Datasets 与 Paper With Code

## 适用场景

- 评测大模型在图表/图形等视觉语境下的数学推理能力
- 向排行榜提交自研模型的 testmini/test 成绩
- 研究细粒度视觉理解与组合推理的失败案例

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L85: **Large Language Models (LLMs)** and **Large Multimodal Models (LMMs)** exhibit impressive problem-solving skills i
> L13: Code for the Paper "MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts".

## 星数曲线

```mermaid
xychart-beta
    title "lupantech/MathVista 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 366 --> 368
    line [367, 367]
```

2026-10-18 367 → 2026-10-25 367（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d001b0092719` · [字段定义](../../DATASET.md)*
