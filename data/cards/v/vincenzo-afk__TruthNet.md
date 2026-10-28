# vincenzo-afk/TruthNet

⭐ 34 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/vincenzo-afk/TruthNet) · 个人维护

**假新闻检测系统：多模型分类新闻真假并给出解释**

TruthNet 是一个假新闻检测框架：将新闻文章文本经预处理管线后分类为真实或虚假，支持 Logistic Regression、Naive Bayes、SVM 与 DistilBERT 四种模型，输出预测结果附特征重要性与置信度解释。提供 FastAPI 构建的 REST API（/predict、/health、/history 端点）、内置 Web 前端与 SQLite 历史记录。README 声明仅供研究与教育用途，不替代专业事实核查；DistilBERT 指标基于代表性子集微调。

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

- 四种模型可选（Logistic Regression / Naive Bayes / SVM / DistilBERT）
- 每次预测附特征重要性与置信度解释信号
- FastAPI REST API 与内置 Web 前端
- SQLite 内置预测历史记录

## 适用场景

- 提交新闻文章文本获得真假分类与置信度
- 通过 API 将假新闻检测接入其他系统
- 在自带前端中交互式分析文章并查看解释

## 场景标签

 · 领域:NLP/假新闻检测

## 证据(README 行号)

> L3: TruthNet is a comprehensive, production-grade machine learning framework designed to identify and classify news arti
> L15: - **Multi-Model Support**: Choose between Logistic Regression, Naive Bayes, SVM, and DistilBERT.

## 星数曲线

```mermaid
xychart-beta
    title "vincenzo-afk/TruthNet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cc1bb8653b2d` · [字段定义](../../DATASET.md)*
