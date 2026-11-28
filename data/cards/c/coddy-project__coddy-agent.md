# coddy-project/coddy-agent

⭐ 214 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/coddy-project/coddy-agent) · [官网](https://coddy.dev) · 组织维护

**单静态 Go 二进制的通用 agent，可从多界面接入**

Coddy agent 是一个打包为静态 Go 二进制的通用 agent（harness），同一会话核心可通过桌面应用、终端 TUI、编辑器 ACP 协议、内嵌 Web UI 的 OpenAI 兼容 API、Telegram 网关、cron 调度器、swarm 中继与远程模式访问。机制上提供 ReAct 循环、文件系统与 shell 工具、MCP、规则、技能、子 agent、hooks、后台任务、长期记忆与上下文压缩；可在 scratch/distroless 镜像与只读根文件系统运行，无需额外运行时。安装覆盖脚本、系统包、Homebrew、Docker 与源码构建。

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

- 同一 agent 核心覆盖桌面、TUI、编辑器（ACP）、HTTP API、Telegram、cron、swarm 多种界面，会话共享于 ~/.coddy
- 静态 Go 二进制，可在 distroless 镜像与只读根文件系统运行，无需运行时
- 支持 skills（内置 6 个 SKILL.md 斜杠命令）、subagents、hooks、MCP（stdio/HTTP/SSE）与会话目标验证
- 接入 OpenAI、Anthropic、Ollama、llama.cpp、vLLM 等任何 OpenAI 兼容 API

## 适用场景

- 在终端、浏览器、编辑器与 Telegram 中延续同一个 agent 会话
- 以容器舰队方式批量运行 agent 节点并通过 swarm 中继管理
- 用 cron 定时任务与后台任务驱动自动化 agent 运行
- 接入本地 Ollama/llama.cpp/vLLM 作为模型后端

## 场景标签

`编码 Agent` `多智能体` `Agent 框架` · 领域:Agent 开发

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e656fd952a52` · [字段定义](../../DATASET.md)*
