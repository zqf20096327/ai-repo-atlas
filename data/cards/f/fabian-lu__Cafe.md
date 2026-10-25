# fabian-lu/Cafe

⭐ 46 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/fabian-lu/Cafe) · [官网](https://cafe-ai.de) · 个人维护

**复合 AI 系统的实验设计评估平台：量化各技术对质量的贡献**

面向复合 AI 系统（检索、重排、提示、模型调用等组成的流水线）的评估框架：把每个流水线配置项当作实验因子，生成全因子或部分因子设计，以黑盒方式带重复地运行各配置，由可配置的 LLM 评审（或人工）打分，再用混合效应模型（序数 CLMM、逻辑 GLMM，运行于 R）做方差归因，输出各因子的显著性、效应量、最优配置及质量-成本 Pareto 前沿。以 pip 安装的 Python 库 + CLI 提供，另有基于 FastAPI + React 的可自托管 Web 平台（Docker 部署）。限制：需 Python ≥ 3.11 和 R 环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 因子化实验设计与带重复运行，分离真实效应与 LLM 非确定性噪声
- 尺度匹配的统计模型（序数→累积链接混合模型，二值→逻辑模型）
- LLM 评审与人工评审并用，Krippendorff's α 度量评审一致性
- 自托管 Web 平台，数据不离开本机；质量-成本-延迟 Pareto 前沿

## 适用场景

- 评估 RAG 流水线中检索、重排、模型选择各自对回答质量的贡献
- 在 LLM 输出非确定性下验证两个配置的差异是否显著
- 在质量、成本、延迟之间寻找 Pareto 最优配置

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L21: **CAFE treats every pipeline knob as an experimental factor.** It generates factorial designs, runs each
> L29: CAFE *measures* compound AI systems; it doesn't build them. Bring your system as a black box — a
> L119: 4. **Judge** — a configurable LLM judge (and/or humans) scores each answer on your rubric.

## 星数曲线

```mermaid
xychart-beta
    title "fabian-lu/Cafe 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 44 --> 47
    line [45, 46, 46]
```

2026-10-18 45 → 2026-10-25 46（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d3f499f0e80b` · [字段定义](../../DATASET.md)*
