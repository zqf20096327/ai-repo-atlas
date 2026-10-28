# textgain/grasp

⭐ 79 · Python · BSD-3-Clause · 推送 2026-10-22 · [GitHub](https://github.com/textgain/grasp) · 组织维护

**纯 Python 轻量 AI 工具箱：数据挖掘/NLP/ML/网络分析 300+ 算法**

单文件无依赖的 Python 工具包（grasp.py，250KB，含 300+ 算法，每函数约 25 行），覆盖数据挖掘（HTML 解析、CSS 选择器、Wikipedia/Bluesky 抓取、WSGI 应用部署）、NLP（40+ 语言识别、地名识别、分词、词性标注、情感极性）、机器学习（向量化、Perceptron/DecisionTree/KNN 训练与预测）与网络分析（Graph、最短路径、PageRank、可视化）。支持模型决策解释 explain()。部分 NLP 功能需 grasp/lm 语言模型（50MB），gpt() 需 OpenAI API key。面向开发者，pip 从 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 300+ 算法打包为单个无依赖 Python 文件
- 语言识别（40+ 语言）、词性标注（10+ 语言，~95% 准确率）
- fit() 训练 Perceptron/DecisionTree/KNN 等模型并以 JSON 保存
- explain() 解释模型预测依据

## 适用场景

- 在无重依赖环境下做文本情感分析与词性标注
- 抓取网页/Bluesky 帖子并做关键词与观点挖掘
- 训练并解释小型分类模型（如垃圾邮件/观点判别）
- 构建与可视化带权重网络并计算 PageRank

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Grasp** is a lightweight AI toolkit for Python, with tools for data mining, natural language processing (NLP), mac
> L141: m = fit([(v1, '+'), (v2, '-')], model=Perceptron) # DecisionTree, KNN, ...
> L153: print(m.predict(vec('She hates dogs.')) # {'+': 0.4: , '-': 0.6}

## 星数曲线

```mermaid
xychart-beta
    title "textgain/grasp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-28 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2a7905926ed4` · [字段定义](../../DATASET.md)*
