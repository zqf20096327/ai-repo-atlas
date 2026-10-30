# sentencizer/sentencizer

⭐ 48 · Go · MIT · 推送 2026-09-07 · [GitHub](https://github.com/sentencizer/sentencizer) · [官网](https://gosbd.pages.dev/) · 组织维护

**Go 语言的规则式句子切分库，服务 RAG 预处理**

受 pySBD 与 pragmatic_segmenter 启发的 Go 原生句界消歧库，按规则将文本切分为句子且不改动原文，开箱即用无需模型或外部依赖。提供语言特定标点配置与文本清洗（处理异常换行、目录、URL/HTML 标签、无空格分隔句等，Clean 移植自 pySBD）。定位为 Go 生态下构建 RAG 系统的关键预处理组件，目前支持中文、英文、希伯来语、日语、立陶宛语、俄语，其余语言列入计划，社区贡献中。MIT 许可，附带在线 Playground。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则式句界消歧，开箱即用，无需模型或外部依赖
- 非破坏性切分：保留原文内容不变
- sentencizer.Clean() 文本清洗（异常换行、目录、URL/HTML、无空格分隔句）
- 语言特定标点配置，当前支持 zh/en/he/ja/lt/ru 六种语言

## 适用场景

- Go 项目中为 RAG 管道做句子级切分预处理
- 清洗带噪声的原始文本后再做检索或切句
- 为不同语言的标点规则做句子边界消歧

## 场景标签

 · 领域:NLP/文本处理工具库

## 证据(README 行号)

> L7: Sentencizer is a library for segmenting text into sentences, designed to make it easier to build Retrieval Augmented
> L86: Sentence splitting is a crucial step in the preprocessing pipeline of Natural Language Processing (NLP) tasks, espe
> L88: While libraries like pragmatic_segmenter and pySBD are known for their high accuracy and efficiency in sentence spl

## 星数曲线

```mermaid
xychart-beta
    title "sentencizer/sentencizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-30 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `52f86ce133c9` · [字段定义](../../DATASET.md)*
