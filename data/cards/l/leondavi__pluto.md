# leondavi/pluto

⭐ 18 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/leondavi/pluto) · 个人维护

**多 AI agent 协调与消息服务器：锁、注册表、死锁检测**

基于 Erlang/OTP 构建的协调服务器，为多个异构 AI agent 提供共享运行时：分布式读写锁（FIFO 公平）、心跳监测与静默自动释放锁、单调递增 fencing token、死锁检测（含牺牲者选择）、agent 注册表与发现、语言无关的 TCP+HTTP 消息总线。不做任务规划，定位为编排框架（LangGraph、CrewAI、AutoGen 等）的补充而非替代。通过安装脚本（依赖 Erlang/OTP、rebar3、Python 3.10+）部署，提供 MCP 工具封装（面向 Claude Code）、PTY 注入封装（面向 Cursor/Aider）、Python 客户端与检查 CLI，附 5 个端到端示例。

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

- 分布式读写锁 + 心跳监测 + 静默自动释放
- 单调递增 fencing token 防止锁撤销后的过期写入
- 死锁检测与牺牲者选择
- 语言无关的 TCP+HTTP 消息总线与 agent 注册表/发现

## 适用场景

- 多个 agent 并发操作共享资源时防止写冲突
- 团队里协调 orchestrator/specialist/reviewer 等角色通信
- 通过 MCP 工具让 Claude Code 等 CLI agent 接入协调运行时

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L18: Pluto is an Erlang/OTP server that gives multiple AI agents a shared
> L20: do that. Pluto provides the coordination primitives an agent team
> L40: Pluto **complements** orchestration frameworks; it doesn't replace them.

## 星数曲线

```mermaid
xychart-beta
    title "leondavi/pluto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2164139ade87` · [字段定义](../../DATASET.md)*
