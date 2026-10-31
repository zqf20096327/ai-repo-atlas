# langchain-ai/lca-engine

⭐ 21 · Python · 推送 2026-07-23 · [GitHub](https://github.com/langchain-ai/lca-engine) · 组织维护

**LangChain 学院课程示例：招聘 Agent 与 LangSmith 评测工作流**

LangChain Academy 课程配套仓库：包含一个招聘助理 Agent（职位查询、构建候选人画像、候选人评分、发送邮件，基于 LangChain/LangGraph），以及 LangSmith 评测脚本 eval.py 和 GitHub Actions 工作流——在 PR 打上 run_evals 标签时自动检出 PR head 并对配置的 LangSmith 数据集运行实验。运行需自行配置 LangSmith API key、项目名与数据集（仓库不含数据集），CI 还需 OPENAI_API_KEY。供学习 Agent 构建与评测流程的开发者使用；需手动创建 run_evals 标签与仓库 secrets。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 招聘 Agent：职位查询、候选人画像、评分、发邮件
- LangSmith evaluate() 评测脚本（eval.py），支持 --dataset 与 --experiment-prefix
- GitHub Actions 工作流：PR 打 run_evals 标签即在 CI 中跑评测
- 提供 gh 命令配置 secrets 与标签、本地复现 PR 评测的操作说明

## 适用场景

- 学习 LangGraph Agent 与 LangSmith 评测的集成方式
- 在 PR 流程中自动对 Agent 变更跑评测实验
- 本地复现 CI 评测做合并前后对比

## 场景标签

`模型评测` `教程课程` · 领域:评测与运维

## 证据(README 行号)

> L3: A recruiting assistant agent (job lookup, building candidate profiles, scoring candidates, and
> L4: sending emails to candidates) with a LangSmith evaluation harness and a GitHub Actions workflow
> L11: - LangSmith for tracing + evals (`eval.py`)
> L182: |`eval.py`|LangSmith `evaluate()` harness.|

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/lca-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0e1251491097` · [字段定义](../../DATASET.md)*
