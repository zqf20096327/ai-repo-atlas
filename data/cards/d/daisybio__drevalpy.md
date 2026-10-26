# daisybio/drevalpy

⭐ 48 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/daisybio/drevalpy) · [官网](https://www.nature.com/articles/s41467-026-72903-w) · 组织维护

**癌症细胞系药物响应预测模型的评测与基准工具包**

面向药物响应预测研究者的 Python 工具包：提供基线模型目录、金标准数据集、标准化评测协议（LCO 等切分策略、交叉验证）、置换检验消融分析与跨数据集泛化评测，并生成论文可用的可视化报告（含 Nemenyi 检验的临界差异图）。支持灵活模型接口接入各类 ML/统计/网络模型，可选用 Ray Tune 并行调参，提供 Nextflow 流水线（nf-core/drugresponseeval）用于计算密集任务与可复现性。安装支持 pip、Docker 与源码（poetry），由慕尼黑工业大学与柏林自由大学合作维护，论文发表于 Nature Communications。

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

- 维护的基线模型目录与金标准基准数据集
- 标准化评测协议：LCO 切分、7 折交叉验证、跨数据集泛化分析
- 置换检验消融研究与论文级可视化报告（临界差异图）
- Nextflow 流水线（nf-core/drugresponseeval）用于高计算量实验

## 适用场景

- 我用新模型在金标准数据集上做标准化药物响应预测评测
- 我把文献基线模型直接从目录调用，无需自行复现
- 我做跨数据集泛化与消融分析并生成论文图表

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L19: - DrEval is a toolkit that ensures drug response prediction evaluations are statistically sound, biologically meani
> L29: 1. Maintained, up-to-date baseline catalog, no need to re-implement literature models
> L31: 3. Consistent application-driven evaluation

## 星数曲线

```mermaid
xychart-beta
    title "daisybio/drevalpy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-26 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ffdc7b690bc0` · [字段定义](../../DATASET.md)*
