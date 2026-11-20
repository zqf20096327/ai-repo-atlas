# shimo4228/contemplative-agent

⭐ 10 · Python · MIT · 推送 2026-11-18 · [GitHub](https://github.com/shimo4228/contemplative-agent) · [官网](https://doi.org/10.5281/zenodo.19212118) · 个人维护 · 中文 README

**研究者驱动的自主 agent 实验：本地 LLM 自主发帖并提议修改自身约束**

一个在 Moltbook（仅 AI agent 发帖的社交网络）上运行的自主 agent 实验：通过 Ollama 在单台 16 GB Mac 上使用本地 LLM 发帖与回复，将每个动作写入 episode 日志，从日志提炼模式并据此提议修改自身的 constitution、身份与技能（提示词层），所有提议须经人工在审批门处采纳或拒绝，采纳历史公开于 contemplative-agent-data 仓库。定位为实验而非生产力工具，面向研究 agent 价值观形成与修订的研究者。默认生成与嵌入模型均本地运行，无 API key，仅两个运行时依赖，无 shell 执行能力。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- propose→approval gate→adopt 的价值观修订流水线，每次决策带文本哈希入日志
- 全部生成与嵌入走本地 Ollama（默认 Gemma 4 E4B + nomic-embed-text），无 LLM API key
- 默认 constitution 为 Contemplative AI 四公理，另有 10 个预设（Stoic、utilitarian 等）一键切换
- 无 shell 执行、无任意网络访问、无文件遍历，仅 requests 与 numpy 两个运行时依赖

## 适用场景

- 研究 agent 长期运行中价值观如何被提议与修订
- 在本地推理上运行无 shell 能力的自主发帖 agent
- 用不同 constitution 的两个 agent 在本地管道中对话观察价值差异

## 场景标签

 · 领域:AI 对齐/agent 实验研究

## 证据(README 行号)

> L17: Contemplative Agent is an autonomous agent that lives on Moltbook, a social network where only AI agents post. It r
> L19: It is an experiment, not a productivity tool. The question it asks is what happens to an agent's values when it kee
> L49: You need Ollama, Python 3.11 or later, uv (or plain `python3 -m venv` and `pip`), and about 10 GB of disk for the m

## 星数曲线

```mermaid
xychart-beta
    title "shimo4228/contemplative-agent 星数(近 2 点)"
    x-axis ["2026-11-10", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-10 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `b03b87c84461` · [字段定义](../../DATASET.md)*
