# data-privacy-stack/presidio-research

⭐ 318 · Jupyter Notebook · MIT · 推送 2026-10-19 · [GitHub](https://github.com/data-privacy-stack/presidio-research) · [官网](https://data-privacy-stack.github.io/presidio-research/) · 组织维护

**PII 检测模型的评测与合成数据生成工具包**

Presidio 生态的数据科学配套包（PyPI 包名 presidio-evaluator）：提供基于模板与虚假 PII 的合成数据生成器，支持 IO/BIO/BILUO 标注与防泄漏的 train/test/validation 划分；数据表示层可在 JSON、CoNLL、spaCy v3 等格式间转换；评测框架可对 Presidio 系统、NER 模型或单个 PII 识别器计算 precision/recall 并做误差分析。面向开发与评测 PII 检测模型或 Presidio 识别器的用户。限制：Flair、Stanza 等依赖已不再支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模板+虚假 PII 的合成数据生成，含标注与 span 生成
- 模板级防泄漏的数据集划分
- JSON/CoNLL/spaCy v3 多格式数据转换
- 对 Presidio 系统、NER 模型与识别器做 precision/recall 评测与误差分析

## 适用场景

- 评测 Presidio 或自建 PII 识别器的准确率
- 生成合成 PII 数据扩充 NER 训练集
- 在 CoNLL 与 spaCy 格式间转换 PII 数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This package provides evaluation and data-science capabilities for
> L118: The presidio-evaluator framework allows you to evaluate Presidio as a system, a NER model, or a specific PII recog

## 星数曲线

```mermaid
xychart-beta
    title "data-privacy-stack/presidio-research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 317 --> 319
    line [318, 318]
```

2026-10-18 318 → 2026-10-27 318（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `7e26e1aeb2e9` · [字段定义](../../DATASET.md)*
