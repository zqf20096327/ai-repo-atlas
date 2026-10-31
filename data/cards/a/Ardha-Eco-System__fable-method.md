# Ardha-Eco-System/fable-method

⭐ 14 · Python · MIT · 推送 2026-09-09 · [GitHub](https://github.com/Ardha-Eco-System/fable-method) · [官网](https://github.com/ardhaecosystem/fable-method) · 组织维护

**给任意模型加结构化解题循环的 Hermes Agent 技能包（四技能+对抗评测）**

面向 Hermes Agent 的纪律层插件：以四个技能（fable-method 思考循环、fable-loop 并行执行、fable-judge 对抗性核验、fable-domain 领域适配生成器）约束模型按 7 步循环解题，在决策点强制产出 INTENT/AUTH/TWINS/PENDING 等工件，设定停止边界（3 次验证失败即停）。附三个陷阱场景的 A/B 评测，通过 diff 与执行而非阅读报告来判定。安装依赖 Hermes Agent 插件机制，其他 agent（Codex/Cursor/aider）可经 AGENTS.md 使用；含 8 个领域适配器，医疗领域刻意不提供。

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

- 7 步解题循环与强制决策点工件（INTENT/AUTH/TWINS/PENDING）
- fable-judge 将报告视为声明，通过 diff 与执行复核，检测弱化测试、虚假完成等
- fable-domain 可为新行业生成适配器（含陷阱 fixture 与冒烟评测）
- 三个陷阱场景 A/B 评测，结果记录于 eval/RESULTS.md

## 适用场景

- 让编码 agent 在执行多步任务前先定义完成标准并验证
- 复核 agent 声称已完成的工作是否属实
- 为代码之外的领域（研究、数据分析、合规等）套用同一解题循环

## 场景标签

`Agent 框架` `提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L7: A discipline layer for Hermes Agent that gives any model, regardless of tier, structured problem-solving thinking. F
> L27: hermes plugins install ardhaecosystem/fable-method --enable

## 星数曲线

```mermaid
xychart-beta
    title "Ardha-Eco-System/fable-method 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5f094aecefc4` · [字段定义](../../DATASET.md)*
