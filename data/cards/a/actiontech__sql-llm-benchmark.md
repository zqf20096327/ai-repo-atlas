# actiontech/sql-llm-benchmark

⭐ 25 · TypeScript · MIT · 推送 2026-07-01 · [GitHub](https://github.com/actiontech/sql-llm-benchmark) · [官网](https://sql-llm-leaderboard.com) · 组织维护 · 中文 README

**评测 LLM SQL 能力的脚本与榜单系统**

由两部分组成：evaluator 评测脚本负责对目标 LLM 在 SQL 理解、方言转换、SQL 优化三个维度打分，支持客观题自动判分与 LLM-as-a-judge 主观判分，并集成 MCP 网络搜索供裁判模型实时检索数据库文档；leaderboard 基于 Next.js 展示榜单与详细报告，含 SSR。用户可自定义数据集、目标模型与裁判模型，按指标权重与难度（1-3 级）加权计分，自动生成三类报告，并接受社区提交模型评测报告上榜。运行需 Python 3.10+ 与 Node.js 18.18+。

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

- SQL 理解/方言转换/SQL 优化三维度评测，客观+LLM-as-a-judge 混合判分
- MCP 网络搜索增强裁判模型的判分依据
- 按指标权重与难度等级（1-3 级）加权计算能力分
- Next.js 榜单前端，支持社区提交模型评测报告上榜

## 适用场景

- 评测自家 LLM 的 SQL 能力并提交到公开榜单
- 对比多个模型在 SQL 理解与优化上的表现
- 用自定义数据集扩展评测维度与测试用例

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: This project provides a script tool and a leaderboard for evaluating the SQL capabilities of Large Language Models (
> L25: This project consists of two main parts: the LLM Evaluation Script (`evaluator`) and the Leaderboard UI (`leaderboa

## 星数曲线

```mermaid
xychart-beta
    title "actiontech/sql-llm-benchmark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `953786a3adce` · [字段定义](../../DATASET.md)*
