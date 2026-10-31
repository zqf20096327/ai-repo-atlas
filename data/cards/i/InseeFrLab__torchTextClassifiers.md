# InseeFrLab/torchTextClassifiers

⭐ 23 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/InseeFrLab/torchTextClassifiers) · [官网](https://inseefrlab.github.io/torchTextClassifiers/) · 组织维护

**基于 PyTorch 的文本分类框架，支持类别变量混合输入**

构建于 PyTorch 与 PyTorch Lightning 之上的文本分类框架，面向开发者。提供 torchTextClassifiers 包装类编排分词器与模型，支持多分类与多标签任务；文本嵌入拆分为 TokenEmbedder 与 SentenceEmbedder 两个可组合阶段，可使用 HuggingFace 分词器或 fastText ngram 分词器，支持文本与类别变量混合输入，ValueEncoder 自动完成编码与解码。集成 Captum 梯度归因与标签注意力实现可解释性。通过 git clone 源码安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TokenEmbedder 与 SentenceEmbedder 两阶段可组合嵌入架构
- 文本与类别变量混合输入，ValueEncoder 自动编码/解码
- 支持多分类与多标签任务
- Captum 集成梯度归因与标签注意力实现 token 级解释

## 适用场景

- 训练文本分类或多标签分类模型
- 处理文本加类别变量的混合特征输入
- 对分类结果做 token 级归因解释

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: A unified, extensible framework for text classification with categorical variables built on PyTorch and PyTorch Ligh
> L15: - **Multiclass / multilabel classification support**: Support for both multiclass (only one label is true) and mult

## 星数曲线

```mermaid
xychart-beta
    title "InseeFrLab/torchTextClassifiers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fc38e04c60e5` · [字段定义](../../DATASET.md)*
