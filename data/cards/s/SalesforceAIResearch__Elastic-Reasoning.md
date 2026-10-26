# SalesforceAIResearch/Elastic-Reasoning

⭐ 51 · Jupyter Notebook · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/SalesforceAIResearch/Elastic-Reasoning) · 组织维护

**让推理模型可伸缩的训练框架：思考与解答分阶段预算控制**

Salesforce AI Research 发布的可伸缩链式推理研究框架：将推理显式拆分为 thinking 与 solution 两个阶段并各自分配 token 预算，在资源受限时优先保证解答段完整。通过集成进 GRPO 的 budget-constrained rollout 策略训练模型适应被截断的思考过程，并泛化到未见过的预算约束。提供 E1-Math-1.5B/7B、E1-Code-14B、E1-AceReason-14B 等基于 Hugging Face 发布的模型，以及基于 rllm/verl 代码库的训练、数据预处理与评测脚本。声明仅用于研究目的。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- thinking/solution 两阶段分离，各自独立 token 预算
- budget-constrained rollout 集成 GRPO 训练，适应思考截断
- 发布 E1-Math/E1-Code/E1-AceReason 系列模型
- 提供 AIME、MATH、LiveCodeBench、Codeforces 评测脚本

## 适用场景

- 在受限推理预算下运行/训练推理模型
- 复现论文中预算约束推理的训练与评测流程
- 基于开源模型做数学与代码推理基准评测

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L23: introduce a lightweight `budget-constrained rollout` strategy, integrated into GRPO,
> L65: ./scripts/e1-math/e1_math_1.5b_1k_1k.sh --model $MODEL_PATH

## 星数曲线

```mermaid
xychart-beta
    title "SalesforceAIResearch/Elastic-Reasoning 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-26 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ffc06699d59a` · [字段定义](../../DATASET.md)*
