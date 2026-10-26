# GeoPandas-AI/geopandas-ai

⭐ 31 · Python · MIT · 推送 2026-06-16 · [GitHub](https://github.com/GeoPandas-AI/geopandas-ai) · [官网](http://geopandas.ai/) · 组织维护

**GeoPandas 扩展库：用自然语言对话式操作地理空间数据**

由布鲁塞尔自由大学 Data Science and Engineering Lab 开发的 Python 库，提供 GeoDataFrameAI 类，将 LLM 嵌入地理空间分析工作流：用户通过 .chat() 以自然语言查询数据、由 LLM 生成并执行 Python 代码，.improve() 支持迭代修正；结果与生成代码默认缓存到磁盘（.gpd_cache/）以避免重复调用。采用依赖注入架构，可配置 LiteLLM、缓存后端、代码执行器（可信或沙箱）、注入器等模块。兼容现有 GeoDataFrame 工作流，需 Python 3.8+，有配套 arXiv 论文。

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

- GeoDataFrameAI 类的 .chat()/.improve() 自然语言查询与迭代修正
- 默认磁盘缓存，重复提示复用结果不产生额外 LLM 调用
- 依赖注入架构：LiteLLM、缓存、代码执行器、注入器等模块均可配置
- 支持包裹现有 GeoDataFrame 与多 dataframe 协同工作

## 适用场景

- 不熟悉 GIS 概念的用户用自然语言分析空间数据
- 在现有 GeoPandas 工作流中加入对话式查询与代码生成
- 通过缓存机制控制 LLM 调用成本并加速重复分析

## 场景标签

`代码生成` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: **GeoPandas-AI** is an open-source Python library that enhances geospatial data analysis by turning the `GeoDataFram
> L30: - ✅ A stateful, LLM-augmented `GeoDataFrameAI` class
> L141: This project is a product of the Université Libre de Bruxelles (ULB), and most notably the Data Science and Engine

## 星数曲线

```mermaid
xychart-beta
    title "GeoPandas-AI/geopandas-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-26 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2bf31f3184d4` · [字段定义](../../DATASET.md)*
