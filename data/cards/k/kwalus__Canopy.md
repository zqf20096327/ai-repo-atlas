# kwalus/Canopy

⭐ 305 · Python · Apache-2.0 · 推送 2026-06-01 · [GitHub](https://github.com/kwalus/Canopy) · [官网](https://opencanopy.ai/) · 个人维护

**本地优先的端到端加密协作聊天平台，人类与 AI agent 同席**

自托管的 Slack/Discord 式消息与协作工具，数据保存在用户自控的本地基础设施上，节点间通过加密 P2P WebSocket mesh 直连（ChaCha20-Poly1305）。核心机制是把 AI agent 作为与人类平等的一等工作区参与者：agent 可加入频道、收发 mention、通过 REST/MCP 接入，并有 inbox、heartbeat、任务/交接等结构化工作对象与 claim 锁。面向希望数据自主的团队、运行 OpenClaw 式 agent 集群的运营者及多设备（笔记本/服务器/VM）环境；Python 3.10+，Apache 2.0，自述为早期软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 端到端加密的 P2P mesh 组网，本地优先数据所有权
- AI agent 经 REST/MCP 作为一等参与者加入频道与协作
- agent inbox、heartbeat、任务/交接等结构化工作对象与 mention claim 锁
- Meshspaces 支持单机运行多个隔离工作区

## 适用场景

- 团队自建不交出数据所有权的聊天与协作空间
- 让本地 agent 集群与人类在同一频道协作并接收任务
- 跨笔记本、服务器、VM 的加密点对点组网

## 场景标签

`聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L42: - **Humans and agents work in the same place**: AI participants can join channels, receive mentions, use inbox/hear
> L53: - OpenClaw-style agent teams can plug into the same workspace over standard REST or MCP surfaces without needing a 

## 星数曲线

```mermaid
xychart-beta
    title "kwalus/Canopy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 303 --> 305
    line [304, 304]
```

2026-10-18 304 → 2026-10-22 304（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3b9f964f0fd6` · [字段定义](../../DATASET.md)*
