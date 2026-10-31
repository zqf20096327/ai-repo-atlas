# yhzhu99/ehr-llm-benchmark

⭐ 15 · Python · 推送 2026-05-25 · [GitHub](https://github.com/yhzhu99/ehr-llm-benchmark) · [官网](https://yhzhu99.github.io/ehr-llm-benchmark/) · 组织维护

**临床预测任务的 LLM 基准评测代码：LLM 对比传统 ML**

npj Digital Medicine 2026 论文 ClinicRealm 的官方代码仓库：在 MIMIC-IV 与 TJH 数据集上，对 15 个 GPT 式 LLM、5 个 BERT 式模型和 11 种传统机器学习/深度学习方法进行非生成式临床预测任务的基准评测，任务涵盖院内死亡、30 天再入院、住院时长预测等。结构化 EHR 与非结构化临床笔记实验代码分目录提供，MIMIC-IV 预处理依赖外部仓库 PKU-AICare/mimic_preprocessor。环境为 Python 3.12，使用 uv 管理依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 15 个 LLM、5 个 BERT 式模型与 11 种传统 ML/DL 方法的对比实验
- 结构化 EHR 与非结构化临床笔记两类输入、多项临床预测任务
- 在线基准结果页面与独立的数据预处理仓库
- Python 3.12 + uv 依赖管理

## 适用场景

- 复现论文中的临床预测基准实验
- 为医院预测任务选型 LLM 或传统 ML 模型时参考基准结果
- 在 MIMIC-IV/TJH 数据上跑自己的模型对比

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L14: Large Language Models (LLMs) are increasingly deployed in medicine. However, their utility in non-generative clinic
> L29: The following prediction tasks, based on the MIMIC-IV and TJH datasets, have been implemented and evaluated in this
> L45: We examine a diverse array of models:

## 星数曲线

```mermaid
xychart-beta
    title "yhzhu99/ehr-llm-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `9a890887022f` · [字段定义](../../DATASET.md)*
