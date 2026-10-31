# hiDaDeng/cntext

⭐ 470 · Python · MIT · 推送 2026-05-03 · [GitHub](https://github.com/hiDaDeng/cntext) · [官网](https://textdata.cn/) · 个人维护 · 中文 README

**面向计算社会科学的中英文文本分析与语义投影 Python 库**

为计算社会科学研究者提供的 Python 文本分析库，含六大模块：读取 PDF/DOCX/CSV 等文件与文本清洗、词频/可读性/词典情感/相似度等统计、词嵌入训练与加载（Word2Vec/GloVe/FastText/SoPmi）、语义投影测量（WEPA 语义轴打分）以及 LLM 辅助结构化文本分析。内置 NRC、DUTIR、HowNet、NTUSD 等中英文 YAML 词典。核心的 WEPA 方法通过正负锚点词构造语义轴，将文本投影得到构念相关的语言显著性指标。限制：WEPA 分数不可解释为潜在心理状态的直接观测或临床诊断；原始论文数据因隐私不随仓库分发。

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

- WEPA 语义投影工作流：锚点词构轴、文本投影打分，附论文复现与最小示例
- 支持 Word2Vec/GloVe/FastText/SoPmi 嵌入训练、加载与词典扩展
- 内置 NRC/LoughranMcDonald/DUTIR/HowNet/NTUSD 等中英文 YAML 词典
- LLM 模块提供结构化文本分析（analysis_by_llm 等）

## 适用场景

- 我从社交媒体或财报文本测量心理构念的语言显著性
- 我用词典法做中英文情感、不确定性（EPU）等内容分析
- 我训练词嵌入并做语义投影、语义距离等指标计算

## 场景标签

`科研工具` `语义搜索` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L7: **cntext** is a Python package for computational social science researchers who work with text data. It supports fil
> L124: |`mind`|`generate_concept_axis`, `project_text`, `wepa`, `sematic_projection`, `project_word`, `semantic_centroid`

## 星数曲线

```mermaid
xychart-beta
    title "hiDaDeng/cntext 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 467 --> 471
    line [468, 469, 470]
```

2026-10-18 468 → 2026-10-31 470（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0706bb0bec7e` · [字段定义](../../DATASET.md)*
