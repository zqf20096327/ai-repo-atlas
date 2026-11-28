# coddy-project/coddy-agent

⭐ 214 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/coddy-project/coddy-agent) · [官网](https://coddy.dev) · 组织维护

**单静态 Go 二进制的通用 AI Agent：多入口同会话**

一个通用 AI Agent，以静态 Go 二进制分发，同一 Agent 核心通过多种入口访问：桌面应用、终端 TUI、面向编辑器的 ACP 服务、内置 Web UI 的 OpenAI 兼容 HTTP API、Telegram/Pachca 网关、cron 调度器、Swarm 中继与远程模式，全部共享 ~/.coddy 下的同一批会话。机制含 ReAct 循环、文件系统与 shell 工具、MCP、rules/skills/subagents/hooks、后台任务、长期记忆、上下文压缩与项目信任门控；运行于 scratch/distroless 容器，无需额外运行时。模型通过配置文件中的 provider 或 OPENAI_API_KEY 提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单静态二进制提供桌面/TUI/ACP/HTTP API/Telegram/调度器/Swarm 等多种入口，共享会话
- 支持 MCP 服务器（stdio/HTTP/SSE）、规则、技能、子代理与生命周期 hooks
- 会话目标模式由第二模型判定工具结果、只读校验器确认，附看门狗防卡死
- 上下文压缩、后台记忆子代理、自配置 YAML 与跨入口会话续接

## 适用场景

- 在终端、编辑器（Zed/VS Code）、浏览器与 Telegram 中续接同一个 Agent 会话
- 以 cron 定时任务形式运行独立会话的自动化 Agent 作业
- 以 docker compose 在容器集群中批量部署 Agent 节点并用 Swarm 中继统一调度
- 通过技能与 hooks 定制代码审查、功能开发等 Agent 工作流

## 场景标签

`编码 Agent` `Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9:  A general-purpose agent in one static Go binary.
> L19: Coddy is a **harness**: the same agent core is reachable from the desktop app with `coddy desktop`, from a terminal
> L89: - **Any model**: OpenAI, Anthropic, NeuralDeep, ChatGPT through Codex, the models of a Devin account (Devin), a loc

## 星数曲线

```mermaid
xychart-beta
    title "coddy-project/coddy-agent 星数(近 15 点)"
    x-axis ["2026-10-26", "2026-10-29", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-15", "2026-11-16", "2026-11-21", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 180 --> 217
    line [187, 186, 189, 194, 183, 200, 203, 204, 205, 206, 208, 209, 213, 214, 214]
```

2026-10-26 187 → 2026-11-28 214（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `5612881f86bc` · [字段定义](../../DATASET.md)*
