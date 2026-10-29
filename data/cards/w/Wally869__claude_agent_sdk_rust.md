# Wally869/claude_agent_sdk_rust

⭐ 26 · Rust · 推送 2026-03-03 · [GitHub](https://github.com/Wally869/claude_agent_sdk_rust) · [官网](https://crates.io/crates/claude-agent-sdk-rust) · 个人维护

**Rust 版 Claude Agent SDK：封装 Claude Code CLI 构建类型安全 AI agent**

面向 Rust 开发者的 SDK，复刻 Python Claude Agent SDK 功能集，通过封装 Claude Code CLI 提供类型安全访问：20+ 内置工具控制、自定义 MCP 服务器配置、细粒度权限模式与权限回调、Hook 系统、结构化 JSON 输出、预算上限、会话恢复/分支、用量跟踪（Max Plan）。要求 Rust 1.85+、Claude Code CLI 2.0.0+，认证需 Claude 订阅或 Anthropic API key。以 crates.io 包分发，附 docs.rs 文档与 7 个示例。限制：结构化输出需多轮、预算为软上限、CLI 禁止嵌套实例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 Claude Code CLI 的类型安全异步 Rust 接口
- 权限模式/权限回调与 Hook 系统控制工具行为
- 结构化 JSON 输出（需 max_turns≥2-3）与预算软上限
- 会话管理：捕获 ID、恢复、继续、分支（fork）

## 适用场景

- 用 Rust 构建 Claude 驱动的 agent 并控制工具权限
- 在 Rust 服务中集成 MCP 服务器与自定义工具
- 实现多轮交互会话的恢复与分支实验

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: Rust SDK for building production-ready AI agents with Claude. Replicate the full feature set of the Python Claude Ag
> L10: The Claude Agent SDK enables you to build powerful AI agents using Claude Code's agent harness. This SDK wraps the 

## 星数曲线

```mermaid
xychart-beta
    title "Wally869/claude_agent_sdk_rust 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-29"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-19 26 → 2026-10-29 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `9946c6203b3e` · [字段定义](../../DATASET.md)*
