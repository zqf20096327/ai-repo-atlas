# Assisted-Mindfulness/naive-bayes

⭐ 45 · PHP · MIT · 推送 2026-09-25 · [GitHub](https://github.com/Assisted-Mindfulness/naive-bayes) · 个人维护

**PHP 朴素贝叶斯文本分类器库：训练后预测文本所属类别**

PHP Composer 包，实现朴素贝叶斯文本分类：通过 learn 方法传入文本与类别（支持字符串、整数、枚举）构建训练集，再用 most/guess 方法预测新文本所属类别并返回各类别概率。概率以 BigDecimal 输出且总和精确为 1，应用拉普拉斯平滑，可配置小数精度与基于训练分布的不均匀先验，默认分词器提取 Unicode 字母并可自定义。供 PHP 开发者在项目中集成垃圾邮件过滤、新闻分类、情感分析等场景。MIT 许可。

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

- learn 训练 + most/guess 预测的朴素贝叶斯分类 API
- 概率以 BigDecimal 输出且精确合计为 1，应用拉普拉斯平滑
- 类别支持字符串/整数/backed enum/pure enum
- 可自定义分词器、精度 scale 与不均匀先验模式

## 适用场景

- 判断邮件是否为垃圾邮件
- 将新闻文章归入技术/政治/体育等类别
- 对文本做正面/负面情感分类

## 场景标签

 · 领域:机器学习/文本分类

## 证据(README 行号)

> L5: This PHP package for Naive Bayes works by looking at a training set and making a guess based on that set.
> L10: You can use this for categorizing any text content into any arbitrary set of **categories**. For example:

## 星数曲线

```mermaid
xychart-beta
    title "Assisted-Mindfulness/naive-bayes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c7091ac10990` · [字段定义](../../DATASET.md)*
