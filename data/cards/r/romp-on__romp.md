# romp-on/romp

⭐ 23 · Python · Apache-2.0 · 推送 2026-09-24 · [GitHub](https://github.com/romp-on/romp) · [官网](https://romp-on.github.io/romp/) · 组织维护

**并行 Claude Code 会话的追踪与协调管理工具**

面向运行多个 Claude Code 会话的开发者的自托管管理面板：以时间线视图展示所有会话状态，读取 agent 的对话转录并聚合成任务卡片（工作目的、已做内容、子任务），通过 Romp Postal Service 让不同会话的 agent 互相提问与交接工作，支持跨机器聚合（SSH/Tailscale），可从手机、浏览器或 VS Code / Cursor 扩展访问。需要 Claude Code（已登录）、Python 3.10+ 与 Node.js，通过 bootstrap 脚本安装，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 时间线视图追踪所有会话的运行/空闲/待处理状态
- 读取 agent 转录生成任务卡片，含工作动机与子任务
- Romp Postal Service 支持 agent 间消息与工作交接
- 自托管，跨机器聚合，手机/浏览器/编辑器扩展均可访问

## 适用场景

- 同时跑多个 Claude Code 会话时集中查看状态与待办
- 让不同机器上的 agent 互相交接工作
- 从手机远程查看和操控服务器上的 agent 会话

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: AI agents like Claude Code can work autonomously for long stretches, allowing several to be run in parallel. But thi
> L41: Romp works with Claude Code today. It adds all of this on top of the sessions you already run, without changing how
> L45: You run Romp yourself, on your laptop or a server, with no hosted service in between.

## 星数曲线

```mermaid
xychart-beta
    title "romp-on/romp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-28 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `6bc3ad301599` · [字段定义](../../DATASET.md)*
