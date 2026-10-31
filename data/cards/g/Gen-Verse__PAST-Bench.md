# Gen-Verse/PAST-Bench

⭐ 35 · Python · Apache-2.0 · 推送 2026-08-05 · [GitHub](https://github.com/Gen-Verse/PAST-Bench) · [官网](https://arxiv.org/abs/2608.04003) · 组织维护 · 中文 README

**评测持久化 agent 跨会话自我改进能力的基准（26 任务族/204 集）**

PAST-Bench 是一个评测个人 agent 跨会话改进能力的基准：以有序任务族序列测试 agent 能否从前次会话经验中学习，配合持久化开/关对照与 trace 级证据做归因。包含记忆、程序复用、主动信息收集与更新四类共 26 任务族、204 episode。附带 Hermes+ 框架（Plan/Render/Route/Gate/Close 五机制），支持 MiniMax、GLM、Kimi、DeepSeek、GPT 等模型对照实验。运行需 Python 3.11+、uv、Docker 守护进程与各模型 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 26 任务族、204 episode 的纵向 fresh-session 序列评测
- 持久化开/关配对对照与 artifact/trace 级归因
- 附带 Hermes+ 改进框架及五机制消融实验
- 支持多模型与多 agent（Agent Zero/nanobot/ZeroClaw）对比

## 适用场景

- 评测我的 agent 能否从历史经验中真正改进
- 对 agent 记忆与自我改进机制做消融归因
- 跨模型、跨 agent 框架对比持久化改进效果

## 场景标签

`模型评测` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L18: **PAST-Bench** is a benchmark for evaluating and attributing cross-session improvement in persistent agents. Rather
> L22: - **PAST-Bench: a controlled benchmark for attributable cross-session improvement.** PAST-Bench evaluates agents th

## 星数曲线

```mermaid
xychart-beta
    title "Gen-Verse/PAST-Bench 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-31 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a3db3a78b51f` · [字段定义](../../DATASET.md)*
