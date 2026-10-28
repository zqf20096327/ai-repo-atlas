# Nextron-Labs/thor-ai-benchmarks

⭐ 28 · Python · 推送 2026-10-23 · [GitHub](https://github.com/Nextron-Labs/thor-ai-benchmarks) · [官网](https://nextron-labs.github.io/thor-ai-benchmarks/) · 组织维护

**THOR 取证发现分诊的 LLM 评测结果集（90 模型）**

发布 LLM 在 THOR 安全取证发现分诊任务上的公开评测结果：覆盖 90 个模型、10 份 THOR 报告、189 条专家标注发现，以人类专家判定为基准，评估分类质量（CW%）与运营可用性（Balanced OTS、Critical Miss Rate、False Review Load）。按闭源 API、开源专业硬件、开源消费级硬件三个部署层级给出各运营画像下的当前领先模型，并提供决策图表（散点图、Pareto 前沿）与交互式浏览视图；强调没有单一最优模型，需按部署约束选择。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 90 个模型、10 份 THOR 报告、189 条专家分类发现的评测结果集
- 双维度指标：CW% 分类质量与 Balanced OTS/Critical Miss/False Review Load 运营指标
- 按闭源 API/开源专业硬件/开源消费硬件三层级分别给出画像领先模型
- 提供决策散点图、成本/速度图表与交互式浏览视图

## 适用场景

- 为 SOC 分诊场景按运营画像选择 LLM
- 对比本地/开源模型与厂商 API 模型的运营表现
- 理解 CW% 与运营风险（漏报、误报复核负载）的差异

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3: This benchmark evaluates LLMs on THOR finding triage. It focuses on security event and forensic finding assessment, 
> L5: The current public result set covers **90 complete models**, **10 THOR reports**, and **189 expert-classified findin

## 星数曲线

```mermaid
xychart-beta
    title "Nextron-Labs/thor-ai-benchmarks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1348d4e5522a` · [字段定义](../../DATASET.md)*
