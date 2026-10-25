# vrunm/Text-Classification-Financial-Phrase-Bank

⭐ 33 · Python · MIT · 推送 2026-06-04 · [GitHub](https://github.com/vrunm/Text-Classification-Financial-Phrase-Bank) · 个人维护

**金融新闻句子情感分类模型：FinBERT 微调与优化器对比**

在 Financial PhraseBank 数据集（16 名金融背景标注者标注的英文金融新闻句子，三分类）上微调 BERT、DistilBERT、FinBERT 进行情感分析，最优为 FinBERT（准确率 90.9%、F1 0.91）。附带多优化器（Adam/AdamW/RMSprop/NAG/SGD）训练对比实验，结论收敛速度 Adam 最快。以 Python 包提供 finbert-train CLI，数据集经 Hugging Face datasets 自动下载，支持四种标注一致性子集配置与分层验证集划分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FinBERT 微调达 90.9% 准确率、0.91 F1
- 六种优化器训练收敛性对比实验
- finbert-train CLI 支持四种标注一致性数据子集
- 数据集首次运行时自动从 Hugging Face Hub 下载

## 适用场景

- 训练金融新闻情感三分类模型
- 比较不同优化器在文本分类微调中的收敛表现
- 复用 CLI 在 Financial PhraseBank 各子集上实验

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3: - Built a sentiment analysis model to predict the sentiment of a financial news sentence.
> L5: - A BERT model was used as a baseline. The **FinBERT and DistilBERT** models were fine-tuned to get the best results
> L6: - The best results were obtained using the fine-tuned on the FINBERT model. It achieved an **Accuracy of 90.9%** and

## 星数曲线

```mermaid
xychart-beta
    title "vrunm/Text-Classification-Financial-Phrase-Bank 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2059b5b3bf97` · [字段定义](../../DATASET.md)*
