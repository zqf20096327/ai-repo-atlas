# niiknow/bayes

⭐ 69 · PHP · MIT · 推送 2026-01-27 · [GitHub](https://github.com/niiknow/bayes) · 个人维护

**PHP 朴素贝叶斯文本分类库，教它学习后判断文本类别**

从 Node.js 库 ttegel/bayes 移植的 PHP 朴素贝叶斯分类器：通过 learn(text, category) 训练后，用 categorize(text) 判断新文本所属类别，并可提取各类别概率。保留与原 Node.js 库相同的 JSON 序列化格式，训练结果可在 PHP 与 Node.js 之间互用；支持自定义 tokenizer（如传入停用词表）。以 composer 包形式安装，面向 PHP 开发者。

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

- learn/categorize/probabilities API 完成文本分类训练与推断
- JSON 序列化格式与原 Node.js 库兼容，训练数据可跨语言互用
- 构造时可传入自定义 tokenizer 处理停用词

## 适用场景

- 判断邮件是否为垃圾邮件
- 将新闻文章归类到技术/政治/体育等类别
- 对文本做正面/负面情感归类

## 场景标签

 · 领域:机器学习/文本分类

## 证据(README 行号)

> L4: `bayes` takes a document (piece of text), and tells you what category that document belongs to.
> L42: ### `$classifier->learn(text, category)`

## 星数曲线

```mermaid
xychart-beta
    title "niiknow/bayes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-30 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b8fddb6164cf` · [字段定义](../../DATASET.md)*
