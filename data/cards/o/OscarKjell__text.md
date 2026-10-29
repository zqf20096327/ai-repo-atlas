# OscarKjell/text

⭐ 160 · R · 推送 2026-10-21 · [GitHub](https://github.com/OscarKjell/text) · [官网](https://r-text.org) · 组织维护

**R 包：用 HuggingFace Transformer 做文本嵌入与分析**

面向 R 用户的自然语言分析包，是 R Language Analysis Suite 的一部分（与 talk、topics 等配套）。通过 Python 接口接入 HuggingFace Transformers，将文本转换为词嵌入，可用多语言模型（如多语言 BERT，覆盖 104 种语言）；同时提供端到端分析功能，如 textTrain() 用嵌入预测数值或分类变量，并支持在嵌入空间中可视化统计显著的词。由心理学与计算机科学协作开发，面向社会与行为科学研究者，在 Ubuntu/macOS/Windows 上测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 Python 接口接入 HuggingFace Transformers 语言模型
- 文本转词嵌入，支持多语言模型（104 种语言的多语言 BERT）
- textTrain() 等函数用嵌入预测数值/分类变量
- 提供嵌入空间中统计显著词的可视化

## 适用场景

- 在 R 中把文本转成可用于下游任务的词嵌入
- 用机器学习检验文本嵌入对变量的预测能力
- 社会与行为科学研究中的语言数据分析与可视化

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L18: An R-package for analyzing natural language with transformers-based
> L40: The *text*-package has two main objectives: \* First, to serve
> L45: Second, to serve as an *end-to-end solution* that provides

## 星数曲线

```mermaid
xychart-beta
    title "OscarKjell/text 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 159 --> 161
    line [160, 160]
```

2026-10-18 160 → 2026-10-29 160（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `85d76241fd7e` · [字段定义](../../DATASET.md)*
