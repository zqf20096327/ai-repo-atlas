# iii-experimental/agentos

⭐ 162 · Rust · Apache-2.0 · 推送 2026-05-07 · [GitHub](https://github.com/iii-experimental/agentos) · [官网](https://agentsos.sh) · 组织维护

**基于 iii 引擎的多 worker 自进化 agent 运行时（Rust）**

AgentOS 是运行在 iii 引擎之上的 agent 系统：65 个窄域 worker（64 个 Rust + 1 个 Python）通过 WebSocket 连接引擎，以 Worker/Function/Trigger 三个原语注册能力，引擎负责路由、重试、状态与追踪。Worker 覆盖推理、状态、协调、执行、安全、渠道（Slack/Discord/Telegram 等 14 个）、遥测与沙箱（microVM 与 wasmtime）。提供 TUI 终端界面与 HTTP API，版本 0.0.1（pre-1.0）。安装需先安装 iii 引擎二进制，再用 cargo 构建各 worker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 65 个窄域 worker 以 Worker/Function/Trigger 三原语注册能力
- TUI 终端界面支持斜杠命令、命令面板与 worker 浏览安装
- 内置 OCI microVM 与 fuel 计量 wasm 两类沙箱命名空间
- CI 校验 worker 清单合规与沙箱边界

## 适用场景

- 搭建可经 HTTP/cron/pub/sub 触发的多 worker agent 系统
- 在终端 TUI 中与 agent 对话并管理 worker 与记忆
- 接入 Slack、Discord、Telegram 等聊天渠道

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L16: AgentOS isn't another agent framework. It's *what's left* when the runtime becomes someone else's problem.
> L18: 65 narrow workers — one Rust binary per domain — register Functions and Triggers on the iii engine. Every capabilit
> L86: |Surfaces|`a2a` `a2a-cards` `mcp-client` `skillkit-bridge` `bridge` `streaming`|

## 星数曲线

```mermaid
xychart-beta
    title "iii-experimental/agentos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 161 --> 163
    line [162, 162]
```

2026-10-18 162 → 2026-10-25 162（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `17d10bfd7347` · [字段定义](../../DATASET.md)*
