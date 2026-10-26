# prokopai/prokop

⭐ 34 · TypeScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/prokopai/prokop) · [官网](https://prokopai.dev/) · 个人维护

**自托管编码 agent 工作台：让多个编码 agent 跨项目保留记忆与技能**

开源桌面/自托管编码工作区，将 Claude Code CLI、Codex CLI 与自带运行时（Prokop runtime）纳入同一界面，用户自选模型供应商。核心机制是跨项目的 agent 记忆与技能：以磁盘上的 Markdown 文件（MEMORY.md/USER.md/SKILL.md）存储，agent 可搜索历史会话并在空闲时复盘已完成对话以更新记忆；学习过程改文件不改模型权重。支持多会话并行（可配 Git worktree）、会话中途插话、解释性审批与手机端访问。单二进制（Bun 服务器）本地运行，无账号无遥测。由单人开发，作者自述尚非企业级就绪；daemon 不支持休眠/重启/崩溃后存活。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三种运行时（Claude Code / Codex CLI / 自带 runtime）同工作区、可会话中途切换
- agent 记忆与技能以 Markdown 文件落地，可读可编辑，跨项目跟随
- agent 空闲时复盘历史会话并沉淀记忆，可逐步撤销
- 多会话并行 + Git worktree，内嵌文件/diff/Git/终端/PR 界面

## 适用场景

- 在一个工作台里同时使用 Claude Code 和 Codex CLI 处理多个任务
- 让编码 agent 记住我的偏好和历史决策，不用每次重新交代
- 在手机上查看和批准本机运行的 agent 会话

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  Prokop is an open-source coding workspace where your agents keep their own memory and skills, search their earlier 
> L42: - **Use the agent you already have.** Run Claude Code or Codex CLI on their own logins, or Prokop's built-in runtim
> L81: |**Prokop**|The built-in runtime|A provider: OpenRouter, DeepSeek, MiniMax, Z.AI (Coding Plan), or Codex (ChatGPT) 

## 星数曲线

```mermaid
xychart-beta
    title "prokopai/prokop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-26 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7f36c96c23e3` · [字段定义](../../DATASET.md)*
