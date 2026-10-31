# Hrithik-Gavankar/brainstack

⭐ 24 · Shell · MIT · 推送 2026-09-29 · [GitHub](https://github.com/Hrithik-Gavankar/brainstack) · [官网](https://hrithik-gavankar.github.io/brainstack/) · 个人维护

**为 AI 编程助手提供持久个人与团队上下文层的工具**

面向使用 AI 编程助手的工程师的上下文层，包含两个作用域：个人版 engineer-brain 通过扫描多仓库 git 历史生成并自动更新本地 BRAIN.md 工程师画像，供 standup 生成、季度回顾、模式分析等命令使用；团队版 Team Brain 基于用户自有的 Supabase 项目存储与 Jira key 关联的共享记忆，通过 MCP 工具实现成员 agent 间实时同步。通过平台适配器接入 Cursor、Claude Code、Copilot、Windsurf、Aider、Continue.dev 等助手。个人数据不上传，团队同步为可选。

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

- 扫描 git 历史生成并维护本地 BRAIN.md 工程师画像
- Team Brain 在自有 Supabase 上按 Jira key 共享团队记忆并实时推送
- 支持 6 个 AI 编程助手平台的适配器（Cursor/Claude Code/Copilot/Windsurf/Aider/Continue.dev）
- 提供 standup 生成、季度回顾、模式分析等 CLI 命令

## 适用场景

- 让 Cursor/Claude Code 等助手自动加载我的技能与项目背景，避免每次重复解释
- 从 git 历史生成 standup 笔记与季度回顾
- 同一 Jira initiative 的团队共享 agent 学习到的决策与研究结论

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L39: Brainstack is a **context layer** for AI coding assistants — with two scopes:
> L176: ## Platform Support
> L312: No. Brainstack doesn't write code. It provides context to tools that do.

## 星数曲线

```mermaid
xychart-beta
    title "Hrithik-Gavankar/brainstack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `6a4ebcaf82a7` · [字段定义](../../DATASET.md)*
