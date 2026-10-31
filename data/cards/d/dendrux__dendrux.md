# dendrux/dendrux

⭐ 14 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/dendrux/dendrux) · 组织维护

**异步 Python agent 运行时：故障恢复、证据持久化、暂停等待人工**

面向构建生产级 agent 的 Python 运行时：工具为普通 Python 函数，运行状态持久化并在进程重启后可被 sweep 清扫，失败运行可基于持久化 trace 重试；每次 LLM 调用、工具执行与暂停均落库留证。支持多 provider（Anthropic、OpenAI、OpenRouter、Groq、OpenAI 兼容端点），提供四层治理（工具 deny、人工审批、预算、PII/密钥检测）、客户端工具暂停恢复、父子 agent 委派与多租户隔离。当前 v0.5.0，API 仍在稳定化、活跃开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 失败运行基于持久化 trace 重试，上下文完整回放
- 人工审批（HITL）与客户端工具暂停/恢复，pause_id 防陈旧审批
- PII 脱敏、密钥检测、token 与美元预算四层治理
- 每次 LLM 调用与工具执行均持久化为证据

## 适用场景

- 构建需要人工审批的高风险工具型 agent（如退款、删号）
- 多租户生产环境部署可审计的 agent 服务
- agent 中途崩溃后从断点恢复或换模型重试

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  The async Python runtime for agents that survive failure, persist everything, and bridge to the real world.
> L62: Dendrux is the runtime that handles this. Tools are plain Python functions. State survives restarts. Crashed runs g
> L77: Three concepts: `Agent`, `@tool()`, provider. Everything else is opt-in.

## 星数曲线

```mermaid
xychart-beta
    title "dendrux/dendrux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `2dfe52e748a6` · [字段定义](../../DATASET.md)*
