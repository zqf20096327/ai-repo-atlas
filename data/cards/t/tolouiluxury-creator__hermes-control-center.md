# tolouiluxury-creator/hermes-control-center

⭐ 13 · TypeScript · MIT · 推送 2026-09-06 · [GitHub](https://github.com/tolouiluxury-creator/hermes-control-center) · [官网](https://hermes-cc.toloui.de/) · 个人维护

**Hermes Agent 的仪表盘式 Web 管控中心：挂件+聊天+管理页**

面向已部署 Hermes Agent 的用户，提供以仪表盘为核心的 Web 控制台：12 个可拖拽的挂件（系统负载、运行状态、模型与 MCP 清单、token/成本分析、定时任务、日志等），聊天通过 Hermes dashboard 的 WebSocket 直接进行，无需 API 服务器或重启网关；另含技能/MCP/模型管理页、可运行的 prompt 工作流链、prompt 库、命令面板与三语界面（英/德/波斯语，波斯语整站 RTL）。要求 Node.js ≥22.5（用 node:sqlite，免编译）和一个 Hermes Agent 安装；尚未发布到 npm，安装需从源码 clone。安全上默认只监听 localhost，设密码后才能对外，密钥不出服务端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 个可拖拽/缩放的仪表盘挂件，布局可保存
- 聊天复用 Hermes dashboard 的 WebSocket，无需 API 服务器或网关重启
- 可运行的工作流链（prompt+定时任务），失败可继续/停止并可经 Telegram 通知
- 默认绑定 localhost，设密码（scrypt 哈希、HMAC 会话）后才允许对外监听

## 适用场景

- 在一个界面总览自托管 Hermes Agent 的健康、成本与任务
- 对运行中的 agent 发起带 token 统计与真取消的对话
- 管理技能、MCP 服务器、模型认证与定时任务

## 场景标签

`工作流自动化` `LLM 可观测性` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L10: Most Hermes web UIs are chat clients with management bolted on. This one is the other way round: a
> L46: - **Chat with your agent**, over the dashboard your Hermes is already running. No API server, no
> L84: |Dashboard backend|`hermes dashboard --no-open`|`127.0.0.1:9119`|config, skills, MCP, models, cron, logs, metrics, 

## 星数曲线

```mermaid
xychart-beta
    title "tolouiluxury-creator/hermes-control-center 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3a4b72baee18` · [字段定义](../../DATASET.md)*
