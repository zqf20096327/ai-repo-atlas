# cheanus/SRSA

⭐ 22 · Python · MIT · 推送 2026-03-24 · [GitHub](https://github.com/cheanus/SRSA) · 个人维护 · 中文 README

**给 AI agent 的记忆自改进层：用间隔重复复习记忆卡片**

SRSA 是叠加在任意 agent 记忆系统之上的记忆自改进层：将 agent 记忆转化为可复习的卡片，借助 FSRS 间隔重复算法调度复习，agent 在复习中回忆知识、与真实情况对比、评估正确性并修正错误记忆，从而缓解记忆漂移、检索失配与记忆过时等问题。以 skill 形式集成，通过 clawhub install srsa 安装，可配置 desired_retention 调节复习频率。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 记忆→卡片→定时复习→自我评估→记忆更新的闭环流程
- 使用 FSRS 算法调度复习以减少不必要的复习次数与 token 消耗
- 与具体记忆系统解耦，适用于任意 agent 记忆架构
- 复习分析：跟踪回忆表现与记忆演化

## 适用场景

- 我想让 AI agent 的长期记忆随时间自我修正而不是越来越失准
- 我想降低 agent 记忆复习带来的 token 开销
- 我想跟踪 agent 记忆的回忆表现变化

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: SRSA (Spaced Repetition Systems for AI Agents) is a **memory self-improvement layer** that converts agent memories i
> L66: SRSA acts as a layer on top of any agent memory system.
> L105: clawhub install srsa

## 星数曲线

```mermaid
xychart-beta
    title "cheanus/SRSA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `726805a6f456` · [字段定义](../../DATASET.md)*
