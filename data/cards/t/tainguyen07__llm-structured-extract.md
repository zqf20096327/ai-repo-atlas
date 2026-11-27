# tainguyen07/llm-structured-extract

⭐ 10 · Python · MIT · 推送 2026-08-21 · [GitHub](https://github.com/tainguyen07/llm-structured-extract) · 个人维护

**给开发者的 LLM 结构化抽取库：Pydantic 校验与修复重试**

Python 库与 CLI：开发者定义 Pydantic v2 模型，指向一个 provider 即可得到通过 schema 校验的结构化对象。核心机制包括校验失败后的 retry/repair 循环（把破损输出与 schema 回传给模型要求修复）、确定性 JSON 修复、异步批量流水线（限并发、感知限流）、逐次调用的 token 与费用统计以及可选磁盘缓存。提供 OpenAI、Anthropic、Mock 三个内置 provider，可子类化自定义；MIT 许可，pip 或源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Pydantic v2 模型输入，返回 schema 校验后的对象实例
- retry/repair 循环与确定性 JSON 修复步骤
- 异步批量流水线：并发限制、限流感知、部分失败容忍
- 逐调用 token/费用统计与按 (model, prompt, schema) 的磁盘缓存

## 适用场景

- 从 LLM 输出中稳定抽取发票、合同等结构化数据
- 批量处理大量抽取任务并跟踪成本
- 消除模型输出格式不稳定带来的重试成本

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L9: Pulling typed data out of an LLM is easy until the model hallucinates a missing bracket, returns prose instead of JS
> L19: - **Provider abstraction.** `OpenAIProvider`, `AnthropicProvider`, `MockProvider`. One interface; swap with a confi
> L27: - **Battle-tested patterns.** Mirrors the well-known `instructor` library's approach but without the framework lock

## 星数曲线

```mermaid
xychart-beta
    title "tainguyen07/llm-structured-extract 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `729302d09256` · [字段定义](../../DATASET.md)*
