# xudong963/conductor_mobile

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-04-07 · [GitHub](https://github.com/xudong963/conductor_mobile) · [官网](https://xudong963.github.io/bringing-conductor-to-my-phone/) · 个人维护

**用 Telegram 远程操控 Mac 上 Conductor 编码代理的桥接工具**

本地优先的桥接进程：必须运行在已安装并初始化 Conductor 的同一台 Mac 上，读取本地 Conductor 数据库并调用本机 Codex 与 Claude Code 二进制。用户通过 Telegram 浏览仓库/分支/工作区、续接或新建代理会话、查看流式输出、排队追加提示并中断当前回合；论坛超级群中每个会话绑定独立话题。限制：单用户、需 Telegram bot token、仅限 macOS 本机场景。提供 npm 发布的 CLI 包与源码两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 Telegram 续接 Codex/Claude 会话并流式输出
- 支持新建聊天、新建工作区（自动创建 git worktree）
- 排队追加提示与中断当前回合
- 论坛超级群中每个会话绑定独立 Telegram 话题

## 适用场景

- 在手机上继续 Mac 上正在进行的编码代理会话
- 不打开 Conductor 界面即可切换仓库、分支和聊天
- 外出时跟进代理输出并发送后续指令

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Use Telegram as a mobile control surface for the Conductor instance already running on your Mac.
> L7: This bridge is local-first: it must run on the same Mac that already has Conductor installed and initialized. It rea
> L292: - New chats inherit the active workspace's preferred agent. Existing Claude workspaces continue as Claude; otherwi

## 星数曲线

```mermaid
xychart-beta
    title "xudong963/conductor_mobile 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7468de92bf13` · [字段定义](../../DATASET.md)*
