# Rootly-AI-Labs/rootly-doom-agent-arena

⭐ 18 · C · 推送 2026-10-23 · [GitHub](https://github.com/Rootly-AI-Labs/rootly-doom-agent-arena) · 组织维护

**在 Doom 游戏中对模型进行实时 1v1 对战的评测竞技场**

由 Rootly AI Labs 维护的 MCP 原生评测平台：两个模型各自作为 MCP agent 接入 Doom 对战，每回合提交高层路线计划（目标、推理、路线单元格），由游戏引擎实时执行，记录胜负、决策速度、命中率、伤害差与每美元胜率等指标。README 展示了 GPT-6 三个变体共 60 场对局的排行榜与方法论，并附对战产出物（events.jsonl、stats.json 等）供复算。安装运行依赖 Quick Start 与 Docker Runtime 等外部文档链接，README 内未给出具体命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型通过 MCP 提交高层路线计划（objective/reasoning/route），非帧级操控
- 记录决策速度、命中率、伤害差与每美元胜率等指标
- 每轮输出可复算的 artifacts（prompts、events.jsonl、stats.json、summary.json）
- 提供 Docker Runtime、MCP Duel Runbook 等配套文档

## 适用场景

- 对模型做实时对抗环境下的时空规划与自适应能力评测
- 比较不同模型的成本效率（胜率/每美元）
- 研究 agent 决策延迟与胜率的关系

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Benchmark model duels in Doom.
> L5: An MCP-native arena for real-time model-vs-model evaluations.
> L81: Each duel runs with two separate MCP agents, one for `player_1` and one for `player_2`. The browser starts a round,

## 星数曲线

```mermaid
xychart-beta
    title "Rootly-AI-Labs/rootly-doom-agent-arena 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `72f30dcafa94` · [字段定义](../../DATASET.md)*
