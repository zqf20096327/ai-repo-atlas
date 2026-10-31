# theoria-dataset/theoria-dataset

⭐ 15 · Jupyter Notebook · 推送 2026-04-06 · [GitHub](https://github.com/theoria-dataset/theoria-dataset) · [官网](https://theoria-dataset.github.io/theoria-dataset/) · 组织维护

**理论物理方程与推导的结构化训练数据集**

面向机器学习训练的理论物理数据集：以每条物理结果（如洛伦兹变换）一个 JSON 文件的格式，收录方程、AsciiMath 分步推导与注释、ArXiv 风格领域标签，条目由物理背景贡献者撰写并附贡献者姓名或 ORCID。提供 manifest.json 元数据、基于 JSON Schema 的 CI 校验、make/python 本地测试脚本，并可用 jq 合并为单一 dataset.json 供训练管线使用。采用 CC-BY 4.0 许可，欢迎研究者、教育者以 PR 方式贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每条物理结果一个 JSON 条目，含分步推导与注释
- ArXiv 风格领域标签（gr-qc、hep-th 等）便于过滤
- JSON Schema 作为校验与贡献指南的单一事实源，CI 自动校验
- 可用 jq 合并生成单一 dataset.json 供训练管线使用

## 适用场景

- 为 ML 模型训练获取结构化的物理方程与推导数据
- 按物理子领域过滤和浏览方程条目
- 研究者/教育者以 PR 方式贡献方程条目

## 场景标签

 · 领域:科学数据/物理

## 证据(README 行号)

> L16: There is a lack of curated datasets with all important equations and derivations of theoretical physics to train be
> L18: TheorIA bridges that gap; it is the first datasets being built to provide a high-quality collection of theoretical 

## 星数曲线

```mermaid
xychart-beta
    title "theoria-dataset/theoria-dataset 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `3c0852b51851` · [字段定义](../../DATASET.md)*
