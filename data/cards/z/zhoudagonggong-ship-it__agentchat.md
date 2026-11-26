# zhoudagonggong-ship-it/agentchat

⭐ 3 · TypeScript · MIT · 推送 2026-11-02 · [GitHub](https://github.com/zhoudagonggong-ship-it/agentchat) · 个人维护 · 中文 README

**把多台电脑上的 AI Agent 装进手机聊天软件统一管理与协作**

AgentChat 是一个连接手机与电脑的消息应用：把运行在多台电脑上的 Codex、Claude Code、OpenCode、Goose、DSH 等 Agent 显示为联系人，用户可在手机上查看状态、发消息下达任务、点击批准或拒绝 Agent 的命令执行；不同电脑、不同来源的 Agent 可互相委托任务并回传结果与文件。通过本地接口或读取会话记录接入 Agent，不修改其程序；数据存储在用户自己的电脑，连接走 Tailscale 或官方中继。目前界面为中文，手机应用仅支持 Android。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手机聊天界面管理多台电脑上的多个 Agent，点按批准/拒绝命令
- 跨机器、跨来源 Agent 的一句话任务委托与结果回传
- 通过 Agent 本地接口或读取会话记录接入，不修改 Agent 程序
- 支持 Tailscale 加密直连或账号中继两种连接方式

## 适用场景

- 出门在外时用手机批准或拒绝电脑上 Agent 的命令
- 让多台电脑上的多个 Agent 组队协作完成任务
- 统一查看各机器上 Agent 的运行状态与错误

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: **Every AI agent on all your computers, in one chat app on your phone.**
> L9: Codex, Claude Code, OpenCode, Goose, DSH (DeepSeek Harness)… running on several computers at home and at work. Agent
> L58: - **How agents are connected.** AgentChat doesn't crack any agent and doesn't modify their program files. It connec

## 星数曲线

```mermaid
xychart-beta
    title "zhoudagonggong-ship-it/agentchat 星数(近 2 点)"
    x-axis ["2026-11-02", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-02 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `4ee34920ff90` · [字段定义](../../DATASET.md)*
