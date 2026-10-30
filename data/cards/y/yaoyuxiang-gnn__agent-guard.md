# yaoyuxiang-gnn/agent-guard

⭐ 21 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/yaoyuxiang-gnn/agent-guard) · [官网](https://pypi.org/project/agent-budget-guard-py/) · 个人维护

**给 AI agent 开发者：进程内预算上限、死循环检测与熔断库**

零依赖的 Python 库，在 agent 循环进程内提供四类上限（max_usd/max_tokens/max_steps/max_seconds）与按工具的作用域预算，配合四种默认开启的循环检测器（重复/乒乓/近似/无进展），在重复调用执行前抛出异常。适配器以鸭子类型包装 OpenAI/Anthropic/LiteLLM 等客户端与 LangChain 回调，无需导入 provider SDK。内置 119 个模型价格表（标注日期），未知模型计为 unpriced 不估算；支持 preflight 预拒付、快照恢复与 CI 报告。非代理、非可观测平台、非 tokenizer。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四类全局上限与按工具/标签的作用域预算（scoped_budgets）
- 四种循环检测器默认开启，在重复执行前触发
- 鸭子类型适配器覆盖 OpenAI/Anthropic/LiteLLM/OpenRouter/vLLM/Groq 等，不导入 SDK
- 内置 119 模型价格表，未知模型标记 unpriced 并显式报告

## 适用场景

- 防止 agent 夜间失控循环烧掉预算
- 定位哪个工具在重试风暴中吃掉预算
- 在 CI 中渲染 agent 运行的花费报告

## 场景标签

 · 领域:AI agent 基础设施/成本治理

## 证据(README 行号)

> L4: budget caps, loop detection and circuit breakers for AI agents
> L159: client = guard_openai(OpenAI(), max_usd=1.0, max_steps=25)
> L284: **Zero dependencies, and it stays that way.** No `pydantic`, no `httpx`, no provider

## 星数曲线

```mermaid
xychart-beta
    title "yaoyuxiang-gnn/agent-guard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a71f123c4b9a` · [字段定义](../../DATASET.md)*
