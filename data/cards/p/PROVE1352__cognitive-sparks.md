# PROVE1352/cognitive-sparks

⭐ 17 · Python · MIT · 推送 2026-04-08 · [GitHub](https://github.com/PROVE1352/cognitive-sparks) · 个人维护 · 中文 README

**基于神经回路调度的 LLM 分析框架：13 个思维工具从数据中提取原理**

Python 包（sparks CLI），面向开发者做数据驱动的深度分析：用户提供目标与数据，由 13 个基于《Sparks of Genius》一书的思维工具（观察、抽象、类比、建模等）产出核心原理、可验证预测与反馈循环。关键机制是速率编码 LIF 神经回路加 STDP 学习决定工具触发顺序，而非硬编码流水线；权重持久化跨会话演化。支持 Claude/GPT-4o/Gemini/Ollama/Groq 后端，按深度模式产生相应 API 费用；大型数据集基准测试仍标记为未完成。

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

- 13 个思维工具的执行顺序由 LIF+STDP 神经回路涌现决定，非硬编码流水线
- 完整闭环：验证→演化→预测→反馈→自优化（Phase A-F）
- 多后端支持：Claude（默认）/OpenAI/Gemini/Ollama/Groq
- quick/standard/deep 三档深度模式对应不同工具数与预算

## 适用场景

- 给定目标与数据，让系统自主提取核心原理与规律
- 从已验证原理生成可检验的预测并与实际结果对比
- 跨会话累积学习，观察工具组合权重的演化

## 场景标签

`数据分析` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L111: Phase A: sparks run     Data -> 13 Tools -> Principles
> L131: |`cli` (default)|Claude Code CLI|Free with subscription|

## 星数曲线

```mermaid
xychart-beta
    title "PROVE1352/cognitive-sparks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e9ba00cd74db` · [字段定义](../../DATASET.md)*
