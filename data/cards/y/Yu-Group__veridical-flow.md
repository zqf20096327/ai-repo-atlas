# Yu-Group/veridical-flow

⭐ 75 · Jupyter Notebook · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Yu-Group/veridical-flow) · [官网](https://vflow.csinva.io) · 组织维护

**数据科学管道稳定性分析库：评估判断选择对结果的影响**

基于 PCS（predictability, computability, stability）框架的 Python 库 vflow，用于构建可验证的数据科学管道：用简单包装器把预处理、建模、评估等环节替换为一组函数（Vset），自动并行化与缓存（Ray/joblib），经 MLflow 记录实验，并调用 stability_report 生成指标对各扰动源（如抽样、模型选择）的方差分解与排名报告。另附 Claude Code 插件 agents/，让多个分析 agent 在真实数据、打乱列副本及多种扰动下重复回答数据集问题并汇总判定。通过 pip 安装。

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

- 用 Vset 替换单一函数并评估下游结果稳定性
- stability_report 输出方差分解、排名等 DataFrame 表格
- Ray 后端自动并行化与 joblib 缓存，MLflow 实验记录
- Claude Code 插件以多 agent 重复分析验证数据集问题

## 适用场景

- 检验指标对插补策略、模型选择等判断的敏感度
- 按 PCS 框架组织可复现的数据科学实验
- 让 AI 分析结果经受打乱数据与扰动的检验

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L18: Using `vflow`s simple wrappers facilitates many best practices for data science,
> L20: for veridical data science. The goal
> L22: providing intuitive low-code syntax, efficient and flexible computational

## 星数曲线

```mermaid
xychart-beta
    title "Yu-Group/veridical-flow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-25 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8593ead9f846` · [字段定义](../../DATASET.md)*
