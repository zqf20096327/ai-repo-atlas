# vstorm-co/pydantic-ai-shields

⭐ 94 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/vstorm-co/pydantic-ai-shields) · [官网](https://vstorm-co.github.io/pydantic-ai-shields/) · 组织维护

**为 Pydantic AI agent 提供即插式安全护栏库**

面向 Pydantic AI 开发者的护栏能力库：通过 capabilities API 向任意 agent 注入成本与预算封顶（超限抛 BudgetExceededError，价格经 genai-prices 自动探测）、工具封禁/审批、输入输出校验，以及提示注入检测（6 类、3 档灵敏度）、PII 检测、密钥脱敏、关键词封锁与拒绝回复拦截；AsyncGuardrail 支持并发/阻塞/监控三种时机与 LLM 调用并行执行。README 顶部声明功能已与 Pydantic 团队合作上游化为 pydantic-ai-harness 的 guardrails 模块，新项目建议改用 harness，本库仍在 PyPI 维持可用。pip 安装，MIT 许可。

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

- CostTracking 按 USD 预算封顶并在超限时报错
- PromptInjection 6 类检测、3 档灵敏度，支持自定义正则
- ToolGuard 支持封禁与执行前审批回调
- AsyncGuardrail 三种时机（concurrent/blocking/monitoring），守卫先失败则取消 LLM 调用

## 适用场景

- 给生产环境 agent 加成本预算与工具权限控制
- 拦截提示注入、PII 与密钥泄漏等风险内容
- 在 LLM 调用前校验输入、调用后校验输出

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6:  Cost & budget caps, input / output / tool blocking, PII & secret redaction — for any Pydantic AI agent.
> L69: **Pydantic AI Shields** are ready-to-use guardrail capabilities for Pydantic AI agents. Drop them into any agent fo

## 星数曲线

```mermaid
xychart-beta
    title "vstorm-co/pydantic-ai-shields 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 93 --> 96
    line [95, 94, 94]
```

2026-10-18 95 → 2026-10-29 94（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ba4d75338ad1` · [字段定义](../../DATASET.md)*
