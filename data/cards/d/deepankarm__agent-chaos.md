# deepankarm/agent-chaos

⭐ 35 · Python · Apache-2.0 · 推送 2026-01-02 · [GitHub](https://github.com/deepankarm/agent-chaos) · 个人维护

**面向 AI agent 的混沌工程测试库：主动注入故障验证鲁棒性**

Python 库，面向构建生产级 agent 的团队：通过 scenario（baseline + 变体）机制向 agent 注入 LLM 故障（限流、500、超时、流中断）、工具故障（错误、超时、数据变异）、prompt 注入等混沌，并配以内置断言（如 MaxTotalLLMCalls、TokenBurstDetection）判定 agent 表现；支持 fuzz_chaos 随机组合故障探索，集成 DeepEval 与 Pydantic Evals 做 LLM-as-judge 语义评估。仅支持 Anthropic SDK 接入的模型，OpenAI/Gemini 为计划项；项目自述处于活跃开发中。提供 CLI 运行场景与 UI 查看结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM/工具/用户输入三类混沌注入器，可组合并按工具/轮次/调用次数定向
- 内置断言与 LLM-as-judge 集成（DeepEval、Pydantic Evals）
- fuzz_chaos 基于 ChaosSpace 配置随机生成故障组合
- CLI 运行场景与结果 UI

## 适用场景

- agent 上线前测试其对 LLM 限流、超时、流中断等故障的容错能力
- 检测工具返回空数据、坏 JSON、错实体时 agent 是否静默失败
- 用 LLM-as-judge 指标评估 agent 在故障下的回答质量

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: **Chaos engineering for AI agents.**
> L33: **agent-chaos** injects these failures so you can test how your agent handles them before users find out. It integr

## 星数曲线

```mermaid
xychart-beta
    title "deepankarm/agent-chaos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6d98b46537bf` · [字段定义](../../DATASET.md)*
