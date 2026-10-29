# bio-ontology-research-group/mowl

⭐ 97 · Python · BSD-3-Clause · 推送 2026-10-01 · [GitHub](https://github.com/bio-ontology-research-group/mowl) · 组织维护

**基于本体背景知识的机器学习 Python 库，面向生物医学研究**

mOWL 是 Python 机器学习库，将本体（ontologies）作为背景知识用于机器学习方法（如本体嵌入）。通过 JPype 绑定 JVM，集成了 Java 编写的 OWLAPI 功能；由 KAUST 生物本体研究组发起开发，相关论文发表于 Bioinformatics。系统依赖为 JDK>=22、Python 3.9-3.12 与 Conda，Python 侧依赖 torch、gensim、JPype1、pykeen、scipy。支持 PyPI 与源码 pip 安装，采用 BSD-3-Clause 许可。

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

- 将本体作为背景知识的机器学习方法库
- 通过 JPype 集成 Java OWLAPI 功能
- 支持本体嵌入等多种方法与算法接口

## 适用场景

- 生物医学本体上训练与评估本体嵌入
- 做神经符号/知识增强的基因变异优先级研究
- 将本体背景知识接入机器学习流程

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L10: **mOWL** is a library that provides different machine learning methods in which ontologies are used as background k
> L11: mainly in Python, but we have integrated the functionalities of OWLAPI, which is written in Java, for which we use 
> L53: **mOWL** is a project initiated and developed by the Bio-Ontology Research Group from KAUST.

## 星数曲线

```mermaid
xychart-beta
    title "bio-ontology-research-group/mowl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 96 --> 98
    line [97, 97]
```

2026-10-18 97 → 2026-10-29 97（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a9dd4cd0f84d` · [字段定义](../../DATASET.md)*
