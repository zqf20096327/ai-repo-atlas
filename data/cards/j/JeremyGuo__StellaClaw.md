# JeremyGuo/StellaClaw

⭐ 14 · Rust · 推送 2026-07-15 · [GitHub](https://github.com/JeremyGuo/StellaClaw) · 个人维护 · 中文 README

**自托管 Rust 多智能体运行时：长时任务、多渠道、可恢复**

Rust 实现的自托管 agent 宿主系统，为长时间运行的多渠道 AI 工作提供持久会话、崩溃恢复与隔离执行。架构分为 StellaCodeX Electron 桌面端、Telegram/Web 渠道、宿主服务器与 agent_server 运行时（SessionActor 状态机、provider/tool 循环），可选通过 SSH/sshfs 绑定远程工作区，形成三跳路径。每个会话可独立选择模型、沙箱策略与远程绑定；支持运行时 SKILL.md 技能与分层 Memory。已可用作 Telegram 与桌面/Web 渠道的 agent 宿主。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Conversation/SessionActor 分层：持久边界与执行边界分离，支持崩溃恢复与未完成回合续接
- StellaCodeX/Telegram/Web 多渠道共享同一后端与工作区模型
- Remote 模式经 SSH/sshfs 将会话绑定到远程工作区（三跳路径）
- 运行时 SKILL.md 技能加载/持久化与 user/conversation/public 三层记忆

## 适用场景

- 让 agent 在远程服务器上跑构建、测试与实验并从桌面或 Telegram 监督
- 论文知识库整理与长时研究工作流，产物附着在会话工作区
- 从桌面启动长后台任务，换设备或渠道继续查看进度

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: Stellaclaw is the next-generation runtime for ClawParty: a self-hosted agent system that stays online, receives mes
> L42: |Host server|`stellaclaw`|Channels, conversations, workdirs, Telegram/Web surfaces, config, routing, delivery, runt
> L43: |Agent server|`agent_server` + `stellaclaw_core`|SessionActor state machine, provider/tool loop, compaction, sessio

## 星数曲线

```mermaid
xychart-beta
    title "JeremyGuo/StellaClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f0c0808dc596` · [字段定义](../../DATASET.md)*
