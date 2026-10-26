# oliverguhr/german-sentiment-lib

⭐ 57 · Python · MIT · 推送 2026-03-02 · [GitHub](https://github.com/oliverguhr/german-sentiment-lib) · [官网](https://pypi.org/project/germansentiment/) · 个人维护

**德语文本情感分类 Python 库，基于 BERT 输出正/负/中性**

提供简单接口的 Python 包，用 BERT 架构对德语文本做情感三分类（positive/negative/neutral），模型基于 184 万条多领域样本（Twitter、Facebook、影评、应用与酒店评论）训练。支持批量预测与输出各类别概率，README 列出在 8 个德语数据集上的 F1 分数。通过 pip 从 PyPI 安装，附有 LREC 2020 论文与引用格式。限制：仅支持德语，未提及 GPU 要求。

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

- 基于 BERT 架构，184 万条多领域德语样本训练
- 支持正/负/中性三分类及各类别概率输出
- 提供 8 个德语数据集上的 F1 分数结果
- pip 从 PyPI 安装，附训练论文引用

## 适用场景

- 对德语评论、社交媒体文本做情感分析
- 德语对话系统中判断用户情感倾向
- 批量文本情感分类并获取置信度概率

## 场景标签

 · 领域:自然语言处理/情感分析

## 证据(README 行号)

> L5: This package provides a very simple interface to detect the sentiment of German texts. It uses the Googles Bert arch
> L37: classes, probabilities = model.predict_sentiment(["das ist super"], output_probabilities = True)

## 星数曲线

```mermaid
xychart-beta
    title "oliverguhr/german-sentiment-lib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-26 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0693ccb10f5b` · [字段定义](../../DATASET.md)*
