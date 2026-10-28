# thedataquarry/structured-outputs

⭐ 29 · Python · MIT · 推送 2025-12-23 · [GitHub](https://github.com/thedataquarry/structured-outputs) · 个人维护

**结构化输出基准：对比 DSPy 与 BAML 在多数据集上的表现**

在 4 个数据集（患者临床笔记、金融实体、保险理赔、PII）上对 DSPy 与 BAML 两个框架进行结构化输出（嵌套 JSON 抽取）的基准评测，其中 3 个数据集来自 Cleanlab 发布的人工标注基准。给出各条件下的结论：小模型与深层嵌套场景 BAML 表现更好，大模型搭配 DSPy 的自定义 BAMLAdapter 表现更好。以 Python 源码仓库形式提供，使用 uv 管理依赖并同步安装，结果存放在 src/baml 与 src/dspy 目录。README 未列出具体测试所用的 LLM 型号清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 4 个人工标注数据集的结构化输出评测
- 对比 DSPy 与 BAML 在不同模型能力与 schema 深度下的表现
- 引入 DSPy 自定义 BAMLAdapter 并对比默认 ChatAdapter 的 schema 格式化
- 结论强调提示词优化对两框架收益的共同影响

## 适用场景

- 在 DSPy 与 BAML 之间做结构化输出选型参考
- 了解嵌套 JSON schema 深度对框架表现的影响
- 复用 Cleanlab 结构化输出基准数据与评测方法

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Structured output benchmark that compares the results from modern tools like BAML
> L7: aims to explore some of those differences and compare their performance on multiple structured output benchmarks.

## 星数曲线

```mermaid
xychart-beta
    title "thedataquarry/structured-outputs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `7bf43dab6c84` · [字段定义](../../DATASET.md)*
