# synadia-ai/synadia-agents

⭐ 86 · TypeScript · Apache-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/synadia-ai/synadia-agents) · 组织维护

**将 AI agent 接入 NATS 的协议 SDK 与预构建通道插件集**

面向构建多 agent 系统的开发者：提供 Synadia Agent Protocol 的官方 caller/host SDK（TypeScript 与 Python），使任意 AI agent（Claude Code、Codex、OpenCode、PI、Hermes 等）可注册为 NATS 微服务，被同样线格式的调用方发现、提示并流式接收回复。仓库另含多个预构建通道插件，无需写代码即可把现有 AI harness 挂上 NATS，以及浏览器 UI、headless 会话控制器等端到端示例。当前版本不含 tracing，通过通用扩展钩子在独立包中实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TypeScript/Python 双语言 caller 与 host SDK，线格式经跨 SDK 互操作测试
- 12+ 个预构建通道插件覆盖 Claude Code、Codex、Grok、DSPy 等现有 agent
- 基于 NATS 微服务的发现、prompt、状态与心跳端点，流式 JSON chunk 响应
- 从零构建的 DSPy ReAct 与 deep-research agent 示例

## 适用场景

- 把已有编码 agent 挂到 NATS 上供其他系统发现和调用
- 构建跨多 agent 的调用方客户端与会话控制器
- 用统一协议对接多种 AI harness 构建多 agent 系统

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: **SDKs and ready-to-run agent plugins for the Synadia Agent Protocol for NATS.**
> L5: The Synadia Agent Protocol for NATS lets any AI agent — Codex, OpenCode, Claude Code, OpenClaw, PI, Hermes, Flue, or
> L42: Two halves per language. The **caller** SDK (`client-sdk/`) discovers and prompts agents; the **host** SDK (`agent-

## 星数曲线

```mermaid
xychart-beta
    title "synadia-ai/synadia-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 85 --> 87
    line [86, 86]
```

2026-10-18 86 → 2026-10-26 86（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `03882640c950` · [字段定义](../../DATASET.md)*
