# ryanbbrown/thinharness

⭐ 17 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/ryanbbrown/thinharness) · 个人维护

**紧凑的 SDK-only Python agent harness 框架，供开发者构建 agent**

一个以极小框架代码量为目标的 Python agent harness：核心只保留模型-工具循环与跨运行需一致的行为，能力以显式插件提供。内置 OpenAI、Anthropic、OpenRouter 适配器，支持自定义类型化工具、Pydantic 结构化输出、断点恢复、并行工具调用、人工审批、工具重试、hooks/事件、JSONL 追踪与 OpenTelemetry span。插件含文件系统、Bash、MCP（FastMCP 客户端）、子 agent、并行 LLM 批量提示、技能运行器。需 Python 3.11+，README 给出 SLOC 对比表（10,574 行）但注明 LOC 非质量或性能分数，基准测试标注为进行中。

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

- 内置 OpenAI/Anthropic/OpenRouter 适配器，开放 provider 与 session 协议
- 显式 Python 插件体系：文件系统、Bash、MCP、子 agent、并行 LLM、技能运行器
- Pydantic 类型化工具与结构化输出，支持审批、重试与预算限制
- 自包含 transcript 可跨 provider 恢复运行

## 适用场景

- 想要少框架代码的 side project 中构建自定义 agent
- 需要审批、重试、预算与追踪的可靠 agent 运行循环
- 通过 MCP 客户端或子 agent 扩展 agent 能力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3:  A compact, SDK-only agent harness:
> L15: Larger harnesses are larger for good reasons. They support more providers, storage systems, sandboxes, durable jobs
> L57: uv add thinharness     # or pip install thinharness

## 星数曲线

```mermaid
xychart-beta
    title "ryanbbrown/thinharness 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `969b7c9e3ac0` · [字段定义](../../DATASET.md)*
