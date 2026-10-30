# dvf/synapse

⭐ 19 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/dvf/synapse) · 个人维护

**轻量级 P2P agent 基础设施层：节点发现、RPC 与共享对话**

Python 库，定位为 agent 框架之下的底层网络层：为每个进程提供 Node，赋予名称、mDNS 种子发现、能力声明、RPC 端点、广播、共享对话事件日志、心跳与定时任务（cron/间隔/日出太阳位置）。附带 Team 层实现任务认领、租约重派与 at-least-once 交付，支持 SQLite 对话日志、事件折叠摘要与保留期修剪。面向搭建多 agent 协作群体的开发者；明确不含规划、记忆、共识、认证与 NAT 穿透，示例可离线运行无需 API key。

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

- swarm 共享名 + mDNS 自动发现，无需服务器
- 共享对话事件日志与可自定义摘要器（可交给 LLM）
- Team 层：能力匹配认领、租约重派、at-least-once 交付
- 定时唤醒支持 interval/cron/太阳事件（sunrise 等）

## 适用场景

- 让多个 agent 进程在局域网内互相发现并协作处理任务
- 搭建带任务重试与故障恢复的编码/交易团队示例
- 让长期运行的节点按 cron 或日出时间自动唤醒执行任务

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L13: Synapse is not an agent framework. It's the layer underneath: give each process a `Node` and it gets a name, peers,
> L3: **Build agent swarms that discover each other, share abilities, join conversations, and wake up on schedules like su

## 星数曲线

```mermaid
xychart-beta
    title "dvf/synapse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-30 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `aae5a7a0886b` · [字段定义](../../DATASET.md)*
