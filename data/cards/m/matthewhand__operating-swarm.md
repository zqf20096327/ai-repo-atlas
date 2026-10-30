# matthewhand/operating-swarm

⭐ 20 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/matthewhand/operating-swarm) · 个人维护

**提供商无关的 agent 运行层与工作流 harness，供开发者运行多 agent 工作流**

由个人维护的实验性 alpha 项目，源于 OpenAI 实验性 Swarm 的衍生品 Open Swarm，现使用 OpenAI Agents SDK 实现 agent、工具与交接。以 Django 提供配置、认证与对话持久化，通过 CLI、OpenAI 风格 HTTP 端点和 React WebUI 三种界面运行 Python agent 工作流（Blueprint）；支持接入本地模型 API、外部 agent CLI 与远端 harness（AnythingLLM、Flowise 等），并提供 MCP 客户端/服务端模式。README 明确声明多数集成与安装器未经完整验证，os-core 包尚未发布到 PyPI，需从源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一抽象层：原生执行、外部 harness 与对等 OS 实例
- 提供 CLI、OpenAI 兼容 HTTP 端点（含 SSE 流式）与 React WebUI 三种使用方式
- 使用 OpenAI Agents SDK 实现 agent、工具与交接
- MCP 客户端/服务端模式与多种远端集成适配器

## 适用场景

- 在统一服务中运行 Python agent 工作流并通过 API/CLI/WebUI 使用
- 通过 OpenAI 兼容端点将 agent 工作流暴露给现有客户端
- 连接 Ollama 等本地模型服务与外部 agent harness

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Operating Swarm runs Python agent workflows and connects model APIs, local agent CLIs and external harnesses through
> L11: The Python import is `swarm`. Django provides configuration, authentication and persisted conversations. Blueprint 
> L7: Operating Swarm began as **Open Swarm**, a derivative of OpenAI's experimental Swarm. It now uses the OpenAI Agents 

## 星数曲线

```mermaid
xychart-beta
    title "matthewhand/operating-swarm 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9a5e37128c92` · [字段定义](../../DATASET.md)*
