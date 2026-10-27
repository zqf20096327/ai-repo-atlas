# Minnzen/claude-code-kit

⭐ 30 · TypeScript · MIT · 推送 2026-10-12 · [GitHub](https://github.com/Minnzen/claude-code-kit) · 个人维护 · 中文 README

**React 终端组件与无头 Agent 框架工具包，用于构建 CLI 与 AI 助手**

面向开发者的 TypeScript/npm 工具包，由 5 个包组成：Yoga 布局引擎、React 终端渲染器、30+ UI 组件、provider 无关的无头 Agent（含权限、会话、压缩、实验性 MCP），以及 10 个内置工具（Bash/Read/Edit/Grep 等）与 LSP/子代理等工具工厂。支持 Anthropic、OpenAI、Ollama 等提供商。五个包均发布为 0.4.0，0.x 期间部分 API 仍会变化。附 3 个维护中的示例工程。

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

- 5 个 npm 包：布局引擎、终端渲染器、30+ UI 组件、无头 Agent、10 个内置工具
- Provider 无关：Anthropic、OpenAI、Ollama、DeepSeek、Groq 或任意 OpenAI 兼容 baseURL
- MCP 客户端支持 stdio + HTTP 动态工具发现，只读工具可并行执行
- 实验性工具工厂：LSP、子代理、任务编排、Jupyter notebook 编辑

## 适用场景

- 构建终端里的 AI 编码助手或对话式 REPL
- 开发终端仪表盘、CLI 工具界面
- 接入 MCP 服务器扩展 agent 工具集

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: This toolkit combines composable React terminal components, a React terminal renderer, and a provider-agnostic head
> L27: - **Provider-agnostic** -- Anthropic, OpenAI, Ollama, DeepSeek, Groq, or any OpenAI-compatible `baseURL`
> L106: |`@claude-code-kit/agent`|Headless agent -- providers, permissions, sessions, compaction, experimental MCP|

## 星数曲线

```mermaid
xychart-beta
    title "Minnzen/claude-code-kit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-27 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3dffa882c2a6` · [字段定义](../../DATASET.md)*
