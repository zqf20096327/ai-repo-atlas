# Suraj1235/open-dynamic-workflows

⭐ 50 · JavaScript · MIT · 推送 2026-07-09 · [GitHub](https://github.com/Suraj1235/open-dynamic-workflows) · [官网](https://github.com/Suraj1235/open-dynamic-workflows#readme) · 个人维护

**本地多智能体工作流编排引擎，脚本而非模型做协调者**

面向 AI 编程 agent 用户的开源编排引擎：模型一次性编写 JavaScript execute() 计划，本地守护进程在 QuickJS WASM 沙箱中执行 agent/parallel/verify/loop 等原语，将每次 agent() 调度为对模型提供商的 HTTP 请求，聊天窗口只收到最终结果。支持 Anthropic/OpenAI/Ollama 及任意 OpenAI 兼容端点，提供六种编排拓扑与对抗式验证。状态存于 SQLite，支持 --resume 断点续跑。通过 MCP 与各编辑器/agent 适配器接入，需 git clone 安装（未上 npm）。

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

- 模型写一次计划，本地 daemon 执行 swarm，避免上下文窗口被协调占用
- QuickJS WASM 沙箱内暴露 agent/parallel/verify/loop/checkpoint 原语
- SQLite + WAL 状态存储，支持 --resume 精确重放与失败 agent 降级
- odw-daemon integrate 一键接入 MCP、Codex、Cursor、Kimi、Gemini 等宿主

## 适用场景

- 让编程 agent 执行跨大量文件/端点的并行审计或迁移工作流
- 在没有云 API key 时用本地 Ollama 模型跑工作流
- 通过对抗式 critic 面板降低多 agent 结论的误报

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: An open-source engine for dynamic, multi-agent workflows where a *script* is the orchestrator, not the model — the p
> L37: The model never babysits the swarm. It writes one `execute(context)` function and hands it to the daemon, which run

## 星数曲线

```mermaid
xychart-beta
    title "Suraj1235/open-dynamic-workflows 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-26 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ea663dc3bbc6` · [字段定义](../../DATASET.md)*
