# deepansh-saxena/DuraLang

⭐ 30 · Python · MIT · 推送 2026-04-01 · [GitHub](https://github.com/deepansh-saxena/DuraLang) · [官网](https://pypi.org/project/duralang/) · 个人维护

**给 LangChain agent 加持久化执行层的装饰器库**

面向使用 LangChain 构建 AI agent 的开发者的 Python 库：在现有代码上加 @dura 装饰器，将每个 LLM 调用、工具调用、MCP 调用与 agent 间调用转为 Temporal Activity，获得自动重试、超时、心跳与事件历史记录；失败时仅重试失败操作，进程崩溃后可从断点恢复。@dura 嵌套成为 Child Workflow，支持任意深度的多 agent 编排。要求运行中的 Temporal 服务器，兼容 Anthropic/OpenAI/Google/Ollama 等任何 LangChain BaseChatModel，执行过程可在 Temporal UI 中查看。

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

- @dura 装饰器将 LLM/工具/MCP 调用转为可重试的 Temporal Activity
- 进程崩溃（OOM/硬件故障/部署）后从断点恢复，已完成步骤不重跑
- @dura 嵌套自动成为 Child Workflow，支持多 agent 编排与并行工具执行
- 兼容任意 LangChain BaseChatModel（Anthropic/OpenAI/Google/Ollama）

## 适用场景

- 长时间运行的 AI agent 任务在调用失败后自动重试并保留进度
- 多 agent 流水线中子 agent 崩溃时只重试该子 agent
- 在 Temporal UI 免费查看每次 LLM/工具调用的输入输出与重试历史

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: <code>duralang</code> is the missing durability layer for LangChain.
> L6: Write the same LangChain code you already know — add <code>@dura</code> — and every LLM call, tool call, MCP call, a
> L219: **duralang vs Temporal directly** — duralang is built on Temporal, but eliminates the boilerplate: no manual workf

## 星数曲线

```mermaid
xychart-beta
    title "deepansh-saxena/DuraLang 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-27 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8b2c125d2647` · [字段定义](../../DATASET.md)*
