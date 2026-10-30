# zeynepyorulmaz/openclaw-orchestrator

⭐ 34 · TypeScript · NOASSERTION · 推送 2026-03-18 · [GitHub](https://github.com/zeynepyorulmaz/openclaw-orchestrator) · [官网](https://zeynepyorulmaz.github.io/openclaw-orchestrator/) · 个人维护

**面向 OpenClaw 网关的自适应多 agent 编排框架**

TypeScript 编写、Zod 校验、SQLite 存储的多 agent 编排框架：LLM 规划器将复杂目标拆解为可并行任务，按名称或能力路由给 OpenClaw 网关上的专门化 agent（如 researcher/coder/analyst），每个 agent 沙箱隔离、仅持有指定工具，形成最小权限结构。循环执行 think→execute→repeat 直到 LLM 判定完成或达到步数上限。附带零前端依赖的单文件 Web 仪表盘（SSE 实时流、步骤可视化、运行历史），提供 serve/run/plan/agents 等 CLI 命令与程序化 API。需 Node.js 22+ 与至少配置一个 agent 的 OpenClaw 网关。许可证为专有（Proprietary）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 规划器将目标拆解为并行任务并自适应迭代
- 三种 agent 适配器：OpenClaw 网关 / HTTP 端点 / 进程内函数
- 单 HTML 文件 Web 仪表盘，SSE 实时流与运行历史
- agent 按 SOUL.md/TOOLS.md 配置实现沙箱化最小权限

## 适用场景

- 把研究、编码、分析类目标分派给专门化 agent 并行执行
- 通过 Web 界面实时观察和检查多 agent 运行过程
- 在 OpenClaw 网关之上做任务编排与路由

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Adaptive multi-agent orchestration for OpenClaw gateways.
> L7: Break down complex goals into tasks, route them to specialized agents, and iterate until done — all driven by an LLM
> L120: 1. **Think** — The orchestrator sends the goal and all accumulated results to an LLM, which responds with either:

## 星数曲线

```mermaid
xychart-beta
    title "zeynepyorulmaz/openclaw-orchestrator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `aeedeab4daf3` · [字段定义](../../DATASET.md)*
