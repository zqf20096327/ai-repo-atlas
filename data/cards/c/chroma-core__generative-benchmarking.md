# chroma-core/generative-benchmarking

⭐ 53 · Jupyter Notebook · MIT · 推送 2025-11-18 · [GitHub](https://github.com/chroma-core/generative-benchmarking) · 组织维护

**面向嵌入模型的定制化基准生成与评测工具包**

Chroma 维护的生成式基准测试工具包：给定一组文档，合成代表 ground truth 的查询，生成针对自有数据与场景的定制基准；包含将 LLM judge 对齐人类偏好的流程（基于 EvalGEN 改编）、不同嵌入模型/配置的指标比较框架，以及复现其技术报告结果的引导式 notebook。提供示例数据与结果目录，通过 uv sync 安装。面向需要对嵌入模型做评测的研究与开发场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从文档集合合成查询以生成定制基准
- 基于改编版 EvalGEN 将 LLM judge 对齐人类偏好
- 比较不同嵌入模型/配置的评测指标
- 提供复现技术报告结果的 notebook 与示例数据

## 适用场景

- 为自己的数据集生成定制化嵌入模型基准
- 将 LLM 评判对齐到特定使用场景的人类偏好
- 对比不同嵌入模型或配置的评测表现

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: We introduce generative benchmarking as a way to address these limitations. Given a set of documents, we synthetica
> L15: - **Generate Custom Benchmarks:** Generate benchmarks tailored to your data and use case
> L29:  A framework for comparing results, which is useful when evaluating different embedding models or configurations

## 星数曲线

```mermaid
xychart-beta
    title "chroma-core/generative-benchmarking 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-30 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0de14e3b3b41` · [字段定义](../../DATASET.md)*
