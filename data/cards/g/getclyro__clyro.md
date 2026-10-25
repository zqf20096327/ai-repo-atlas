# getclyro/clyro

⭐ 55 · Python · Apache-2.0 · 推送 2026-08-14 · [GitHub](https://github.com/getclyro/clyro) · [官网](https://clyro.dev/) · 组织维护

**AI agent 运行时治理 SDK：拦截死循环、成本失控与策略违规**

面向 Python agent 的治理层，以 `clyro.wrap()` 包裹任意可调用对象，提供执行追踪、步数/成本上限、循环检测与策略执行（8 种操作符，含 block/allow/require_approval）。提供 5 种框架适配器（LangGraph、CrewAI、Claude Agent SDK、Anthropic SDK、通用），另有 MCP 包装器治理 Claude Desktop/Cursor/VS Code 的工具调用、Claude Code hooks 拦截危险命令、以及 `clyro suggest` 策略推荐器。支持完全离线的本地 YAML 策略模式，可选连接 Clyro Cloud；SDK 采用 fail-open 设计，出错不中断 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 步数/成本上限、循环检测与策略执行的 Prevention Stack
- 5 种框架适配器（LangGraph/CrewAI/Claude Agent SDK/Anthropic SDK/通用）
- MCP JSON-RPC 代理与 Claude Code hooks 两个治理入口
- 离线本地 YAML 策略模式，无需 API key；dry-run 模式只记录不拦截

## 适用场景

- 给生产环境的 agent 设置成本与步数护栏，防止失控
- 在 Claude Code 会话中拦截 rm -rf、DROP TABLE 等破坏性命令
- 对现有 agent 跑 clyro suggest 获得治理策略建议
- 先以 dry-run 模式验证策略再开启强制执行

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L14: |**SDK**|Wrap any Python agent with tracing, cost limits, loop detection, and policy enforcement|`clyro` / `clyro-s
> L30: - **5 framework adapters**: LangGraph, CrewAI, Claude Agent SDK, Anthropic SDK, Generic

## 星数曲线

```mermaid
xychart-beta
    title "getclyro/clyro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-25 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `fba186050b6b` · [字段定义](../../DATASET.md)*
