# lfoppiano/grobid-quantities

⭐ 86 · JavaScript · Apache-2.0 · 推送 2026-09-13 · [GitHub](https://github.com/lfoppiano/grobid-quantities) · [官网](https://grobid-quantities.readthedocs.io) · 组织维护

**GROBID 扩展：从科技文献中识别并归一化物理量测量表达**

GROBID 的扩展模块，面向技术与科学文献和专利（支持文本、XML、PDF 输入），识别文中的测量表达（如压力、温度），进行解析与归一化并转换为 SI 单位。支持数值、字母、指数及日期/时间等多种数值表示形式，并可识别测量所关联的被量化物质。模型仅依赖机器学习，使用线性 CRF；单位归一化由 Java 库 Units of measurement 处理。提供 Hugging Face Spaces 在线演示，当前版本 0.8.2，标注为开发进行中（work in progress）。自 2015 年由 science-miner 开发，获 Inria 与日本物质材料研究机构支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 识别测量表达并解析归一化为 SI 单位
- 支持数值/字母/指数/日期时间多种表示形式
- 识别测量所关联的被量化物质
- 基于线性 CRF 机器学习模型，单位归一化使用 Java 库 Units of measurement

## 适用场景

- 科技文献中抽取压力、温度等测量数据
- 批量解析文献 PDF/XML 并统一转换为 SI 单位
- 通过 REST API 集成到文本与数据挖掘流程

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: The goal of this GROBID module is to recognize in textual documents any expressions of measurements (e.g. _pressure
> L30: As with the other GROBID models, the module relies only on machine learning and it uses linear CRF.

## 星数曲线

```mermaid
xychart-beta
    title "lfoppiano/grobid-quantities 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-30 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `24c39a143bf5` · [字段定义](../../DATASET.md)*
