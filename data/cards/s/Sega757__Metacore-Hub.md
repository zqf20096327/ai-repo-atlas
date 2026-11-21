# Sega757/Metacore-Hub

⭐ 4 · Python · MIT · 推送 2026-11-10 · [GitHub](https://github.com/Sega757/Metacore-Hub) · 个人维护

**为 LLM 工程代理提供守护进程托管的状态机与合并门控**

MetaCore Hub 位于非确定性的 AI 生成（云端编码 worker、LLM 审阅者）与确定性系统提交（代码合并）之间：LLM 只能提出建议，由一个做 schema 校验的 CoreEngine 守护进程独占任务状态与合并决策。机制包括 FSM 状态机、JSON Schema（Draft 2020-12）事件契约与死信队列、Watchdog 停滞检测与熔断、SHA-256 哈希链防篡改审计日志、A2A 卡片加固（SSRF 白名单、扩展确认）。合并需同时满足置信度阈值、HITL 关闭与引擎侧证据门。Python 3.10+ 运行，从源码安装，Gemini 支持为可选扩展。

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

- 守护进程独占任务状态转换与合并决策，LLM 仅提出建议
- JSON Schema 事件校验，无效事件进入死信队列不触及状态
- 哈希链防篡改审计日志与 Watchdog 熔断器
- Gemini 仲裁器带安全回退：模型输出异常时降级为确定性规则

## 适用场景

- 让 LLM 编码代理自动提交代码变更但由引擎把关合并
- 多代理流程中防止幻觉式批准与失控循环
- 需要人工确认（HITL）的代理合并审批流程
- 对代理事件流做防篡改审计与问责

## 场景标签

`多智能体` `Agent 框架` `代码审查` · 领域:Agent 开发

## 证据(README 行号)

> L7: MetaCore Hub sits between non-deterministic AI generation (cloud coding workers, LLM reviewers) and deterministic
> L18: |Task state, transitions, merge decisions|`CoreEngine` daemon — **sole owner**|
> L93: |`metacore.arbiter`|`RuleBasedArbiter` (offline, deterministic), `GeminiArbiter` (LLM with safe fallback)|

## 星数曲线

```mermaid
xychart-beta
    title "Sega757/Metacore-Hub 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-11-10", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-19 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `6eecd7732b51` · [字段定义](../../DATASET.md)*
