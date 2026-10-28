# dbisina/relay

⭐ 31 · Go · Apache-2.0 · 推送 2026-08-23 · [GitHub](https://github.com/dbisina/relay) · 个人维护

**多 AI 编程 agent 间的任务轮换与交接编排器**

面向使用多个 AI 编程订阅的开发者：Relay 检测本机正在运行的 Claude Code / Codex / Copilot / Cursor / Cline 等会话，在代理撞上配额墙前于安全点暂停，将意图、计划、进行中代码序列化为 HMAC 签名的 continuation contract，并交接到另一个代理、账号或供应商继续执行。提供桌面应用（Electron）与 CLI/TUI 两种形态，支持配额面板、预测性交接、多代理 DAG 流水线与 MCP server。安装包未做代码签名，需 git 与至少一个 AI agent CLI 作为前置条件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- HMAC 签名的 continuation contract 跨代理/供应商携带意图、计划与在途代码
- 检测并接管本机已运行的 AI agent 会话（Claude Code、Codex、Copilot、Cursor 等）
- 账号自动故障转移与配额钱包（剩余额度、重置时间、燃尽 ETA）
- 以 MCP server 形式将全部 API 暴露给任意 MCP 客户端

## 适用场景

- 某个 AI 编程订阅配额耗尽时把任务无缝转移到另一个账号或供应商
- 同时持有多个 AI 订阅，按剩余配额路由下一个任务
- 用 MCP 客户端驱动 Relay 做跨代理的任务交接

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: Relay detects the Claude Code / Codex / Copilot / Cursor / Cline / Antigravity sessions **already running on your m
> L103: Relay treats the handoff as a first-class, signed protocol. When an agent hits a

## 星数曲线

```mermaid
xychart-beta
    title "dbisina/relay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ee28bbec0c99` · [字段定义](../../DATASET.md)*
