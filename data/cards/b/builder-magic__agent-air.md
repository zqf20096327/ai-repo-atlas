# builder-magic/agent-air

⭐ 14 · Rust · MIT · 推送 2026-05-30 · [GitHub](https://github.com/builder-magic/agent-air) · [官网](https://agent-core.ai) · 个人维护

**用 Rust 构建 TUI/服务端 AI Agent 的 SDK 与运行时**

开源 SDK 与运行时，用于构建在终端 UI 或服务器上运行的 AI Agent。框架负责 LLM 通信、多会话管理、markdown 渲染、小组件与布局、工具、技能、MCP 协议与权限系统，开发者在其上编写 agent 逻辑。支持 75+ 提供商、500+ 模型运行时切换，具备会话隔离、上下文压缩策略、流式解析与自定义工具等机制。以 Rust crate 形式通过 Cargo.toml 引入使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 LLM 通信、会话、工具、MCP、权限的 Agent 开发运行时
- 75+ providers / 500+ 模型，支持运行时切换
- 预置 StatusBar、ChatView 等 TUI 小组件与斜杠命令框架
- 隔离并发会话，各自独立历史与工具注册

## 适用场景

- 在终端里快速搭建一个可交互的 AI agent
- 构建多会话并发的服务端 agent 应用
- 通过 MCP 接入外部工具并自建技能系统

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: agent-air is an open-source SDK and Runtime for building AI agents running in a Terminal UI or on the server. agent
> L36: - **High Performance Rust Core** - Async-first architecture powered by Tokio with zero-cost abstractions

## 星数曲线

```mermaid
xychart-beta
    title "builder-magic/agent-air 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `75e69c34ccab` · [字段定义](../../DATASET.md)*
