# arieradle/shekel

⭐ 19 · Python · MIT · 推送 2026-06-17 · [GitHub](https://github.com/arieradle/shekel) · [官网](https://pypi.org/project/shekel/) · 个人维护

**给 AI agent 开发者的 LLM 花费预算控制与成本治理 Python 库**

面向构建 agent 系统的开发者，通过 monkey-patch OpenAI/Anthropic 等提供商的 SDK 调用来追踪与限制 LLM 支出，无需修改业务代码。提供硬性 USD 上限、按节点/链/agent/任务/工具的组件级限额、循环与速率防护、滚动窗口限流、便宜模型回退，以及 Redis 后端的多进程与多租户预算。另有 CLI（shekel run）在零代码改动下执行预算，内置 GPT-4o、Claude、Gemini 等模型定价，支持 Langfuse 与 OpenTelemetry 可观测输出。仅追踪本机调用，不依赖外部服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- monkey-patch 提供商 SDK 实现零集成代码的预算强制
- LangGraph 节点 / LangChain 链 / CrewAI agent 与任务的组件级限额
- loop_guard、max_velocity 等循环与烧钱速率防护
- shekel run CLI 零代码执行预算，exit code 对 CI 友好

## 适用场景

- 给夜间运行的 agent 设硬性花费上限，防止重试循环烧钱
- 在多 agent 流水线中按阶段分配预算并查看花费树
- 多进程/多租户场景用 Redis 做配额与限流管理

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L16:     run_my_agent()       # hard stop at $5. no SDK changes. no config. just works.
> L63: No wrapping your OpenAI client. No decorators. No SDK replacement. shekel monkey-patches the provider on context en

## 星数曲线

```mermaid
xychart-beta
    title "arieradle/shekel 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `118e13c907f3` · [字段定义](../../DATASET.md)*
