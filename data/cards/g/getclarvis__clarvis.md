# getclarvis/clarvis

⭐ 14 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/getclarvis/clarvis) · [官网](https://clarvis.dev) · 组织维护

**本地优先的终端编码 Agent，整合模型、工具、计划与记忆**

面向开发者的 local-first 终端编码 Agent（TUI/CLI）：在一个界面中集成会话、计划、Markdown 记忆、任务与多 Agent 工作流（内置 Lead/Sub-agent 及 audit/implement/research 打包工作流）。模型接入支持配置 API 提供商、OpenAI 兼容本地端点及 beta 版 ChatGPT/Grok 订阅流程。安全机制包括路径级工作区限制、命令审批、可选原生沙箱与工作区信任。pre-1.0 beta 状态，接口与状态格式可能变化；提供跨平台安装脚本，安装包含内置 Bun 运行时，无需预装 Node 或编译器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 Agent 工作流：内置 Lead、Sub-agent 与 audit/implement/research 打包工作流
- BYO 模型：API 提供商、OpenAI 兼容本地端点、beta 订阅流程
- 路径级工作区限制、命令审批、Linux/macOS 可选原生沙箱
- 可扩展：MCP 服务器、插件、hooks、Agent Skills、自定义 agent

## 适用场景

- 在终端中用 AI Agent 读写代码库并执行命令
- 以多 Agent 工作流拆分审计、实现与调研任务
- 接入本地 OpenAI 兼容端点在自有模型上编码

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: Clarvis is a local-first coding agent that brings models, tools, plans, memory, and multi-agent
> L24: - **Agent workflows:** use a built-in Lead, delegate to focused Sub-agents, or run the packaged

## 星数曲线

```mermaid
xychart-beta
    title "getclarvis/clarvis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0f6198fc85e7` · [字段定义](../../DATASET.md)*
