# worldbank/ai4data

⭐ 16 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/worldbank/ai4data) · [官网](https://worldbank.github.io/ai4data/) · 组织维护

**世界银行项目工具集：用 AI 生产/治理统计数据并让数据可被 AI 使用**

世界银行 Development Data Group 的 AI for Data – Data for AI 项目聚合仓库，提供方法、软件与指南。Python 包 ai4data 覆盖八项能力：数据集提及抽取与名称规范化、时序异常检测与四类解释、基于嵌入的目录语义搜索、元数据模式映射与五 agent 元数据审查、PDF 图表抽取为结构化数据等；另有 @ai4data npm 包支持浏览器内混合检索（HNSW+BM25）、端到端参考实现（含 MCP 服务与 Proof-Carrying Numbers 数字核验）及 11 部面向统计机构的操作手册（工作草稿，非官方指南）。面向工程师、数据管理员、统计机构管理者与研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五 agent 元数据审查流水线（检测/批评/分类/严重度评分），支持 OpenAI/Anthropic/Azure/Ollama
- Proof-Carrying Numbers：核验聊天回答中数字与源记录是否一致（论文 arXiv:2509.06902）
- @ai4data/search 浏览器内语义检索：HNSW、BM25、混合排序，Web Worker 运行
- 零样本 NER 抽取文档中的数据集提及并做变体归一与去重

## 适用场景

- 统计机构审查与修复不完整/矛盾的元数据
- 为 AI 系统准备可发现、可溯源的官方统计数据
- 在聊天回答中核验数字与权威记录是否一致
- 从 PDF 报告中定位图表并转换为结构化数据

## 场景标签

`语义搜索` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L66: Input: a World Development Indicators series record whose name reads "GDP per capita (curent US$)" and whose measur
> L106: ```python
> L136: pip install ai4data              # core

## 星数曲线

```mermaid
xychart-beta
    title "worldbank/ai4data 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-23 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d16cc4ad7ba8` · [字段定义](../../DATASET.md)*
