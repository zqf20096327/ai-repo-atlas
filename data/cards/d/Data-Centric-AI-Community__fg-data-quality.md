# Data-Centric-AI-Community/fg-data-quality

⭐ 455 · Jupyter Notebook · MIT · 推送 2026-04-23 · [GitHub](https://github.com/Data-Centric-AI-Community/fg-data-quality) · 组织维护

**Python 数据质量评估库：一行代码检测数据管道中的质量问题**

开源 Python 库 data_quality（PyPI 包名 fg-data-quality），面向数据管道开发多阶段的数据质量评估：以单一 Data Quality 引擎对 pandas 数据做多维度模块化检查，输出汇总与可检索的警告列表。模块覆盖偏差与公平性、数据期望、数据关系、漂移分析、重复、标签、缺失与错误数据，并附教程 notebook。前身为 ydata_quality 包，README 提供迁移指南（卸载旧包、替换导入）。GPL-3.0 许可，由 YData 开发团队维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单引擎多维度数据质量检查，输出汇总与警告列表
- 8 个检查模块：偏差公平性/数据期望/漂移/重复/缺失等
- 提供 ydata_quality → fg-data-quality 迁移指南
- 基于 pandas 的 Python API

## 适用场景

- 数据管道各阶段对 pandas 数据做整体质量体检
- 检测数据漂移、缺失、重复与错误数据并获取明细警告
- 从旧的 ydata_quality 迁移到新包名

## 场景标签

 · 领域:数据工程/机器学习数据

## 证据(README 行号)

> L3: data_quality is an open-source python library for assessing Data Quality throughout the multiple stages of a data pi
> L5: A holistic view of the data can only be captured through a look at data from multiple dimensions and `data_quality` 

## 星数曲线

```mermaid
xychart-beta
    title "Data-Centric-AI-Community/fg-data-quality 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 454 --> 456
    line [455, 455]
```

2026-10-18 455 → 2026-10-22 455（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `bb4b27831ad5` · [字段定义](../../DATASET.md)*
