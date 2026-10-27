# Vidhi1290/LLM---Detect-AI-Generated-Text

⭐ 75 · Jupyter Notebook · MIT · 推送 2025-11-24 · [GitHub](https://github.com/Vidhi1290/LLM---Detect-AI-Generated-Text) · 个人维护

**基于 BERT 的 AI 生成文本检测项目（Kaggle 竞赛）**

面向研究者与开发者的 AI 生成文本检测方案：使用 BERT 序列分类模型，流程包括数据预处理、BERT 分词、模型训练与预测，结果以 CSV 文件输出（含置信分数）。README 提供克隆仓库的安装步骤，属于 Kaggle LLM 检测竞赛的实现代码。项目以 MIT 许可发布，未提供打包安装、Docker 或演示链接，使用需自行训练模型。

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

- BERT 序列分类模型区分人类与 AI 生成文本
- 输出含置信分数的 CSV 检测结果
- 流程覆盖预处理、分词、训练、预测

## 适用场景

- 检测文章或帖子中 AI 生成的文本片段
- 作为 Kaggle AI 文本检测竞赛的参考实现
- 基于 BERT 二分类思路做文本真伪判定实验

## 场景标签

 · 领域:NLP/AI 文本检测

## 证据(README 行号)

> L1: # AI-Generated Text Detection using BERT
> L11: AI-generated content is becoming increasingly sophisticated, making it challenging to distinguish between genuine a
> L40: **Model Training:** Using a BERT-based sequence classification model, we train the system to distinguish between ge

## 星数曲线

```mermaid
xychart-beta
    title "Vidhi1290/LLM---Detect-AI-Generated-Text 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-27 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c8b2feaca01b` · [字段定义](../../DATASET.md)*
