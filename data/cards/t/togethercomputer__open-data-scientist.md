# togethercomputer/open-data-scientist

⭐ 190 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/togethercomputer/open-data-scientist) · 组织维护

**执行数据分析任务并生成报告的 ReAct 数据科学 AI Agent**

基于 ReAct（推理+行动）框架的数据分析 Agent：接收用户数据目录，迭代生成并执行 Python 代码，输出完整分析报告。代码执行支持两种模式——云端 Together Code Interpreter（TCI，需 Together API key，文件上传云端）或本地 Docker 容器（文件留在本地，会话隔离有限制）。提供 CLI 与 Python API，默认模型 DeepSeek-V3，可保存推理与执行 trace。README 声明为实验性工具，AI 生成代码可能含错误，需人工核验，不建议生产使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- ReAct 框架迭代执行数据分析并生成详细报告
- TCI 云端与本地 Docker 两种代码执行模式
- CLI 与 Python API 两种使用方式，默认模型可配置
- 可保存查询/执行 trace 为 JSONL 与 Markdown 日志

## 适用场景

- 上传数据集自动完成探索性数据分析
- 生成包含结果与图表的分析报告
- 以本地 Docker 方式在自有环境执行 AI 生成的代码

## 场景标签

 · 领域:数据科学/LLM Agent

## 证据(README 行号)

> L3: An AI-powered data analysis assistant that follows the ReAct (Reasoning + Acting) framework to perform comprehensive
> L32: Our Open Data Scientist can perform comprehensive data analysis and generate detailed reports. Below is an example 

## 星数曲线

```mermaid
xychart-beta
    title "togethercomputer/open-data-scientist 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 189 --> 191
    line [190, 190]
```

2026-10-18 190 → 2026-10-24 190（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6e632724f22f` · [字段定义](../../DATASET.md)*
