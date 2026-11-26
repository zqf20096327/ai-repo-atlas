# KarimELMERNISSI/Cohort-Studio

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/KarimELMERNISSI/Cohort-Studio) · [官网](https://karimelmernissi.github.io/Cohort-Studio/) · 个人维护

**给临床研究者的队列数据分析与可复现报告应用**

面向临床研究人员、生物统计学家与健康数据科学家的开源本地优先应用：从原始文件加载数据后完成数据质量评分（含多种异常检测算法）、以勾选条件定义分析人群并生成参与者流程、缺失数据多重插补并以 Rubin 规则合并、生存与回归建模，最终产出 Word 报告与研究档案。所有数据变更记录在哈希链追溯的 JSON 轨迹中，headless 引擎可重放并逐步校验指纹。基于 Python 3.14+ 与 Streamlit，AI 助手为可选组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 哈希链追溯的 JSON 轨迹与可校验重放机制（run_trace）
- 数据质量评分：完整性、一致性及 Isolation Forest、LOF、DBSCAN 异常检测
- 多重插补与 Rubin 规则合并、Cox 生存模型、诊断准确度指标
- 可选 AI 助手支持本地 Ollama 与多家云服务商，需显式同意

## 适用场景

- 从原始队列数据生成带参与者流程的分析人群
- 对注册数据库做缺失数据插补并合并生存模型结果
- 为 observational cohort 研究产出 Word 研究档案
- 核查数据变更轨迹以复现已发表的分析结果

## 场景标签

`数据分析` `科研工具` · 领域:效率与自动化

## 证据(README 行号)

> L8:  An open-source, local-first application for observational cohort studies.
> L43: 4. **Optional AI assistant** (the `ai` group): connectors for local Ollama (the default), Google Gemini, OpenAI, Mi
> L30: **CohortStudio** is built for clinical researchers, biostatisticians and health data scientists who work with obser

## 星数曲线

```mermaid
xychart-beta
    title "KarimELMERNISSI/Cohort-Studio 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-24 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `5ec0d8720e6d` · [字段定义](../../DATASET.md)*
