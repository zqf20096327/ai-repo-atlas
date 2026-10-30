# jie-jw-wu/Survey-CodeLLM4LowResource-DSL

⭐ 20 · MIT · 推送 2026-06-11 · [GitHub](https://github.com/jie-jw-wu/Survey-CodeLLM4LowResource-DSL) · [官网](https://arxiv.org/pdf/2410.03981v3) · 组织维护

**LLM 低资源/领域专用语言代码生成综述的论文资源清单**

配套发表于 ACM TOSEM 综述论文的资源仓库，主题为 LLM 在低资源编程语言（LRPL）与领域专用语言（DSL）上的代码生成。系统性梳理 2020-2024 年间从 27,000+ 篇研究中筛选出的 111 篇论文，覆盖 40+ 种编程语言；归纳四类评测技术、六组增强方法（微调 48 篇、提示策略 25 篇等）、数据集构建流程，并按语言类别给出完整论文列表与基准/指标统计表。面向代码生成方向的科研人员与研究生。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 111 篇论文（27,000+ 初筛，2020-2024）、覆盖 40+ 种编程语言的系统性综述
- 增强方法分类统计：微调/提示/预训练/RAG/知识蒸馏等
- 评测指标与基准汇总（pass@k、MultiPL-E、VerilogEval 等）
- 数据集构建与处理流水线（过滤、去污、合成数据生成）分析

## 适用场景

- 查找 LRPL/DSL 代码生成方向的已有研究与基准
- 了解针对低资源语言的 LLM 增强方法分类
- 为代码生成数据集构建参考处理流程

## 场景标签

`精选清单` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: This repository contains resources referenced in the paper: A Survey on LLM-based Code Generation for Low-Resource a
> L21: Our survey provides a **systematic review of 111 papers** filtered from over 27,000 published studies from 2020-202

## 星数曲线

```mermaid
xychart-beta
    title "jie-jw-wu/Survey-CodeLLM4LowResource-DSL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `db237d55a4a8` · [字段定义](../../DATASET.md)*
