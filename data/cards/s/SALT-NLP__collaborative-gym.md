# SALT-NLP/collaborative-gym

⭐ 163 · Python · MIT · 推送 2026-08-20 · [GitHub](https://github.com/SALT-NLP/collaborative-gym) · [官网](https://cogym.saltlab.stanford.edu/) · 组织维护

**人机协作 agent 的构建与评测框架（Co-Gym）**

SALT-NLP 维护的 Python 框架，用于构建和评测能与人类协作的 LLM agent。以 CoEnv 类建模共享工作区，人与 agent 可互发消息并执行动作，人类可实时干预；提供旅行规划、文献综述、表格分析三个任务环境，基于 Redis 跨进程通信。支持模拟人（如 gpt-4o）与真实用户两种实验条件，评测覆盖结果（Collab Score）与过程（主动性熵、受控自主性），并含 CollabSkill 贝叶斯评分模块分离人机贡献。通过 conda/pip 源码方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三个协作任务环境：旅行规划、文献综述、表格分析
- 模拟人与真实用户两种实验条件，附 386 会话轨迹数据集
- Collab Score 结果评测与主动性熵、受控自主性过程审计
- CollabSkill 贝叶斯评分分离 agent 与人的技能水平

## 适用场景

- 研究人机协作 agent 并做受控实验
- 用真实用户在线部署与评测协作 agent
- 比较不同 agent 在协作任务中的技能水平

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L9: Collaborative Gym (Co-Gym) is a framework for enabling and evaluating **Human-Agent Collaboration**. Unlike traditio
> L16: **We view Co-Gym as a framework for building and evaluating collaborative agents that take initiative at the correc
> L92: ## Evaluation

## 星数曲线

```mermaid
xychart-beta
    title "SALT-NLP/collaborative-gym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 162 --> 164
    line [163, 163]
```

2026-10-18 163 → 2026-10-24 163（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `4fc904507379` · [字段定义](../../DATASET.md)*
