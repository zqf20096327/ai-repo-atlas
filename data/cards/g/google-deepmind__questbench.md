# google-deepmind/questbench

⭐ 44 · Python · Apache-2.0 · 推送 2026-06-30 · [GitHub](https://github.com/google-deepmind/questbench) · [官网](https://openreview.net/pdf?id=gpwA9aZLTZ) · 组织维护

**LLM 欠定推理任务追问能力的基准数据集与评测代码**

QuestBench 将欠定任务形式化为缺失变量赋值的约束满足问题，评测 LLM 识别最小必要追问的能力。包含四个子集：Logic-Q（缺一命题的逻辑推理）、Planning-Q（部分可观测初始态的 PDDL 规划）、GSM-Q（人工标注缺一变量的小学数学）、GSME-Q（方程化版本）。仓库提供数据生成脚本与评测脚本，支持 Gemini、GPT、Claude、Gemma 系列（Gemma 需经 vLLM 服务运行）。论文发表于 NeurIPS 2025。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个子任务覆盖逻辑/规划/数学的欠定推理场景
- 要求模型从选项中选出正确的澄清问题
- 提供数据生成脚本与评测脚本
- 支持 Gemini/GPT/Claude/Gemma 多系列模型评测

## 适用场景

- 评测 LLM 在信息不足时提出必要澄清问题的能力
- 研究模型信息获取能力与欠定任务难度轴
- 生成欠定推理任务数据用于训练或分析

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Recently, a large amount of work has focused on improving large language models' (LLMs') performance on reasoning be
> L7: This repository contains code for generating QuestBench data and evaluating LLMs on it.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/questbench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-31 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3cdc989c3796` · [字段定义](../../DATASET.md)*
