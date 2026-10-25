# luismond/tm2tb

⭐ 60 · Python · GPL-3.0 · 推送 2025-11-19 · [GitHub](https://github.com/luismond/tm2tb) · 个人维护

**双语术语抽取器：从翻译记忆与双语文档生成术语库**

面向翻译与本地化工作流的 Python 工具：读取 .tmx/.mqxliff/.mxliff/.csv/.xlsx 双语文件，用 spaCy 做分词与词性标注抽取术语，再用 sentence-transformers 嵌入模型匹配源语与目标语术语，输出双语术语表。默认内置英西德法葡意 6 种中等 spaCy 模型，支持替换更小的多语言嵌入模型；提供 Docker、CLI 与 Web 应用（截至 2025 年 10 月网站维护中）。已被多篇 NLP 论文引用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从双语句子对或文档抽取并匹配术语，生成双语术语库
- 支持 .tmx/.mqxliff/.mxliff/.csv/.xlsx 五种双语文件格式
- spaCy 分词/词性标注 + sentence-transformers 嵌入匹配
- 默认含 6 种语言模型，可配置术语长度与词性过滤

## 适用场景

- 翻译/本地化项目构建双语术语库做质量保证
- 抽取双语术语用于微调机器翻译模型
- 外语教学中生成双语词表作为教学资源

## 场景标签

 · 领域:翻译技术/NLP

## 证据(README 行号)

> L3: **tm2tb** is a bilingual term extractor.
> L46: 2. Use an AI model to convert these terms to 'vectors' (a sequence of numbers, don't worry about this)

## 星数曲线

```mermaid
xychart-beta
    title "luismond/tm2tb 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-25 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `c530c1bad41d` · [字段定义](../../DATASET.md)*
