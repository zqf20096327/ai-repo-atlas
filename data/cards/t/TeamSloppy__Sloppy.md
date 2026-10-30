# TeamSloppy/Sloppy

⭐ 27 · Swift · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/TeamSloppy/Sloppy) · [官网](https://sloppy.team) · 组织维护

**Swift 编写的多 agent 运行时与可视化控制平面**

用 Swift 6 实现的多 agent 运行时，运行于 macOS/Linux/Windows：提供 HTTP API、规则驱动的路由编排、Channel/Branch/Worker 执行模型、SQLite 持久化、模型/工具/网关插件体系、终端 UI 与 React Dashboard，并内置 Telegram/Discord 网关，支持 MCP 与 ACP 外部 agent。面向需要编排多个 AI agent、要求执行过程可审计可干预的个人与团队；无需 API key 即可本地运行核心。核心采用 AGPL-3.0，另提供商业版 Sloppy Enterprise。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 规则驱动的确定性路由与 Channel/Branch/Worker 运行时结构
- 模型/工具/内存/网关插件体系，AnyLanguageModel 桥接 OpenAI 与 Ollama
- SQLite 持久化、事件与 artifact 追踪、Visor 定期记忆摘要
- 终端 UI + React Dashboard + Telegram/Discord 网关，支持 MCP/ACP

## 适用场景

- 在一个界面里编排与审计多个自主运行的 AI agent
- 通过 Telegram/Discord 或手机与 agent 对话并下发任务
- 本地优先运行 agent 工作流，无需先搭建分布式系统

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: Sloppy is a multi-agent runtime for building operator-visible AI workflows in Swift 6 on macOS, Linux, and Windows.
> L58: Sloppy is a control plane for AI agents and tool-driven workflows.
> L64: |`sloppy`|🖥️ HTTP API, routing layer, orchestration services, persistence, scheduling, and plugin bootstrap|

## 星数曲线

```mermaid
xychart-beta
    title "TeamSloppy/Sloppy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `094a07ab6543` · [字段定义](../../DATASET.md)*
